from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Equipment)
admin.site.register(models.Client)
admin.site.register(models.Leasing)
admin.site.register(models.LeasingEquipments)