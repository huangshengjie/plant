from django.db import models
from django.utils import timezone


# Create your models here.

# 用户表
class User(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    name = models.CharField(verbose_name='用户名', max_length=10, unique=True)
    password = models.CharField(verbose_name='密码', max_length=16)
    email = models.EmailField(verbose_name='邮箱', max_length=20, unique=True)
    phone = models.IntegerField(verbose_name='手机号', unique=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


# 管理员
class Admin(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    name = models.CharField(verbose_name='管理员名', max_length=10, unique=True)
    password = models.CharField(verbose_name='密码', max_length=16)
    email = models.EmailField(verbose_name='邮箱', max_length=20, unique=True)
    phone = models.IntegerField(verbose_name='手机号', unique=True)

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = '管理员'


# 新闻
class News(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    title = models.CharField(verbose_name='标题', max_length=25)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    author = models.CharField(verbose_name='作者', max_length=15)
    content = models.TextField(verbose_name='内容', default='')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'


# 推送通知
class Notify(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    title = models.CharField(verbose_name='标题', max_length=25)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    content = models.TextField(verbose_name='内容', default='')

    class Meta:
        verbose_name = '推送通知'
        verbose_name_plural = '推送通知'


# 植物
class Plant(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    user_id = models.ForeignKey(verbose_name='用户id', to=User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='植物名', max_length=20)
    address = models.CharField(verbose_name='植物产地', max_length=20)

    class Meta:
        verbose_name = '植物'
        verbose_name_plural = '植物'


# 数字身份证
class DigitalCard(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    plant_id = models.ForeignKey(verbose_name='植物id', to=Plant, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名字', max_length=20)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    identifier = models.CharField(verbose_name='序列号', max_length=200)

    class Meta:
        verbose_name = '数字身份证'
        verbose_name_plural = '数字身份证'


# 相册
class Album(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    plant_id = models.ForeignKey(verbose_name='植物id', to=Plant, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    name = models.CharField(verbose_name='相册名', max_length=20)
    content = models.CharField(verbose_name='内容', max_length=50)

    class Meta:
        verbose_name = '相册'
        verbose_name_plural = '相册'


# 照片
class Photo(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    album_id = models.ForeignKey(verbose_name='相册id', to=Album, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='标题', max_length=15)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    path = models.CharField(verbose_name='路径', max_length=100)

    class Meta:
        verbose_name = '照片'
        verbose_name_plural = '照片'


# 评判
class Judge(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    plant_id = models.ForeignKey(verbose_name='植物id', to=Plant, on_delete=models.CASCADE)
    organizer = models.IntegerField(verbose_name='发起人')
    subject = models.CharField(verbose_name='主题', max_length=20)
    start_date = models.DateTimeField(verbose_name='开始时间', default=timezone.now)
    end_time = models.DateTimeField(verbose_name='结束时间', default=timezone.now)
    content = models.TextField(verbose_name='内容', default='')
    vote = models.IntegerField(verbose_name='投票数', default=0)

    class Meta:
        verbose_name = '评判'
        verbose_name_plural = '评判'


# 排行榜
class Board(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    subject = models.CharField(verbose_name='主题', max_length=20)

    class Meta:
        verbose_name = '排行榜'
        verbose_name_plural = '排行榜'


# 类别
class Category(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    name = models.CharField(verbose_name='类别名', max_length=10)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'


# 植物-类别中间表
class PlantToCategory(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    plant_id = models.ForeignKey(verbose_name='植物id', to=Plant, on_delete=models.CASCADE)
    category_id = models.ForeignKey(verbose_name='类别id', to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '植物-类别中间表'
        verbose_name_plural = '植物-类别中间表'
