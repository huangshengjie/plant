from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'name': 'huang',
               '1': 'china'}
    return render(request, 'application/index.html', context)


# 登录
def login():
    return


# 注册
def registered():
    return
