# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_rental', '0006_auto_20170808_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site3',
            old_name='agentes_id',
            new_name='agentes',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='alteracion_id',
            new_name='alteracion',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='deposito_id',
            new_name='deposito',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='emplazamiento_geo_id',
            new_name='emplazamiento_geo',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='emplazamiento_sitio_id',
            new_name='emplazamiento_sitio',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='evaluacion_id',
            new_name='evaluacion',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='hallazgo_id',
            new_name='hallazgo',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='instrumentos_id',
            new_name='instrumentos',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='localidad_id',
            new_name='localidad',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='prov_bio_id',
            new_name='prov_bio',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='publicacion_id',
            new_name='publicacion',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='rasgos_id',
            new_name='rasgos',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='registrado_id',
            new_name='registrado',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='sedimento_id',
            new_name='sedimento',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='vegetacion_id',
            new_name='vegetacion',
        ),
        migrations.RenameField(
            model_name='site3',
            old_name='zona_id',
            new_name='zona',
        ),
        migrations.RemoveField(
            model_name='ad_cultural',
            name='sitio',
        ),
        migrations.RemoveField(
            model_name='site3',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='site3',
            name='manuscritos',
        ),
        migrations.RemoveField(
            model_name='site3',
            name='tipo_yacimiento',
        ),
        migrations.AddField(
            model_name='site3',
            name='ad_cultural',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='adscripción cultural'),
        ),
        migrations.AddField(
            model_name='site3',
            name='fechado',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='fechado'),
        ),
        migrations.AlterField(
            model_name='ad_cultural',
            name='componente',
            field=models.CharField(max_length=32, verbose_name='Componente'),
        ),
        migrations.AlterField(
            model_name='ad_cultural',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment_rental.Periodo'),
        ),
        migrations.AlterField(
            model_name='site3',
            name='extension_ns',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='extensión norte sur'),
        ),
        migrations.AlterField(
            model_name='site3',
            name='extension_we',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='extensión este oeste'),
        ),
        migrations.AlterField(
            model_name='site3',
            name='pendiente',
            field=models.CharField(blank=True, choices=[('0', 'Plano (0°)'), ('1', 'Suave (1°-5°)'), ('2', 'Mediana (5°-15°'), ('3', 'Marcada (>15°'), ('4', 'No registrado'), ('5', 'Indeterminado'), ('6', 'No aplicable')], max_length=32, null=True, verbose_name='pendiente'),
        ),
        migrations.AlterField(
            model_name='site3',
            name='visibilidad',
            field=models.CharField(blank=True, choices=[('0', 'Alta'), ('1', 'Media'), ('2', 'Baja'), ('3', 'Nula')], max_length=32, null=True, verbose_name='visibilidad'),
        ),
        migrations.DeleteModel(
            name='Componente',
        ),
    ]
