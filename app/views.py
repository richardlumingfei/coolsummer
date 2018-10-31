from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Handu.html')
    #首页

def register(request):
    return render(request,'register.html')
    #注册页面

def cart(request):
    return render(request,'cart.html')
    #购物车

def entry(request):
    return render(request,'entry.html')
    #登录界面

def goods(request):
    return  render(request,'goods_1.html')
    #商品页面
