from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Site3)
admin.site.register(models.Provincia)
admin.site.register(models.Localidad)
admin.site.register(models.Zona)
admin.site.register(models.Subtipo)
admin.site.register(models.Tipo)
admin.site.register(models.Publicaciones)
admin.site.register(models.Tipo_publicaciones)
admin.site.register(models.Provincia_biotica)
admin.site.register(models.Rasgos)
admin.site.register(models.Ad_cultural)
admin.site.register(models.Periodo)