/**
 * Created by Administrator on 16-9-14.
 */


$(function() {

    // 用户(手机号)验证
    $("#name").blur(function () {
        var tel = $(this).val();
        if ($(this).val() == '') return
        if (/^1[3578]\d{9}$/.test(tel)) {
            $.get('/checkname/', {'name': $(this).val()}, function (response) {
                console.log(response)
                if (response.status == 1) {  // 可用
                    $(".p1").html("可以注册的手机号√");
                }
                else {    // 不可用
                    $(".p1").html("该手机号已被注册×");
                }
            })
        }

        else {
            $(".p1").html("用户名不正确")
        }
    })


    // 密码
    $("#pwd").blur(function () {
        if ($(this).val() == '') return
        var pas = $(this).val();
        if (/^[0-9a-zA-Z_]{8,15}$/.test(pas)) {
            $(".p2").html(" ");
        } else {
            $(".p2").html("密码不正确");
        }
    })

    // 再次输入密码
    $("#pwd_again").blur(function () {
        if ($(this).val() == '') return
        var pass = $(this).val();
        if ($(this).val() == $("#pwd").val()) {
            $(".p3").html(" ");
        } else {
            $(".p3").html("密码不一致!");
        }
    })

    // 重置验证码
    function reset_code() {
        var strSum = "";
        for (var i = 0; i < 4; i++) {
            //  数字0-9(10位)       48-57
            var sum = parseInt(Math.random() * 10) + 48;
            //  大写字母A-Z(26位)    65-90
            var num = parseInt(Math.random() * 26) + 65;
            //  小写字母a-z(26位)    97-122
            var smallNum = parseInt(Math.random() * 26) + 97;
            //  随机数
            var a = parseInt(Math.random() * 10);
            if (a % 3 == 0) {
                strSum = strSum.concat(String.fromCharCode(sum));
            } else if (a % 3 == 1) {
                strSum = strSum.concat(String.fromCharCode(num));
            } else {
                strSum = strSum.concat(String.fromCharCode(smallNum));
            }
        }
        $(".identifying_code").html(strSum);
    }

    reset_code()
    // 点击刷新验证码
    $(".identifying_code").click(function () {
        reset_code()
    })

    // 验证框
    $("#code").blur(function () {
        if ($(this).val() == $(".identifying_code").html()) {
            $(".p4").html("");
        } else {
            $(".p4").html("验证码不正确");

        }
    })

})
