from django.db import models
from django.utils import timezone

from django.utils.html import format_html


# 用户表
class User(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    name = models.CharField(verbose_name='用户名', max_length=10, unique=True)
    password = models.CharField(verbose_name='密码', max_length=16)
    email = models.EmailField(verbose_name='邮箱', max_length=20, unique=True)
    phone = models.CharField(verbose_name='手机号', unique=True, max_length=11)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name


# 管理员
class Admin(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    name = models.CharField(verbose_name='管理员名', max_length=10, unique=True)
    password = models.CharField(verbose_name='密码', max_length=16)
    email = models.EmailField(verbose_name='邮箱', max_length=20, unique=True)
    phone = models.IntegerField(verbose_name='手机号', unique=True)

    class Meta:
        db_table = 'admin'
        verbose_name = '管理员'
        verbose_name_plural = '管理员'

    def __str__(self):
        return self.name


# 新闻
class News(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    title = models.CharField(verbose_name='标题', max_length=25)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    author = models.CharField(verbose_name='作者', max_length=15)
    content = models.TextField(verbose_name='内容', default='')

    class Meta:
        db_table = 'news'
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.title


# 推送通知
class Notify(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    title = models.CharField(verbose_name='标题', max_length=25)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    content = models.TextField(verbose_name='内容', default='')

    class Meta:
        db_table = 'notify'
        verbose_name = '推送通知'
        verbose_name_plural = '推送通知'

    def __str__(self):
        return self.title


# 类别
class Category(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    name = models.CharField(verbose_name='类别名', max_length=20)

    class Meta:
        db_table = 'category'
        verbose_name = '植物类别'
        verbose_name_plural = '植物类别'

    def __str__(self):
        return self.name


# 植物
class Plant(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    user = models.ForeignKey(verbose_name='用户', to=User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(verbose_name='植物类别', to=Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(verbose_name='植物名', max_length=20)
    address = models.CharField(verbose_name='植物产地', max_length=20)
    avatar = models.ImageField(verbose_name='植物头像', upload_to='')

    class Meta:
        db_table = 'plant'
        verbose_name = '植物'
        verbose_name_plural = '植物'

    def __str__(self):
        return self.name

    def avatar_image(self):
        return format_html(
            '<img src="/static/{}" width="75px"/>',
            self.avatar,
        )

    avatar_image.short_description = '植物头像'


# 数字身份证
class DigitalCard(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    plant_id = models.ForeignKey(verbose_name='植物id', to=Plant, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名字', max_length=20)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    identifier = models.CharField(verbose_name='序列号', max_length=200)

    class Meta:
        db_table = 'digital_card'
        verbose_name = '数字身份证'
        verbose_name_plural = '数字身份证'


# 相册
class Gallery(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    user = models.ForeignKey(verbose_name='用户id', to=User, on_delete=models.CASCADE)
    plant = models.ForeignKey(verbose_name='植物id', to=Plant, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    name = models.CharField(verbose_name='相册名', max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=50)

    class Meta:
        db_table = 'gallery'
        verbose_name = '相册'
        verbose_name_plural = '相册'

    def __str__(self):
        return self.name


# 照片
class Photo(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    gallery = models.ForeignKey(verbose_name='相册', to=Gallery, on_delete=models.CASCADE, default=1)
    title = models.CharField(verbose_name='标题', max_length=15)
    date = models.DateTimeField(verbose_name='日期', default=timezone.now)
    # path = models.CharField(verbose_name='路径', max_length=100)
    path = models.ImageField(verbose_name='路径', upload_to='')

    class Meta:
        db_table = 'photo'
        verbose_name = '照片'
        verbose_name_plural = '照片'

    def __str__(self):
        return self.title

    def path_image(self):
        return format_html(
            '<img src="/static/{}" width="75px"/>',
            self.path,
        )

    path_image.short_description = '图片'


# 排行榜
class Rank(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    subject = models.CharField(verbose_name='主题', max_length=20)
    title = models.TextField(verbose_name='标题', default='')
    content = models.TextField(verbose_name='内容', default='')

    class Meta:
        db_table = 'rank'
        verbose_name = '排行榜'
        verbose_name_plural = '排行榜'

    def __str__(self):
        return self.subject


# 投票
class Vote(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True, max_length=11)
    user = models.ForeignKey(verbose_name='用户', to=User, on_delete=models.CASCADE)
    plant = models.ForeignKey(verbose_name='植物', to=Plant, on_delete=models.CASCADE)
    rank = models.ForeignKey(verbose_name='排行榜', to=Rank, on_delete=models.CASCADE)
    vote_date = models.DateTimeField(verbose_name='投票时间', default=timezone.now)
    comment = models.TextField(verbose_name='评论', default='')
    vote = models.IntegerField(verbose_name='投票数', default=0)

    class Meta:
        db_table = 'vote'
        verbose_name = '投票'
        verbose_name_plural = '投票'
