# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-27 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20190427_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
