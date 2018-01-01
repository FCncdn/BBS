# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-31 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbs', '0013_auto_20180101_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='blackList',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backList', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('MN', 'Man'), ('WM', 'Women'), ('SY', 'Secrecy')], default='SY', max_length=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='resume',
            field=models.CharField(blank=True, help_text='最多200字', max_length=200, null=True, verbose_name='个人简介'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.CharField(blank=True, help_text='输入个人网站', max_length=200, null=True, verbose_name='个人网站'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phoneNum',
            field=models.CharField(blank=True, help_text='长号', max_length=11, null=True, verbose_name='手机号码'),
        ),
    ]
