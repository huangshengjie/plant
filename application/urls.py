from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('account/', views.account, name='account'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('login/', views.login, name='login'),
    path('registered/', views.registered, name='registered'),
    path('user_center/', views.user_center, name='user_center'),
    path('new_plant/', views.new_plant, name='new_plant'),
    path('plant_detail/<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('new_gallery/', views.new_gallery, name='new_gallery'),
    path('gallery_detail/<int:gallery_id>/', views.gallery_detail, name='gallery_detail'),
    path('user_update/', views.user_update, name='user_update'),
    path('news/', views.news, name='news'),
    path('news_content/', views.news_content, name='news_content'),
    path('notify/', views.notify, name='notify'),
    path('notify_content/', views.notify_content, name='notify_content'),
    path('rank/', views.rank, name='rank'),
    path('gallery/', views.gallery, name='gallery'),
    path('tf_plant/', views.tf_plant, name='tf_plant'),

    path('upload/', views.upload, name='upload'),
]
