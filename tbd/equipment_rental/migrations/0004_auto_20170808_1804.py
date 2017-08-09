# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_rental', '0003_auto_20170728_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad_cultural',
            name='periodo_id',
        ),
        migrations.RemoveField(
            model_name='publicaciones',
            name='financiamiento_id',
        ),
        migrations.AddField(
            model_name='ad_cultural',
            name='periodo',
            field=models.CharField(default='', max_length=32, verbose_name='Periodo'),
        ),
        migrations.DeleteModel(
            name='Periodo',
        ),
    ]