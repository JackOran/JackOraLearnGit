$(function () {
    $(".subShopping").click(function () {

        var sub = $(this);
        // console.log(sub.parents("li").attr("cartid"));
        var $li = sub.parents("li");
        var cartid = $li.attr("cartid");
        $.getJSON("/app/sub_from_cart/", {"cartid": cartid}, function (data) {
            console.log(data);
            if (data["status"] == 200) {
                // var result = data["c_goods_num"];
                var total_price = data["total_price"];
                $("#total_money").html(total_price);
                var span = sub.next("span");
                span.html(data["c_goods_num"]);
                if (data["c_goods_num"] == 0) {
                    $li.remove();
                }
            }
        })
    });

    $(".addShopping").click(function () {
        var $add = $(this);
        var $li = $add.parents("li");
        var cartid = $li.attr("cartid");

        $.getJSON("/app/add_from_cart/", {"cartid": cartid}, function (data) {
            console.log(data);
            if (data["status"] == 200) {
                var total_price = data["total_price"];
                $("#total_money").html(total_price);
                var span = $add.prev("span");
                span.html(data["c_goods_num"]);
            }
        })
    })

    $(".is_choose").click(function () {
        var span = $(this);
        var li = span.parents("li");
        var cartid = li.attr("cartid");
        // console.log(cartid);
        //url
        //参数
        //回调函数
        //返回数据类型
        $.get("/app/change_cart_status/", {"cartid": cartid}, function (data) {
            console.log(data);
            if (data["status"] == "200") {
                var total_money = data["total_money"];
                console.log(total_money);
                $("#total_money").html(total_money);
                if (data["c_is_select"]) {
                    console.log("变为选中状态");
                    span.find("span").html("√");
                    if (data["is_all_select"]){
                        $("#all_select").find("span").html("√");
                    }else {
                        $("#all_select").find("span").html("");
                    }
                } else {
                    console.log("变为非选中状态");
                    span.find("span").html("");
                    $("#all_select").find("span").html("");
                }
            }
        }, "json")
    });

    $("#all_select").click(function () {

        var cart_select = [];
        var cart_unselect = [];
        var $all_select = $(this);
        var menulist = $(".menuList");
        menulist.each(function () {
            var $li = $(this);
            var content = $li.find(".is_choose").find("span").html();
            if ($.trim(content) == "") {
                var cartid = $li.attr("cartid");
                console.log("未选中" + cartid);
                cart_unselect.push(cartid);
            } else {
                var cartid = $li.attr("cartid");
                console.log("选中" + cartid);
                cart_select.push(cartid);
            }
        });
        if (cart_unselect.length == 0) {
            console.log("全部变为未选中");
            $.getJSON("/app/change_status_multi/", {"cart_select": cart_select.join("#")}, function (data) {
                // console.log(data);
                if (data["status"] == "200") {
                    var change_list = data["changelist"];
                    console.log(change_list);
                    for (var i = 0; i < change_list.length; i++) {
                        var cart = change_list[i];
                        $(".menuList").each(function () {
                            var $li = $(this);
                            var cartid = $li.attr("cartid");
                            if (cartid == cart) {
                                $li.find(".is_choose").find("span").html("");
                                $all_select.find("span").html("");
                            }
                        })
                    }
                }
            })
        } else {
            console.log("全部变为选中");
            $.getJSON("/app/change_status_multi_select/", {"cart_unselect": cart_unselect.join("#")}, function (data) {
                console.log(data);
                if (data["status"] == "200"){
                    var change_unlist = data["change_unselect"];
                    console.log(change_unlist);
                    for (var i=0; i<change_unlist.length; i++){
                        var cart_unselect = change_unlist[i];
                        $(".menuList").each(function () {
                            var $li = $(this);
                            if (cart_unselect == $li.attr("cartid")) {
                                $li.find(".is_choose").find("span").html("√");
                                $all_select.find("span").html("√");
                            }
                        })
                    }

                }
            })
        }
    });
    $("#make_order").click(function () {
       //把cartid发送给服务器
       var cart_select = [];
       $(".menuList").each(function () {
           var $li = $(this);
           if ($.trim($li.find(".is_choose").find("span").html()) != "") {
               cart_select.push($li.attr("cartid"));
           }
       });
       if (cart_select.length==0){
           alert("请剁手");
       }else {
           // console.log("下单");
           // console.log(cart_select);
           $.getJSON("/app/generate_order/", {"goods_list": cart_select.join("#")}, function (data) {
               console.log(data);
               window.open("/app/orderdetail/?orderid="+data["order_id"], target="_self");
           })
       }
    })
});