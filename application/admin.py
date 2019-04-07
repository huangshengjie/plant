from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 每页显示10条数据
    list_per_page = 10
    # 控制列表页显示表的哪些字段
    list_display = ['id', 'name', 'password', 'email', 'phone']
    # 侧边栏过滤框
    # list_filter = ['title', 'date', 'author']
    # 搜索框
    search_fields = ['name', 'email', 'phone']


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name', 'password', 'email', 'phone']
    # list_filter = ['title', 'date', 'author']
    search_fields = ['name', 'email', 'phone']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'title', 'date', 'author', 'content']
    list_filter = ['title', 'date', 'author']
    search_fields = ['title', 'author']


@admin.register(Notify)
class NotifyAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'title', 'date', 'content']
    list_filter = ['title', 'date']
    search_fields = ['title', 'date']


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'user_id', 'name', 'address']
    list_filter = ['name', 'address']
    search_fields = ['name', 'address']


@admin.register(DigitalCard)
class DigitalCardAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'plant_id', 'name', 'date', 'identifier']
    list_filter = ['name', 'date']
    search_fields = ['name', 'date']


@admin.register(Gallery)
class AlbumAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'plant', 'date', 'name', 'desc']
    list_filter = ['name', 'date']
    search_fields = ['name', 'date']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'album_id', 'title', 'date', 'path']
    list_filter = ['title', 'date']
    search_fields = ['title', 'date']


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'plant_id', 'organizer', 'subject', 'start_date', 'end_time', 'content', 'vote']
    list_filter = ['subject']
    search_fields = ['subject']


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'subject']
    list_filter = ['subject']
    search_fields = ['subject']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
