# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-03 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0005_auto_20160602_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='run',
            field=models.CharField(default='', max_length=100),
        ),
    ]