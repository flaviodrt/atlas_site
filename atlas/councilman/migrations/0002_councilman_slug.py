# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councilman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='councilman',
            name='slug',
            field=models.CharField(default=None, max_length=150, null=True, verbose_name='Name'),
        ),
    ]
