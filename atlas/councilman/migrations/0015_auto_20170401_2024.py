# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councilman', '0014_auto_20170401_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='councilman',
            name='from_file',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='From file'),
        ),
        migrations.AddField(
            model_name='donation',
            name='from_file',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='From file'),
        ),
    ]
