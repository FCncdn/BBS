# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    # 标题最大长度255,不能重名
    title = models.CharField(u'文章标题', max_length=255, unique=True)
    # 发布板块-使用外键关联Category
    category = models.ForeignKey("Category", verbose_name='板块名称')
    # 上传文件
    #head_img = models.ImageField(upload_to="uploads")
    # 文章内容
    content = models.TextField(u"内容")
    # 文章作者
    author = models.ForeignKey("UserProfile", verbose_name="作者")
    # 发布日期
    publish_date = models.DateTimeField(auto_now=True, verbose_name="发布日期")
    # 帖子的优先级
    priority = models.IntegerField(default=1000, verbose_name="优先级")
    # 帖子的浏览数
    view_count = models.IntegerField(default=0, verbose_name="浏览数")
    # 帖子隐藏
    def __unicode__(self):
        return "<%s,author:%s>" % (self.title, self.author)


class Comment(models.Model):
    # 评论是基于文章的,并且一条评论只属于一个文章
    # 一个文章可以有多个评论,一个评论只属于一个文章
    # 评论文章
    article = models.ForeignKey("Article")
    # 评论用户
    user = models.ForeignKey("UserProfile")
    # 评论内容
    comment = models.TextField(max_length=1000)
    # 评论时间
    date = models.DateTimeField(auto_now=True)

    # 多级评论,是不是评论评论的当前的表(自己表),所以就得和自己做一个关联!
    # 这里parent_comment,必须设置为可以为空,因为如果他是第一评论他是没有父ID的
    parent_comment = models.ForeignKey("self", related_name='p_comment', blank=True, null=True)

    def __unicode__(self):
        return "<user:%s>" % (self.user)


class ThumbUp(models.Model):
    # 给哪一个个文章点的
    article = models.ForeignKey('Article')
    # 用户名
    user = models.ForeignKey('UserProfile')
    # 时间
    date = models.DateTimeField(auto_now=True)


class Category(models.Model):
    # 板块名称
    name = models.CharField(max_length=64, unique=True, verbose_name="板块名称")
    # 板块管理员
    admin = models.ManyToManyField("UserProfile", verbose_name="模块管理员")

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # 名字
    name = models.CharField(max_length=32)
    # 属组
    groups = models.ManyToManyField("UserGroup")
    # 签名
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything here.')
    # 头像
    photo = models.ImageField(upload_to="upload_imgs/", default='upload_imgs/user-1.jpg')

    def __str__(self):      #__unicode__ in pyhton2
        return self.name
    
    def get_absolute_url(self):
        return reverse("personalProfile:personalProfileMain", args=[str(self.pk)])
    


class UserGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name
