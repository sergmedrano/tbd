from django.db import models


class Equipment(models.Model):
	name = models.CharField(max_length=32, verbose_name='nombre')
	branch = models.CharField(max_length=32,blank=True, verbose_name='marca')
	model = models.CharField(max_length=32,blank=True, verbose_name='modelo')
	description = models.CharField(max_length=128, verbose_name='descripción')
	daily_lease_price = models.PositiveIntegerField(verbose_name='precio de arriendo diario')
	stock = models.PositiveIntegerField(verbose_name='inventario')
	stock_available = models.PositiveIntegerField(verbose_name='inventario disponible')

	def __str__(self):
		return self.name


class Client(models.Model):
	name = models.CharField(max_length=64, verbose_name='nombre')

	def __str__(self):
		return self.name


class Leasing(models.Model):
	client = models.ForeignKey(Client, verbose_name='cliente')
	lease_record = models.DateTimeField(verbose_name='fecha/hora de registro')
	return_record = models.DateTimeField(blank=True,null=True,verbose_name='fecha/hora de entrega')
	total_price = models.PositiveIntegerField(verbose_name='precio total')
	return_date = models.DateField(verbose_name='fecha de devolución')
	returned = models.BooleanField(default=False,verbose_name='devueltomak')
	equipments = models.ManyToManyField(Equipment, through='LeasingEquipments',verbose_name='equipamientos')

	def __str__(self):
		return "{} ({})".format(self.client, self.lease_record)

	def str_equipments(self):
		return ",".join(str(x) for x in self.equipments.all())

class LeasingEquipments(models.Model):
	leasing = models.ForeignKey(Leasing,on_delete=models.CASCADE,verbose_name='arriendo')
	equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE,verbose_name='equipamiento')
	quantity = models.PositiveIntegerField(verbose_name='cantidad')
