# Generated by Django 2.2 on 2019-05-12 18:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='管理员名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('email', models.EmailField(max_length=20, unique=True, verbose_name='邮箱')),
                ('phone', models.IntegerField(unique=True, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=20, verbose_name='类别名')),
            ],
            options={
                'verbose_name': '植物类别',
                'verbose_name_plural': '植物类别',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('name', models.CharField(max_length=20, verbose_name='相册名')),
                ('desc', models.CharField(max_length=50, verbose_name='描述')),
            ],
            options={
                'verbose_name': '相册',
                'verbose_name_plural': '相册',
                'db_table': 'gallery',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=25, verbose_name='标题')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('author', models.CharField(max_length=15, verbose_name='作者')),
                ('content', models.TextField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=25, verbose_name='标题')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('content', models.TextField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '推送通知',
                'verbose_name_plural': '推送通知',
                'db_table': 'notify',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=20, verbose_name='植物名')),
                ('address', models.CharField(max_length=20, verbose_name='植物产地')),
                ('avatar', models.ImageField(upload_to='', verbose_name='植物头像')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application.Category', verbose_name='植物类别')),
            ],
            options={
                'verbose_name': '植物',
                'verbose_name_plural': '植物',
                'db_table': 'plant',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.TextField(default='', verbose_name='标题')),
                ('content', models.TextField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '排行榜',
                'verbose_name_plural': '排行榜',
                'db_table': 'rank',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=10, verbose_name='主题')),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('email', models.EmailField(max_length=20, unique=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('vote_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投票时间')),
                ('comment', models.TextField(default='', verbose_name='评论')),
                ('vote', models.IntegerField(default=0, verbose_name='投票数')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Plant', verbose_name='植物')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Rank', verbose_name='排行榜')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '投票',
                'verbose_name_plural': '投票',
                'db_table': 'vote',
            },
        ),
        migrations.AddField(
            model_name='rank',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Subject', verbose_name='主题'),
        ),
        migrations.AddField(
            model_name='plant',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application.User', verbose_name='用户'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=15, verbose_name='标题')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('path', models.ImageField(upload_to='', verbose_name='路径')),
                ('gallery', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application.Gallery', verbose_name='相册')),
            ],
            options={
                'verbose_name': '照片',
                'verbose_name_plural': '照片',
                'db_table': 'photo',
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Plant', verbose_name='植物id'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.User', verbose_name='用户id'),
        ),
        migrations.CreateModel(
            name='DigitalCard',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('identifier', models.CharField(max_length=200, verbose_name='序列号')),
                ('plant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Plant', verbose_name='植物id')),
            ],
            options={
                'verbose_name': '数字身份证',
                'verbose_name_plural': '数字身份证',
                'db_table': 'digital_card',
            },
        ),
    ]
