from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
import logging

from application.models import *

logger = logging.getLogger('app.log')


# 打印日志
def debug(message):
    logger.info(message)


# Create your views here.
def index(request):
    # items = map(str, range(10))
    # context = {'items': items}
    news_list = News.objects.all()
    paginator = Paginator(news_list, 2)  # Show 2 contacts per page

    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'application/index.html', {'news': news})


# 用户登录和注册页
def account(request):
    context = {'message': '欢迎'}
    return render(request, 'application/account.html', context)


# 登录
def login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.filter(email=email, password=password).first()

    if user is None:
        context = {'login_title': '用户不存在',
                   'registered_title': '创建账户'}
        return render(request, 'application/account.html', context)

    if email == user.email:
        if password == user.password:
            return HttpResponseRedirect('/')
        else:
            context = {'login_title': '密码错误',
                       'registered_title': '创建账户'}
            return render(request, 'application/account.html', context)
    else:
        context = {'login_title': '用户名错误',
                   'registered_title': '创建账户'}
        return render(request, 'application/account.html', context)


# 注册
def registered(request):
    email = request.POST['email']
    phone = request.POST['phone']
    name = request.POST['name']
    password = request.POST['password']

    try:
        user = User.objects.get_or_create(email=email, phone=phone, name=name, password=password)
        debug('233' + user is True)
    except:
        context = {'login_title': '欢迎',
                   'registered_title': '注册失败'}
        return render(request, 'application/account.html', context)

    if user is True:
        context = {'login_title': '欢迎',
                   'registered_title': '注册成功'}
        return render(request, 'application/account.html', context)
    else:
        context = {'login_title': '欢迎',
                   'registered_title': '注册失败'}
        return render(request, 'application/account.html', context)


def demo(request):
    debug('user page')
    return render(request, 'application/user.html')
