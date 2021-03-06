# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-26 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='accuracy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='admin_name1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='admin_name2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='admin_name3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='country_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malaria_cause',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malaria_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malaria_risk_factor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malaria_risk_index',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malnutrition_cause',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malnutrition_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malnutrition_risk_factor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='malnutrition_risk_index',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='place_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='tuberculosis_cause',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='tuberculosis_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='tuberculosis_risk_factor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='tuberculosis_risk_index',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
