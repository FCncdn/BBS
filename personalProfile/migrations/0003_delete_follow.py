# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalProfile', '0002_auto_20171226_1814'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
