from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_user/', views.update_user),
]
