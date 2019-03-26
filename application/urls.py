from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('login/', views.login, name='login'),
    path('registered/', views.registered, name='registered'),
    path('user_center/', views.user_center, name='user_center'),
    path('news/', views.news, name='news'),
    path('news_content/', views.news_content, name='news_content'),
    path('notify/', views.notify, name='notify'),
    path('notify_content/', views.notify_content, name='notify_content'),
    path('rank/', views.rank, name='rank'),
]
