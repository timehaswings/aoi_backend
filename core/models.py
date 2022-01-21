from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.


# 标签管理表
class Tags(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    name = models.CharField(max_length=50, verbose_name='标签名称')
    desc = models.CharField(max_length=300, null=True, blank=True, verbose_name='标签描述')
    sort = models.IntegerField(default=100, verbose_name='排序前后')
    is_active = models.BooleanField(default=1, verbose_name='是否启用')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater_name = models.CharField(max_length=40, verbose_name='更新人姓名')
    updater_id = models.IntegerField(verbose_name='更新人ID')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否已删除')

    class Meta:
        db_table = 'tb_tags'
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


# 地区管理表
class Area(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    name = models.CharField(max_length=50, verbose_name='地区名称')
    sort = models.IntegerField(default=100, verbose_name='排序前后')

    class Meta:
        db_table = 'tb_area'
        verbose_name = '地区表'
        verbose_name_plural = verbose_name


# 分类管理表
class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    name = models.CharField(max_length=50, verbose_name='分类名称')
    desc = models.CharField(max_length=300, null=True, blank=True, verbose_name='分类描述')
    is_active = models.BooleanField(default=1, verbose_name='是否启用')
    sort = models.IntegerField(default=100, verbose_name='排序前后')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater_name = models.CharField(max_length=40, verbose_name='更新人姓名')
    updater_id = models.IntegerField(verbose_name='更新人ID')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否已删除')

    class Meta:
        db_table = 'tb_category'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name


# 视频管理表
class BaseVideo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    guid = models.CharField(blank=True, max_length=50, verbose_name='全局唯一标识')
    name = models.CharField(max_length=200, verbose_name='视频名称')
    desc = models.CharField(blank=True, max_length=500, verbose_name='视频描述')
    artists = models.CharField(default='', max_length=200, verbose_name='演员')
    release_time = models.DateField(null=True, verbose_name='上映时间')
    m3u8_path = models.CharField(max_length=300, verbose_name='视频地址')
    thumb_path = models.CharField(max_length=300, verbose_name='缩略图')
    sort = models.IntegerField(default=100, verbose_name='排序前后')
    is_active = models.BooleanField(default=1, verbose_name='是否启用')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建人姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater_id = models.IntegerField(verbose_name='更新人ID')
    updater_name = models.CharField(max_length=40, verbose_name='更新人姓名')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否已删除')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='视频类别')
    tags = models.ManyToManyField(Tags, verbose_name='视频标签')

    class Meta:
        db_table = 'tb_base_video'
        verbose_name = '视频表单'
        verbose_name_plural = verbose_name


# 发现管理表
class Discover(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    name = models.CharField(max_length=50, verbose_name='名称')
    content = models.TextField(blank=True, null=True, verbose_name='内容')
    is_active = models.BooleanField(default=1, verbose_name='是否启用')
    sort = models.IntegerField(default=100, verbose_name='排序前后')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater_name = models.CharField(max_length=40, verbose_name='更新人姓名')
    updater_id = models.IntegerField(verbose_name='更新人ID')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否已删除')

    class Meta:
        db_table = 'tb_discover'
        verbose_name = '发现表'
        verbose_name_plural = verbose_name


# 评论管理表
class Comment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    content = models.CharField(max_length=500, verbose_name='评论内容')
    score = models.DecimalField(default=0.0, max_digits=4, decimal_places=2, verbose_name='评分')
    favor_count = models.IntegerField(default=0, verbose_name='赞成数')
    oppose_count = models.IntegerField(default=0, verbose_name='反对数')
    is_active = models.BooleanField(default=1, verbose_name='是否启用')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否已删除')
    video = models.ForeignKey(BaseVideo, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='视频')
    discover = models.ForeignKey(Discover, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='发现')

    class Meta:
        db_table = 'tb_comment'
        verbose_name = '评论表'
        verbose_name_plural = verbose_name


# 网站配置
class Config(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    module = models.CharField(max_length=80, verbose_name='所属模块')
    name = models.CharField(max_length=80, verbose_name='变量名称')
    desc = models.CharField(max_length=80, verbose_name='变量描述')
    codename = models.CharField(max_length=40, verbose_name='key')
    value = models.CharField(max_length=255, verbose_name='变量value')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater_name = models.CharField(max_length=40, verbose_name='更新人姓名')
    updater_id = models.IntegerField(verbose_name='更新人ID')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否已删除')

    class Meta:
        db_table = 'tb_config'
        verbose_name = '网站配置表'
        verbose_name_plural = verbose_name


# 用户轨迹
class UserTravel(models.Model):
    OPERATION_CHOICES = (
        ('come', '进入'),
        ('leave', '离开'),
        ('favor', '喜爱'),
        ('oppose', '抵触'),
        ('comment', '评论'),
        ('share', '分享'),
        ('reward', '打赏'),
        ('spend', '花钱'),
    )
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='用户')
    video = models.ForeignKey(BaseVideo, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='视频')
    discover = models.ForeignKey(Discover, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='发现')
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES, verbose_name='操作类型')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'tb_user_travel'
        verbose_name = '用户轨迹表'
        verbose_name_plural = verbose_name


# 活动记录
class Deeds(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    title = models.CharField(max_length=80, verbose_name='活动标题')
    content = models.TextField(blank=True, default=[], verbose_name='活动内容')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater_id = models.IntegerField(verbose_name='更新人ID')
    updater_name = models.CharField(max_length=40, verbose_name='更新人姓名')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'tb_deeds'
        verbose_name = '活动表'
        verbose_name_plural = verbose_name


class Menu(models.Model):
    TYPE_CHOICES = (
        ('catalogue', '目录'),
        ('router', '路由')
    )
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    parent_id = models.IntegerField(default=-1, verbose_name='父菜单id')
    name = models.CharField(max_length=80, verbose_name='菜单名称')
    url = models.CharField(max_length=160, blank=True, verbose_name='菜单URL')
    icon = models.CharField(max_length=40, verbose_name='图标')
    component = models.CharField(max_length=160, verbose_name='前端组件')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='类型')
    is_nav = models.BooleanField(default=1, verbose_name='是否为导航')
    is_show = models.BooleanField(default=1, verbose_name='是否展示')
    is_active = models.BooleanField(default=1, verbose_name='是否启用')
    sort = models.IntegerField(default=0, verbose_name='排序前后')
    create_id = models.IntegerField(verbose_name='创建人ID')
    create_name = models.CharField(max_length=40, verbose_name='创建姓名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updater_id = models.IntegerField(verbose_name='更新人ID')
    updater_name = models.CharField(max_length=40, verbose_name='更新人姓名')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'tb_menu'
        verbose_name = '菜单表'
        verbose_name_plural = verbose_name


class GroupMenu(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='自增id')
    menu = models.ForeignKey(Menu, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='菜单id')
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='组别id')

    class Meta:
        db_table = 'tb_group_menu'
        verbose_name = '菜单表'
        verbose_name_plural = verbose_name
