# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20160330_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='portrait',
            field=models.ImageField(default='../myblog/img/touxiang.jpg', upload_to='myblog/img/touxiang.jpg'),
        ),
    ]