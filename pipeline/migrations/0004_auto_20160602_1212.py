# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-02 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0003_auto_20160602_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='ab',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='results',
            name='ad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='results',
            name='end_pos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='results',
            name='pos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='results',
            name='size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='results',
            name='total_reads',
            field=models.IntegerField(),
        ),
    ]
