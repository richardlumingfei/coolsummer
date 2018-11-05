from django.shortcuts import render, redirect

# Create your views here.
from app.models import  wheel, Users


def index(request):
    wheels=wheel.objects.all()
    data={
        'wheels': wheels
    }
    return render(request,'Handu.html',context=data)
    #首页

def cart(request):
    return render(request,'cart.html')
    #购物车

def entry(request):
    return render(request,'entry.html')
    #登录界面

def goods(request):
    return  render(request,'goods_1.html')
    #商品页面

    #注册
def register(request):
    if request.method == 'GET': # 获取注册页面
        return render(request, 'register.html')
    elif request.method == 'POST':  # 注册操作
        # 获取客户端传入的数据
        name = request.POST.get('name')
        password = request.POST.get('pwd')
        print(name,password)

        # 存入数据库
        users = Users()
        users.name = name
        users.password = password
        users.save()

        # 重定向首页
        response = redirect('Handu.html')

        # 状态保持
        response.set_cookie('username', name)

        #return HttpResponse('注册成功')
        return response