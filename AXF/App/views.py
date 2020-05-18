import uuid

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from App.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Good, UserModel, CartModel, Order, \
    OrderGoods

PRICE_UP = '1'
PRICE_DOWN = '2'
SALE_DOWN = '3'

def hello(request):
    return HttpResponse("hello")

# 主页
def home(request):
    wheels = MainWheel.objects.all()
    navs = MainNav.objects.all()
    mustbuys = MainMustBuy.objects.all()
    shops = MainShop.objects.all()
    shop0 = shops[0:1]
    shop1_3 = shops[1:3]
    shop3_7 = shops[3:7]
    shops7_11 = shops[7:11]

    mainshows = MainShow.objects.all()
    data = {
        "title": '首页',
        "wheels": wheels,
        "navs": navs,
        "mustbuys": mustbuys,
        "shops": shops,
        "shop0": shop0,
        "shop1_3": shop1_3,
        "shop3_7": shop3_7,
        "shop7_11": shops7_11,
        "mainshows": mainshows,
    }
    return render(request, "App/main/home/Home.html", context=data)

def market(request):
                                                      #关键字参数
    return redirect(reverse("app:market_with_params", kwargs={"typeid": "104749", "childcid": "0", "order_rule": "0"}))

# 闪购
def marketWithParams(request, typeid, childcid, order_rule):
    food_types = FoodType.objects.all()
    # 过滤
    if childcid == "0":
        goods_list = Good.objects.filter(categoryid=typeid)
    else:
        goods_list = Good.objects.filter(categoryid=typeid).filter(childcid=childcid)

    if order_rule == PRICE_UP:
        goods_list = goods_list.order_by("price")
    elif order_rule == PRICE_DOWN:
        goods_list = goods_list.order_by("-price")
    elif order_rule == SALE_DOWN:
        goods_list = goods_list.order_by("-productnum")

    foodtypes = FoodType.objects.get(typeid=typeid)
    childtypenames = foodtypes.childtypenames
    childtype_list = childtypenames.split("#")
    child_type_list = []
    for child in childtype_list:
        child_type_list.append(child.split(":"))
    data = {
        "title": '闪购',
        "food_types": food_types,
        "goods_list": goods_list,
        "typeid": typeid,
        "childcid":childcid,
        "child_type_list": child_type_list,
    }
    return render(request, "App/main/market/Market.html", context=data)

# 购物车
def cart(request):
    username = request.session.get("username")
    if not username:
        return redirect(reverse("app:user_log_in"))
    user = UserModel.objects.get(u_name=username)
    carts = CartModel.objects.filter(c_user=user)
    is_all_select = True
    for cart_obj in carts:
        if cart_obj.c_is_select == False:
            is_all_select = False
            break
    data = {
        "title": '购物车',
        "carts": carts,
        "is_all_select": is_all_select
    }
    return render(request, 'App/main/cart/Cart.html', context=data)

# 个人中心
def mine(request):
    data = {
        "title": '我的',
        "is_login": False,
    }
    #从session中获取
    username = request.session.get("username")
    if username:
        user = UserModel.objects.get(u_name=username)
        data["is_login"] = True
        data["username"] = user.u_name
        data["usericon"] = "/static/uploads/" + user.u_icon.url

        data["order_wait_receive"] = Order.objects.filter(o_user=user).filter(o_status=2).count()
        data["order_wait_pay"] = Order.objects.filter(o_user=user).filter(o_status=1).count()
    return render(request, 'App/main/mine/Mine.html', context=data)

# 添加到购物车
def add_to_cart(request):
    # print(request.GET.get("goodsid"))
    username = request.session.get("username")
    if username:
        # print(request.GET.get("goodsid"))
        goodsid = request.GET.get("goodsid")
        print(goodsid)
        user = UserModel.objects.get(u_name=username)
        goods = Good.objects.get(pk=goodsid)
        cart_objs = CartModel.objects.filter(c_user=user).filter(c_goods=goods)
        data = {
            "status": "200",
            "msg": "ok",
        }
        # 存在的话每次加一
        if cart_objs.exists():
            cart_obj = cart_objs.first()
            # print(cart_obj)
            cart_obj.c_goods_num = cart_obj.c_goods_num + 1
            cart_obj.save()
        else:
            # 不存在创建
            cart_obj = CartModel()
            cart_obj.c_goods = goods
            cart_obj.c_user = user
            cart_obj.save()

        data["c_goods_num"] = cart_obj.c_goods_num
        return JsonResponse(data=data)
    else:
        # return redirect(reverse("app:user_register"))
        return JsonResponse({"status": "302", "msg": "ok"})

def sub_to_cart(request):
    username = request.session.get("username")
    if username:
        # print(request.GET.get("goodsid"))
        goodsid = request.GET.get("goodsid")
        print(goodsid)
        user = UserModel.objects.get(u_name=username)
        goods = Good.objects.get(pk=goodsid)
        cart_objs = CartModel.objects.filter(c_user=user).filter(c_goods=goods)
        data = {
            "status": "200",
            "msg": "ok",
        }
        if cart_objs.exists():
            cart_obj = cart_objs.first()
            if cart_obj.c_goods_num != 1:
                cart_obj.c_goods_num = cart_obj.c_goods_num - 1
                cart_obj.save()
                data["c_goods_num"] = cart_obj.c_goods_num
                return JsonResponse(data=data)
    else:
        return JsonResponse({"status": "302", "msg": "ok"})

# 注册页面
def user_register(request):
    if request.method == 'GET':
        return render(request, "App/user/user_register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        #上传的文件用File
        icon = request.FILES.get("icon")

        user = UserModel()
        user.u_name = username
        # user.u_password = password
        user.set_password(password=password)
        user.u_email = email
        user.u_icon = icon
        user.save()

        # 发送激活邮件
        token = str(uuid.uuid4())
        cache.set(token, user.id, timeout=10*60)
        template = loader.get_template("App/ActiveEmail.html")
        template_content = template.render({"username": username, "active_url": "http://127.0.0.1:8000/app/user_active/?u_token="+token})
        send_mail("AXF高级VIP激活", "", "18567032383@163.com", [email,], html_message=template_content)
        # 存入session中
        request.session["username"] = username
        return redirect(reverse("app:mine"))


def user_log_out(request):
    request.session.flush()
    return redirect(reverse("app:mine"))


def check_user(request):
    # print(request.GET.get("username"))
    username = request.GET.get("username")
    user = UserModel.objects.filter(u_name=username)
    data = {
        "msg": "ok",
        "status": "200",
    }
    if user.exists():
        data["msg"] = "user exist"
        data["status"] = "901"
    return JsonResponse(data=data)


def user_log_in(request):
    if request.method == "GET":
        return render(request, "App/user/user_login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        users = UserModel.objects.filter(u_name=username)
        if users.exists():
            user = users.first()
            print(user.u_password)
            # user = UserModel()
            if user.verify_password(password=password):
                if user.is_active:
                    request.session["username"] = username
                    # print("ok，进来了")
                    return redirect(reverse("app:mine"))
                else:
                    return HttpResponse("请激活账号使用")
            else:
                print("进入失败")
                return redirect(reverse("app:user_log_in"))
        else:
            print("好菜哦，连里面都进不去")
            return redirect(reverse("app:user_log_in"))


def sub_from_cart(request):
    # print(request.GET.get("cartid"))
    cartid = request.GET.get("cartid")
    data = {
        "status": "200",
        "msg": "ok",
        "c_goods_num": 0,
    }
    cart_obj = CartModel.objects.get(pk=cartid)
    if cart_obj.c_goods_num == 1:
        cart_obj.delete()
    else:
        cart_obj.c_goods_num = cart_obj.c_goods_num - 1
        # print(cart_obj.c_goods_num)
        cart_obj.save()
        data["c_goods_num"] = cart_obj.c_goods_num

    username = request.session.get("username")
    total_price = cal_totalprice(username)
    data["total_price"] = total_price
    return JsonResponse(data=data)


def add_from_cart(request):
    cartid = request.GET.get("cartid")
    data = {
        "status": "200",
        "msg": "ok",
    }
    cart_obj = CartModel.objects.get(pk=cartid)
    cart_obj.c_goods_num = cart_obj.c_goods_num + 1
    cart_obj.save()
    data["c_goods_num"] = cart_obj.c_goods_num

    username = request.session.get("username")
    total_price = cal_totalprice(username)
    data["total_price"] = total_price
    return JsonResponse(data=data)


def change_cart_status(request):
    cartid = request.GET.get("cartid")
    # print(cartid)

    cart_obj = CartModel.objects.get(pk=cartid)
    cart_obj.c_is_select = not cart_obj.c_is_select
    cart_obj.save()
    data = {
        "status": "200",
        "msg": "ok",
    }
    data["c_is_select"] = cart_obj.c_is_select
    is_all_select = True
    total_money = 0
    user = UserModel.objects.get(u_name=request.session.get("username"))
    carts = CartModel.objects.filter(c_user=user)
    for cart in carts:
        if cart.c_is_select == False:
            is_all_select = False
        else:
            total_money += cart.c_goods_num * cart.c_goods.price
    data["is_all_select"] = is_all_select
    data["total_money"] = total_money
    return JsonResponse(data=data)


def change_status_multi(request):
    change_list = request.GET.get("cart_select")
    print(change_list)
    changelist = change_list.split("#")
    print(changelist)
    data = {
        "status": '200',
        "msg": "ok",
    }
    for change in changelist:
        cart_obj = CartModel.objects.get(pk=change)
        cart_obj.c_is_select = False
        cart_obj.save()
    data["changelist"] = changelist
    return JsonResponse(data=data)


def change_status_multi_select(request):
    change_unlist = request.GET.get("cart_unselect")
    print(change_unlist)
    changelist = change_unlist.split("#")
    data = {
        "status": "200",
        "msg": "ok",
    }
    for change in changelist:
        cart_obj = CartModel.objects.get(pk=change)
        cart_obj.c_is_select = True
        cart_obj.save()
    data["change_unselect"] = changelist
    return JsonResponse(data=data)

# 获取总价
def cal_totalprice(username):
    total_money = 0
    user = UserModel.objects.get(u_name=username)
    carts = CartModel.objects.filter(c_user=user).filter(c_is_select=True)
    for cart in carts:
        total_money += cart.c_goods_num * cart.c_goods.price
    return total_money


def generate_order(request):
    goods_list = request.GET.get("goods_list")
    good_list = goods_list.split("#")
    '''
        生成订单
        移除购物车数据
        将购物车数据添加到商品订单中
    '''
    username = request.session.get("username")
    user = UserModel.objects.get(u_name=username)
    order = Order()
    order.o_user =user
    order.save()

    # 移除数据
    for good in good_list:
        ordergoods = OrderGoods()
        ordergoods.o_order = order

        cart_obj = CartModel.objects.get(pk=good)
        ordergoods.o_goods_num = cart_obj.c_goods_num
        ordergoods.o_goods = cart_obj.c_goods
        ordergoods.save()
        cart_obj.delete()

        data = {
            "status": "200",
            "msg": "ok",
            "order_id": order.id,
        }
    return JsonResponse(data=data)


def orderdetail(request):
    order_id = request.GET.get("orderid")
    order = Order.objects.get(pk=order_id)
    data = {
        "order": order,
    }
    return render(request, "App/order/Orderdetail.html", context=data)


def alipy(request):
    orderid = request.GET.get("orderid")
    order = Order.objects.get(pk=orderid)
    order.o_status = 2
    order.save()
    data = {
        "status": "200",
        "msg": "ok",
        "redirect": reverse("app:mine")
    }
    return JsonResponse(data=data)


def order_list_wait_pay(request):
    username = request.session.get('username')
    user = UserModel.objects.get(u_name=username)
    orders = Order.objects.filter(o_user=user).filter(o_status=1)
    data = {
        "orders": orders,
    }
    return render(request, "App/order/OrderList.html", context=data)


def test_email(request):
    # 先加载后渲染
    template = loader.get_template("App/ActiveEmail.html")
    template_content = template.render({"username": "李狗蛋", "active_url": "httpS://www.tom195.com"})
    send_mail("AXF高级VIP激活", "", "18567032383@163.com", ["18567032383@163.com", "1015496993@qq.com",], html_message=template_content)
    return HttpResponse("发送成功")


def user_active(request):
    u_token = request.GET.get("u_token")
    if not u_token:
        return HttpResponse("激活过期，请重新激活")
    u_id = cache.get(u_token)
    user = UserModel.objects.get(pk=u_id)
    user.is_active = True
    user.save()
    cache.delete(u_token)
    return HttpResponse("激活成功")