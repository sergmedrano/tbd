# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_rental', '0007_auto_20170809_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site3',
            name='ad_cultural',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment_rental.Ad_cultural'),
        ),
    ]