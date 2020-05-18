$(function () {
    //输入框内容改变或者是焦点消失
    $("#username").change(function () {
        var username = $(this).val();
        console.log(username);
        //ajax
        $.getJSON("/app/check_user/", {"username": username}, function (data) {
            console.log(data);
            if (data["status"]=="200"){
                $("#username_info").css("color", "green").html("用户名可用");
            }else if (data["status"]== "901"){
                $("#username_info").css("color", "red").html("用户已存在");
            }
        })
    })

    $("#password_confirm").change(function () {
        var password_confirm = $(this).val();
        var password = $("#password").val();
        if (password_confirm == password){
            $("#password_confirm_info").css("color", "green").html("两次输入一致");
        }else{
            $("#password_confirm_info").css("color", "red").html("两次输入不一致");
        }
    })
});

function data_safe() {
    console.log("ok，进来了");
    console.log("啦啦啦");
    //用户名存在也不能提交,通过颜色来找到
    var info_color = $("#username_info").css("color");
    console.log(info_color);
    if (info_color == "rgb(255, 0, 0)"){
        return false;
    }else {
        return true;
    }

    var password_confirm = $("#password_confirm").val();
    var password = $("#password").val();
    if (password == password_confirm){
        var password_new = md5(password);
        $("#password").val(password_new);
        return true;
    }else {
        $("#password_confirm_info").css("color", "red").html("两次输入不一致");
        return false;
    }
}