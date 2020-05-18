import hashlib

from django.db import models

class Main(models.Model):
    img = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=16)

    class Meta:
        abstract = True
class MainWheel(Main):

    class Meta:
        db_table = 'axf_wheel'

class MainNav(Main):

    class Meta:
        db_table = 'axf_nav'

class MainMustBuy(Main):

    class Meta:
        db_table = 'axf_mustbuy'

class MainShop(Main):

    class Meta:
        db_table = 'axf_shop'

'''
trackid,name,img,categoryid,brandname,img1,childcid1,productid1,
longname1,price1,marketprice1,img2,childcid2,productid2,longname2,
price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3
'''
class MainShow(Main):
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=32)
    img1 = models.CharField(max_length=300)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=128)
    price1 = models.FloatField(default=1)
    marketprice1 = models.FloatField(default=2)
    img2 = models.CharField(max_length=300)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=128)
    price2 = models.FloatField(default=1)
    marketprice2 = models.FloatField(default=2)
    img3 = models.CharField(max_length=300)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=128)
    price3 = models.FloatField(default=1)
    marketprice3 = models.FloatField(default=2)

    class Meta:
        db_table = "axf_mainshow"
'''
typeid,typename,childtypenames,typesort
'''
class FoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = "axf_foodtypes"

'''
productid,productimg,productname,productlongname,isxf,pmdesc,
specifics,price,marketprice,categoryid,childcid,childcidname,
dealerid,storenums,productnum) 
values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q",
"","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品",
"4858",200,4);
'''
#商品表
class Good(models.Model):
    productid = models.CharField(max_length=16)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=128)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=True)
    pmdesc = models.BooleanField(default=True)
    specifics = models.CharField(max_length=32)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=1)
    categoryid = models.CharField(max_length=16)
    childcid = models.CharField(max_length=32)
    childcidname = models.CharField(max_length=32)
    dealerid = models.CharField(max_length=16)
    storenums = models.IntegerField(default=5)
    productnum = models.IntegerField(default=10)

    class Meta:
        db_table = 'axf_goods'

class UserModel(models.Model):
    u_name = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=256)
    u_email = models.CharField(max_length=128, unique=True)
    u_icon = models.ImageField(upload_to="icons")
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def set_password(self, password):
        hash = hashlib.md5()
        hash.update(password.encode("utf-8"))
        result = hash.hexdigest()
        self.u_password = result

    def verify_password(self, password):
        # hash = hashlib.md5()
        # hash.update(password.encode("utf-8"))
        # result = hash.hexdigest()
        #这点可能有点bug
        print(password)
        return password == self.u_password

class CartModel(models.Model):
    c_user = models.ForeignKey(UserModel)
    c_goods = models.ForeignKey(Good)
    c_goods_num = models.IntegerField(default=1)
    c_is_select = models.BooleanField(default=True)

class Order(models.Model):
    # 级联用户表
    o_user = models.ForeignKey(UserModel)
    '''
        1.已下单未付款
        2.已下单已付款
        3.已发货
        4.已收货
        5.已收货
        6.已评价
        7.已追评
        8.退货
        9.删除订单
        10.订单取消
    '''
    o_status = models.IntegerField(default=1)
    o_get_time = models.DateTimeField(auto_now=True)

class OrderGoods(models.Model):
    # 级联订单表
    o_order = models.ForeignKey(Order)
    # 级联商品表
    o_goods = models.ForeignKey(Good)
    o_goods_num = models.IntegerField(default=1)