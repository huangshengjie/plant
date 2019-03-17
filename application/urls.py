from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('account/', views.account, name='account'),
    path('login/', views.login, name='login'),
    path('demo/', views.demo, name='demo'),
]
