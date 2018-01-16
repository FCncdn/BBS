# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    # 标题最大长度255,不能重名
    title = models.CharField(u'文章标题', max_length=255, unique=True)
    # 发布板块-使用外键关联Category
    category = models.ForeignKey("Category", verbose_name='板块名称', on_delete=models.CASCADE)
    # 上传文件
    #head_img = models.ImageField(upload_to="uploads")
    # 文章内容
    content = models.TextField(u"内容")
    # 文章作者
    author = models.ForeignKey("UserProfile", verbose_name="作者", on_delete=models.CASCADE)
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True, verbose_name="发布日期")
    # 帖子的优先级
    priority = models.IntegerField(default=1000, verbose_name="优先级")
    # 帖子的浏览数
    view_count = models.IntegerField(default=0, verbose_name="浏览数")
    # 帖子隐藏
    def __str__(self):
        return "<%s,author:%s>" % (self.title, self.author)


class Comment(models.Model):
    # 评论是基于文章的,并且一条评论只属于一个文章
    # 一个文章可以有多个评论,一个评论只属于一个文章
    # 评论文章
    article = models.ForeignKey(
        "Article",
        related_name='comment',
        on_delete=models.CASCADE,
    )
    # 评论用户
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    # 评论内容
    comment = models.TextField(max_length=1000)
    # 评论时间
    date = models.DateTimeField(auto_now=True)

    # 多级评论,是不是评论评论的当前的表(自己表),所以就得和自己做一个关联!
    # 这里parent_comment,必须设置为可以为空,因为如果他是第一评论他是没有父ID的
    parent_comment = models.ForeignKey("self", related_name='p_comment', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "<user:%s>" % (self.user)


class ThumbUp(models.Model):
    # 给哪一个个文章点的
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    # 用户名
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    # 时间
    date = models.DateTimeField(auto_now=True)


class Category(models.Model):
    # 板块名称
    name = models.CharField(max_length=64, unique=True, verbose_name="板块名称")
    # 板块管理员
    admin = models.ManyToManyField("UserProfile", verbose_name="模块管理员", related_name='category')

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename = "headImage.jpg"
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
    #dynamic
    RECEIVE_ALL_DYNAMIC = 'AL'
    RECEIVE_FOLLOW_DYNAMIC = 'FL'
    #email
    RECEIVE_ALL_EMAIL = 'AM'
    RECEIVE_UNREAD_EMAIL = 'EM'
    RECEIVE_NO_EMAIL = 'NM'
    #gender
    MAN = 'MN'
    WOMEN = 'WM'
    SECRECY = 'SY'
    RECEIVE_DYNAMIC_CHOICES = (
        (RECEIVE_ALL_DYNAMIC, '所有人'),
        (RECEIVE_FOLLOW_DYNAMIC, '关注的人'),
    )
    RECEIVE_EMAIL_CHOICES = (
        (RECEIVE_ALL_EMAIL, '所有邮件'),
        (RECEIVE_UNREAD_EMAIL, '未读邮件'),
        (RECEIVE_NO_EMAIL, '不接受'),
    )
    GENDER_CHOICES = (
        (MAN, '男'),
        (WOMEN, '女'),
        (SECRECY, '保密'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    # 名字
    name = models.CharField(max_length=32)
    # 属组
    groups = models.ManyToManyField("UserGroup")
    # 签名
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything here.')
    # 头像
    headImage = models.ImageField(
        upload_to=user_directory_path ,
        default='static/picture/zwei_art.jpg'
    )
    
    #need regular expression
    phoneNum = models.CharField(
        max_length=11, 
        null=True, 
        blank=True, 
        help_text='长号', 
        verbose_name='手机号码'
    )

    resume = models.CharField(
        max_length = 200,
        null = True,
        blank = True,
        help_text = '最多200字',
        verbose_name = '个人简介',
    )

    #need regular expression
    website = models.CharField(
        max_length = 200,
        null = True,
        blank = True,
        help_text = '输入个人网站',
        verbose_name = '个人网站'
    )
    blackList = models.ForeignKey(
        User,
        null = True,
        blank = True,
        on_delete=models.CASCADE,
        related_name='backList'
    )
    receive_dynamic = models.CharField(
        max_length = 2,
        choices = RECEIVE_DYNAMIC_CHOICES,
        default=RECEIVE_ALL_DYNAMIC,
    )
    receive_email = models.CharField(
        max_length = 2,
        choices = RECEIVE_EMAIL_CHOICES,
        default = RECEIVE_ALL_EMAIL,
    )
    gender = models.CharField(
        max_length=2,
        choices = GENDER_CHOICES,
        default = SECRECY,
    )
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("personalProfile:personalProfileMain", args=[str(self.user.pk)])
    def is_receive_dynamic_choices(self):
        return self.receive_dynamic in (self.RECEIVE_ALL_DYNAMIC, self.RECEIVE_FOLLOW_DYNAMIC)
    def is_receive_email_choices(self):
        return self.receive_email in (self.RECEIVE_ALL_EMAIL, self.RECEIVE_NO_EMAIL)
    class Meta:
        permissions = (
            ('edit_profile','Edit profile'),
        )

class UserGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
