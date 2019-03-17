from django.shortcuts import render
import logging


# Create your views here.
def index(request):
    context = {'name': 'huang',
               '1': 'china'}
    return render(request, 'application/index.html', context)


# 用户登录和注册页
def account(request):
    context = {}
    return render(request, 'application/login.html', context)


# 登录
def login(request):
    email = request.POST['email']
    password = request.POST['password']

    context = {'email': email,
               'password': password}

    logging.debug(email)
    logging.debug(password)
    if email == '1@qq.com':
        if password == '1':
            print("yes")
            return render(request, 'application/login.html', context)
        else:
            print('no')


# 注册
def registered():
    return
