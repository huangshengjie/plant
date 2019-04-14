import logging
import os
import uuid
import time

from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import redirect
from django.shortcuts import render

from application.models import *
from plant import settings

logger = logging.getLogger('app.log')


# 打印日志
def debug(message):
    logger.info(message)


def upload(request):
    if request.POST:
        files = request.FILES.getlist('files')
        if len(files) > 0:
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)

            images = []
            for file in files:
                extension = os.path.splitext(file.name)[1]
                file_name = '{}{}'.format(uuid.uuid4(), extension)

                file_path = '{}/{}'.format(settings.MEDIA_ROOT, file_name)
                images.append('{}{}'.format(settings.STATIC_URL, file_name))

                with open(file_path, 'wb') as f:
                    for c in file.chunks():
                        f.write(c)

        return render(request, 'application/show.html', {'images': images})

    return render(request, 'application/upload.html')


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


def rank(request):
    context = {'notify': ''}
    return render(request, 'application/rank.html', context)


def gallery(request):
    context = {'notify': ''}
    return render(request, 'application/gallery.html', context)


def user_center(request):
    if ():
        print('')
    else:
        user_id = request.COOKIES.get('user_id')
        user = User.objects.filter(id=user_id).first()

        plants = Plant.objects.all()
        plant_category = Category.objects.all()
        user_plants = Plant.objects.filter(user=user_id).all()

        user_gallery = Gallery.objects.filter(user=user_id).all()

        context = {'user': user,
                   'plants': plants,
                   'plant_category': plant_category,
                   'user_plant': user_plants,
                   'gallery': user_gallery}

        return render(request, 'application/user_center.html', context)


def user_update(request):
    name = request.POST['name']
    pw = request.POST['password']
    email = request.POST['email']
    phone = request.POST['phone']

    cursor = connection.cursor()
    # sql = 'insert into user (name,password,email,phone) values (%s,%s,%s,%s);' % (name, pw, email, phone)
    sql = "insert into user (name,password,email,phone) " \
          "values ('%s','%s','%s','%s')" % (name, pw, email, phone)
    cursor.execute(sql)
    debug('huang' + sql)

    return redirect('user_center')
    # return render(request, 'application/user_center.html')


def new_plant(request):
    user = request.COOKIES.get('user_id')
    category = request.POST['category']
    name = request.POST['name']
    address = request.POST['address']
    files = request.FILES.get('files')

    extension = os.path.splitext(files.name)[1]
    file_name = '{}{}'.format(uuid.uuid4(), extension)

    file_path = '{}/{}'.format(settings.MEDIA_ROOT, file_name)

    with open(file_path, 'wb') as f:
        for c in files.chunks():
            f.write(c)

    cursor = connection.cursor()
    sql = "insert into plant (name,address,avatar,user_id,category_id)" \
          "values ('%s','%s','%s','%s','%s')" % (name, address, file_name, user, category)
    cursor.execute(sql)

    return redirect('user_center')


def new_gallery(request):
    user_id = request.COOKIES.get('user_id')
    plant_id = request.POST['plant_id']
    name = request.POST['name']
    desc = request.POST['desc']
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # sql = "insert into gallery (user_id,plant_id,name,desc,date)" \
    #       "values (%d,%d,'%s','%s','%s')" % (int(user_id), int(plant_id), name, desc, date)
    #
    # with connection.cursor() as cursor:
    #     cursor.execute(sql)

    Gallery.objects.create(user_id=user_id, plant_id=plant_id, name=name, desc=desc, date=date)

    return redirect('user_center')


def sign_out(request):
    response = render(request, 'application/account.html')
    response.delete_cookie('user_id')
    return response


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
            request.session['user_%d' % user.id] = user.id
            response = render(request, 'application/index.html')
            response.set_cookie('user_id', user.id)
            return response
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
