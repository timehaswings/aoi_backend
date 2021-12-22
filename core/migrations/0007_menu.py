# Generated by Django 3.1.7 on 2021-12-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210906_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='自增id')),
                ('parent_id', models.IntegerField(default=-1, verbose_name='父菜单id')),
                ('name', models.CharField(max_length=80, verbose_name='菜单名称')),
                ('url', models.CharField(max_length=160, verbose_name='菜单URL')),
                ('icon', models.CharField(max_length=40, verbose_name='图标')),
                ('component', models.CharField(max_length=160, verbose_name='前端组件')),
                ('type', models.CharField(choices=[('catalogue', '目录'), ('router', '路由')], max_length=20, verbose_name='类型')),
                ('is_active', models.BooleanField(default=1, verbose_name='是否启用')),
                ('sort', models.IntegerField(default=0, verbose_name='排序前后')),
                ('create_id', models.IntegerField(verbose_name='创建人ID')),
                ('create_name', models.CharField(max_length=40, verbose_name='创建姓名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updater_id', models.IntegerField(verbose_name='更新人ID')),
                ('updater_name', models.CharField(max_length=40, verbose_name='更新人姓名')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '菜单表',
                'verbose_name_plural': '菜单表',
                'db_table': 'tb_menu',
            },
        ),
    ]
