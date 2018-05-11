from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index_views(request):
    resp = HttpResponse('This is index ...')
    return resp


def login_views(request):
    if request.method == 'GET':
        # 判断是否登录过(cookies中是否有id和uphone的值)
        if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            return HttpResponse('欢迎：' + request.COOKIES['uphone'])
        else:
            return render(request, 'login.html')

    else:
        uphone = request.POST.get('uphone', '')
        upwd = request.POST.get('upwd', '')
        if uphone and upwd:
            # 正常处理登录的操作
            # 方式1
            # users = Users.objects.filter(uphone=uphone, upass=upwd)
            # # sql : select * from users where uphone='xxx' and upass='xx'
            # if users:
            #     return HttpResponse('欢迎：' + users[0].uphone)
            # else:
            #     return HttpResponse('登录失败！')

            # 方式2
            users = Users.objects.filter(uphone=uphone)
            # 判断 users 中是否有数据，并给出提示
            if users:
                # uphone 是存在的
                if users[0].upass == upwd:
                    resp = HttpResponse('登录成功')
                    # 判断是否勾选记住密码
                    if 'isSaved' in request.POST:
                        # 将登录者的ID保存进cookie
                        resp.set_cookie('id', users[0].id, 60 * 60 * 24 * 365)
                        # 将登录这的uphone保存进cookie
                        resp.set_cookie('uphone', uphone, 60 * 60 * 24 * 365)
                    return resp
                else:
                    return HttpResponse('密码不对')
            else:
                # uphone是不存在的
                return HttpResponse('电话号码输入不正确')
        else:
            # 给出错误提示并响应回login.html
            return HttpResponse('请输入手机号和密码')


def register_views(request):
    # 1. 如果是 get 请求的话，则响应 register.html 模板
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 2. 如果是 post 请求的话，则接受请求的数据进行处理
        # 2.1 获取请求提交的数据
        uphone = request.POST.get('uphone', '')
        # 2.2 验证用户名称是否存在
        users = Users.objects.filter(uphone=uphone)
        if users:
            # uphone 已经存在
            errMsg = '手机号已存在，请重新输入'
            return render(request, 'register.html', locals())
        else:
            upwd = request.POST.get('upwd', '')
            uname = request.POST.get('uname', '')
            uemail = request.POST.get('uemail', '')
            Users.objects.create(uphone=uphone, upass=upwd,
                                 uname=uname, uemail=uemail)
            return HttpResponse('Register OK')
