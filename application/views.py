import logging

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from application.models import *

logger = logging.getLogger('app.log')


# 打印日志
def debug(message):
    logger.info(message)


def index(request):
    context = {'news': ''}
    return render(request, 'application/index.html', context)


def news(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 2)  # Show 2 contacts per page

    page = request.GET.get('page')
    news = paginator.get_page(page)
    context = {'news': news}
    return render(request, 'application/news.html', context)


def news_content(request):
    news_id = request.GET['id']
    news = News.objects.filter(id=news_id).first()
    context = {'news': news}
    return render(request, 'application/news_content.html', context)


def notify(request):
    notify_list = Notify.objects.all()
    paginator = Paginator(notify_list, 2)  # Show 2 contacts per page

    page = request.GET.get('page')
    notify = paginator.get_page(page)
    context = {'notify': notify}
    return render(request, 'application/notify.html', context)


def notify_content(request):
    notify_id = request.GET['id']
    notify = Notify.objects.filter(id=notify_id).first()
    context = {'notify': notify}
    return render(request, 'application/notify_content.html', context)


def user_center(request):
    return render(request, 'application/user_center.html')


def sign_out(request):
    return render(request, 'application/account.html')


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
