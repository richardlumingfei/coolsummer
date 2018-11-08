import hashlib
import time
import uuid

from django.http import HttpResponse, JsonResponse
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


def goods(request):
    return  render(request,'goods_1.html')
    #商品页面

    #注册
def genarate_password(param):
    sha = hashlib.sha256()
    sha.update(param.encode('utf-8'))
    return sha.hexdigest()

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # try:
            user = Users()
            user.name = request.POST.get('name')
            user.password = genarate_password(request.POST.get('pwd'))


            user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))

            user.save()

            # 状态保持
            request.session['token'] = user.token

            # 重定向
            #HttpResponse('注册成功,正在为您跳转至登录页面......')
            # time.sleep(1)
            return redirect('app:entry')

        # except:
        #      return HttpResponse('注册失败(该用户已被注册)')
def checkname(request):
    name = request.GET.get('name')

    responseData = {
        'msg': '账号可用',
        'status': 1 # 1标识可用，-1标识不可用
    }

    try:
        user = Users.objects.get(name=name)
        responseData['msg'] = '该手机号已被使用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)


def logout(request):
    request.session.flush()
    return redirect('app:index')


def entry(request):
    if request.method == 'GET':
        return render(request, 'entry.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pwd')

        try:
            user = Users.objects.get(name=name)
            if user.password == genarate_password(password):    # 登录成功

                # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'entry'))
                user.save()
                request.session['token'] = user.token
                return redirect('app:index')
            else:   # 登录失败
                return render(request, 'entry.html', context={'passwdErr': '密码错误!'})
        except:
            return render(request, 'entry.html', context={'nameErr':'账号不存在!'})