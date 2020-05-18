

function password_safe() {
    console.log("ok，进来了");
    console.log("啦啦啦");

    var password_input = $("#password");
    var password = password_input.val();
    var password_new =  md5(password);
    password_input.val(password_new);
    console.log(password_new);

    return true;
}