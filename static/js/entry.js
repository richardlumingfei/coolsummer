/**
 * Created by Administrator on 16-9-19.
 */

$(function(){
    function reset_code(){
        var strSum="";
        for(var i=0;i<4;i++)
        {
            //  数字0-9(10位)       48-57
            var sum=parseInt(Math.random()*10)+48;
            //  大写字母A-Z(26位)    65-90
            var num=parseInt(Math.random()*26)+65;
            //  小写字母a-z(26位)    97-122
            var smallNum=parseInt(Math.random()*26)+97;
            //  随机数
            var a=parseInt(Math.random()*10);
            if(a%3==0)
            {
                strSum=strSum.concat(String.fromCharCode(sum));
            }else if(a%3==1){
                strSum=strSum.concat(String.fromCharCode(num));
            }else{
                strSum=strSum.concat(String.fromCharCode(smallNum));
            }
        }
        $(".codes").html(strSum);
    }
    reset_code();

    // 验证码
    $(".codes").click(function(){
        reset_code();
    })

    //判断是否存在该用户(匹配用户名和密码是否都一致)
    $(".login_btn").click(function(e){
        if($(".login_txt").val().length<=0){
            $(".login_error").html("用户名/密码/验证码不能为空");
            return
        }

        //判断是否存在该用户

    })
})

