# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response
from . import models
from django.contrib import auth
from django.http import HttpResponseRedirect
from django_comments.models import Comment
# Create your views here.


def index(request):
    bbs_list1 = models.Article.objects.filter(category_id=1)
    bbs_list2 = models.Article.objects.filter(category_id=2)
    bbs_list3 = models.Article.objects.filter(category_id=3)
    bbs_list4 = models.Article.objects.filter(category_id=4)
    bbs_list5 = models.Article.objects.filter(category_id=5)
    bbs_list6 = models.Article.objects.filter(category_id=6)
    bbs_category_one = models.Category.objects.get(id='1')
    bbs_category_two = models.Category.objects.get(id='2')
    bbs_category_three = models.Category.objects.get(id='3')
    bbs_category_four = models.Category.objects.get(id='4')
    bbs_category_five = models.Category.objects.get(id='5')
    bbs_category_six = models.Category.objects.get(id='6')
    user = request.user
    return render_to_response('index.html', locals())

def article(request, article_id):
    user = request.user
    article_obj = models.Article.objects.get(id=article_id)
    count = article_obj.view_count
    count = count+1
    article_obj.view_count = count
    article_obj.save(update_fields=["view_count"])
    return render_to_response('article.html', locals())


def sub_comment(request):
    article_id = request.POST.get('article_id')
    comment = request.POST.get('comment_content')
    Comment.objects.create(
        content_type_id=12,
        object_pk=article_id,
        site_id=1,
        user=request.user,
        comment=comment,
    )
    return HttpResponseRedirect('/article/%s' % article_id)

def partition(request, category_id):
    user = request.user
    partition_obj = models.Category.objects.get(id=category_id)
    bbs_list = models.Article.objects.filter(category_id=category_id)
    return render_to_response('partition.html', locals())

def login(request):
    return render_to_response('login.html')

def sub_page(request):
    bbs_category = models.Category.objects.all()
    user = request.user
    return render_to_response('articlepost.html', locals())

def logout_view(request):
    user = request.user
    auth.logout(request)
    response = HttpResponse("<b>%s</b> Logged out! <br/><a href='/login/'>Re-Login</a>" % user)
    return response


def sub_article(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    author = models.UserProfile.objects.get(user__username=request.user)
    category = models.Category.objects.get(name=request.POST.get('category'))
    models.Article.objects.create(
        title=title,
        author=author,
        content=content,
        view_count=1,
        category=category,
    )
    return   HttpResponseRedirect('/')

def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        response = HttpResponseRedirect('/')
        return response
    else:
        return render_to_response('login.html', {'login_err': 'Wrong username or password!'})


