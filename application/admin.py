from django.contrib import admin
from .models import *

admin.site.site_header = "植物管家后台系统"


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
    list_display = ['id', 'avatar_image', 'user', 'category', 'name', 'address']
    list_filter = ['user', 'category', 'name', 'address']
    search_fields = ['user', 'category', 'name', 'address']


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
    list_display = ['id', 'gallery', 'title', 'date', 'path_image']
    list_filter = ['title', 'date']
    search_fields = ['title', 'date']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'user', 'plant', 'rank', 'vote_date', 'comment', 'vote']
    list_filter = ['rank']
    search_fields = ['rank']


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
