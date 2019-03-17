from django.shortcuts import render
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger('app.log')


# 打印日志
def debug(message):
    logger.info(message)


# Create your views here.
def index(request):
    debug('def index')
    context = {'name': 'huang',
               '1': 'china'}
    return render(request, 'application/index.html', context)


# 用户登录和注册页
def account(request):
    debug('def account')
    context = {'message': '欢迎'}
    return render(request, 'application/account.html', context)


# 登录
def login(request):
    debug('def login')

    email = request.POST['email']
    password = request.POST['password']

    debug(email)
    debug(password)

    if email == '1@qq.com':
        if password == '1':
            debug('yes')
            return HttpResponseRedirect('')
        else:
            debug('密码错误')
            context = {'message': '用户名错误'}
            return render(request, 'application/account.html', context)
    else:
        debug('用户名错误或不存在')

    


# 注册
def registered():
    return


# 注册
def demo(request):
    debug('user page')
    return render(request, 'application/user.html')
