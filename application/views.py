from django.shortcuts import render
import logging

logger = logging.getLogger('app.log')


# Create your views here.
def index(request):
    logger.info('def index')
    context = {'name': 'huang',
               '1': 'china'}
    return render(request, 'application/index.html', context)


# 用户登录和注册页
def account(request):
    logger.info('def account')
    context = {}
    return render(request, 'application/login.html', context)


# 登录
def login(request):
    logger.info('def login')
    email = request.POST['email']
    password = request.POST['password']

    context = {'email': email,
               'password': password}

    logger.info(email)
    logger.info(password)
    if email == '1@qq.com':
        if password == '1':
            logger.info('yes')
            return render(request, 'application/login.html', context)
        else:
            logger.info('no')


# 注册
def registered():
    return


# 注册
def demo(request):
    logger.debug('user page')
    return render(request, 'application/user.html')
