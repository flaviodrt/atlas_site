# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councilman', '0006_auto_20170326_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='councilman',
            name='sequential_id',
            field=models.IntegerField(default=None, null=True, verbose_name='Sequential Id'),
        ),
    ]