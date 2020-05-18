$(function () {
    //全部分类的点击
    $("#all_type").click(function () {

        $("#all_type_container").show();
        $("#all_type_logo").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
        $("#all_sort_conainer").hide();
        $("#all_sort_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
    });
    $("#all_type_container").click(function () {
        $(this).hide();
        $("#all_type_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")

    });

    //综合排序的点击事件
    $("#sort_rule").click(function () {
        $("#all_sort_conainer").show();
        $("#all_sort_logo").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
        $("#all_type_container").hide();
        $("#all_type_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
    });
    $("#all_sort_conainer").click(function () {
        $(this).hide();
        $("#all_sort_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")

    });

    $(".addShopping").click(function () {
        var addShopping = $(this);
        // console.log(addShopping.attr("class"));
        // console.log(addShopping.prop("class"));
        // console.log(addShopping.attr("goodsid"));
        // console.log(addShopping.prop("goodsid"));
        var goodsid = addShopping.attr("goodsid");
        $.getJSON("/app/add_to_cart/", {"goodsid":goodsid}, function (data) {
            console.log(data);
            if (data["status"]=="200"){
                console.log("ok，可以加一了");
                var result = data["c_goods_num"];
                var span = addShopping.prev("span");
                span.html(result);
            }else if (data["status"]=="302"){
                //打开注册页面
                window.open("/app/user_log_in/", target = "_self");
            }
        })
    });

    $(".subShopping").click(function () {
        var subShopping = $(this);
        var goodsid = subShopping.attr("goodsid");

        $.getJSON("/app/sub_to_cart/", {"goodsid": goodsid}, function (data) {
            console.log(data);
            if (data["status"]=="200"){
                console.log("ok,可以减一");
                var result = data["c_goods_num"];
                var span = subShopping.next("span");
                span.html(result);
            }else if (data["status"]=="302"){
                window.open("/app/user_log_in/", target="_self");
            }
        })
    })
});