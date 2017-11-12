# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from . import models


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
    return render_to_response('index.html', locals())


def article(request, article_id):
    article_obj = models.Article.objects.get(id=article_id)
    return render_to_response('article.html', locals())


def partition(request, category_id):
    partition_obj = models.Category.objects.get(id=category_id)
    bbs_list = models.Article.objects.filter(category_id=category_id)
    return render_to_response('partition.html', locals())
