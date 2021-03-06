# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_rental', '0005_auto_20170808_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad_cultural',
            old_name='componente_id',
            new_name='componente',
        ),
        migrations.RenameField(
            model_name='ad_cultural',
            old_name='periodo_id',
            new_name='periodo',
        ),
        migrations.RemoveField(
            model_name='site3',
            name='ad_cultural_id',
        ),
        migrations.AddField(
            model_name='ad_cultural',
            name='sitio',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='equipment_rental.Site3', verbose_name='sitio_id'),
        ),
    ]
