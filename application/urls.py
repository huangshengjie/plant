from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('account/', views.account, name='account'),
    path('login/', views.login, name='login'),
    path('registered/', views.registered, name='registered'),
    path('demo/', views.demo, name='demo'),
]
