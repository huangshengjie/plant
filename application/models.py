from django.db import models


# Create your models here.

# 用户表
class User(models.Model):
    id = models.AutoField(primary_key=True, max_length=11)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=11)


# 管理员
class Admin(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    email = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=11)


# 新闻
class News(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    title = models.CharField(max_length=25)
    date = models.DateTimeField
    author = models.CharField(max_length=15)
    content = models.TextField


# 推送通知
class Notify(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    title = models.CharField(max_length=25)
    date = models.DateTimeField
    content = models.TextField


# 植物
class Plant(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    title = models.TextField


# 数字身份证
class DigitalCard(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    plant_id = models.ForeignKey(to=Plant, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    date = models.DateTimeField
    identifier = models.CharField(max_length=200)


# 相册
class Album(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    plant_id = models.ForeignKey(to=Plant, on_delete=models.CASCADE)
    date = models.DateTimeField
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=50)


# 照片
class Photo(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    album_id = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    date = models.DateTimeField
    path = models.CharField(max_length=100)


# 评判
class Judge(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    plant_id = models.ForeignKey(to=Plant, on_delete=models.CASCADE)
    organizer = models.IntegerField(max_length=11)
    subject = models.CharField(max_length=20)
    start_date = models.DateTimeField
    end_time = models.DateTimeField
    content = models.TextField
    star = models.IntegerField(max_length=11)


# 排行榜
class Board(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    subject = models.CharField(max_length=20)


# 类别
class Category(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    name = models.CharField(max_length=10)


# 中间表
class PlantToCategory(models.Model):
    id = models.IntegerField(primary_key=True, max_length=11)
    plant_id = models.ForeignKey(to=Plant, on_delete=models.CASCADE)
    category_id = models.ForeignKey(to=Category, on_delete=models.CASCADE)
