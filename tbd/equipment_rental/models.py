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

#------------------------------------------------------------------------------------------------------------

class Provincia(models.Model):
	prov_id = models.AutoField(primary_key=True, verbose_name='prov_id')
	nombre = models.CharField(max_length=32, verbose_name='Provincia')

	def __str__(self):
		return str(self.nombre)

class Localidad(models.Model):
	localidad_id = models.AutoField(primary_key=True, verbose_name='localidad_id')
	nombre_loc = models.CharField(max_length=32, verbose_name='Localidad')
	prov_id = models.ForeignKey(Provincia, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.nombre_loc)

class Provincia_biotica(models.Model):
	prov_bio_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Provincia Biótica')

	def __str__(self):
		return str(self.nombre)

class Emplazamiento_geo(models.Model):
	emplazamiento_geo_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Emplazamiento geomorfologico')

	def __str__(self):
		return str(self.nombre)

class Emplazamiento_sitio(models.Model):
	emplazamiento_sitio_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Emplazamiento sitio')

	def __str__(self):
		return str(self.nombre)

class Zona(models.Model):
	zona_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Zona')

	def __str__(self):
		return str(self.nombre)

class Naturaleza(models.Model):
	naturaleza_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Naturaleza')

	def __str__(self):
		return str(self.nombre)

class Tipo_sedimento(models.Model):
	sedimento_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Sedimiento')
	naturaleza_id = models.ForeignKey(Naturaleza, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.nombre)

class Tipo_deposito(models.Model):
	deposito_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Tipo deposito')

	def __str__(self):
		return str(self.nombre)

class Vegetacion(models.Model):
	vegetacion_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Vegetacion')

	def __str__(self):
		return str(self.nombre)

class Distribucion_espacial(models.Model):
	distribucion_espacial_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Distribucion espacial')

	def __str__(self):
		return str(self.nombre)

class Tipo_hallazgo(models.Model):
	hallazgo_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Tipo Hallazgo')
	distribucion_id = models.ForeignKey(Distribucion_espacial, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.nombre)

class Periodo(models.Model):
	periodo_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Periodo')

	def __str__(self):
		return str(self.nombre)

class Ad_cultural(models.Model):
	ad_cultural_id = models.AutoField(primary_key=True)
	componente = models.CharField(max_length=32, verbose_name='Componente')
	periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.periodo)

class Instrumentos(models.Model):
	instrumentos_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Instrumentos')

	def __str__(self):
		return str(self.nombre)

class Evaluacion(models.Model):
	evaluacion_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Evaluacion')

	def __str__(self):
		return str(self.nombre)

class Rasgos(models.Model):
	rasgos_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Rasgos')

	def __str__(self):
		return str(self.nombre)

class Por_alteracion(models.Model):
	alteracion_id = models.AutoField(primary_key=True)
	porcentaje = models.CharField(max_length=32, verbose_name='Porcentaje de alteracion')

	def __str__(self):
		return str(self.porcentaje)

class Tipo_agente(models.Model):
	agente_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Agente')
	impacto = models.CharField(max_length=32, verbose_name='Impacto')

	def __str__(self):
		return "{} ({})".format(self.nombre, self.impacto)

class Impacto(models.Model):
	impacto_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Impacto')

	def __str__(self):
		return str(self.nombre)

class Agentes(models.Model):
	agente_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Agente')
	importancia = models.CharField(max_length=32, verbose_name='Importancia')
	agente_id = models.ForeignKey(Tipo_agente, on_delete=models.CASCADE)
	impacto_id = models.ForeignKey(Impacto, on_delete=models.CASCADE)

	def __str__(self):
		return "{} ({})".format(self.nombre, self.importancia)

class Tipo(models.Model):
	tipo_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='nombre')

	def __str__(self):
		return str(self.nombre)

class Subtipo(models.Model):
	subtipo_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Impacto')
	tipo_id = models.ForeignKey(Tipo, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.nombre)

class Imagenes(models.Model):
	imagenes_id = models.AutoField(primary_key=True)
	ruta = models.CharField(max_length=32, verbose_name='Ruta imagen')
	formato = models.CharField(max_length=32, verbose_name='Formato imagen')
	autor =  models.CharField(max_length=32, verbose_name='autor',default="Desconocido")
	descripcion =  models.CharField(max_length=32, verbose_name='descripcion',default="Desconocido")

	def __str__(self):
		return str(self.ruta)

class Registrado_por(models.Model):
	registrado_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Registrado por')
	email = models.CharField(max_length=32, verbose_name='email')

	def __str__(self):
		return str(self.nombre)

class Tipo_publicaciones(models.Model):
	tipo_pub_id = models.AutoField(primary_key=True)
	tipo = models.CharField(max_length=32, verbose_name='tipo publicacion')

	def __str__(self):
		return str(self.tipo)

class Financiamiento(models.Model):
	financiamiento_id = models.AutoField(primary_key=True)
	proyecto = models.CharField(max_length=32, verbose_name='proyecto')
	descripcion = models.CharField(max_length=32, verbose_name='descripcion')
	area = models.CharField(max_length=32, verbose_name='area')

	def __str__(self):
		return str(self.proyecto)

class Publicaciones(models.Model):
	dbi = models.CharField(max_length=32, verbose_name='dbi')
	titulo = models.CharField(max_length=32, verbose_name='titulo')
	año = models.PositiveIntegerField(verbose_name='año')
	volumen = models.PositiveIntegerField(verbose_name='volumen')
	paginas = models.PositiveIntegerField(verbose_name='paginas')
	pais = models.CharField(max_length=32, verbose_name='pais')
	ciudad = models.CharField(max_length=32, verbose_name='ciudad')
	tipo_pub_id = models.ForeignKey(Tipo_publicaciones, on_delete=models.CASCADE)
	#financiamiento_id = models.ForeignKey(Financiamiento, on_delete=models.CASCADE, blank="true")

	def __str__(self):
		return "{} ({})".format(self.nombre)

class Autores(models.Model):
	autor_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Autor')
	email = models.CharField(max_length=32, verbose_name='email')

	def __str__(self):
		return str(self.nombre)

class Instituciones(models.Model):
	institucion_id = models.AutoField(primary_key=True)
	institucion = models.CharField(max_length=32, verbose_name='Institucion')
	direccion = models.CharField(max_length=32, verbose_name='direccion')
	ciudad = models.CharField(max_length=32, verbose_name='ciudad')
	pais = models.CharField(max_length=32, verbose_name='pais')
	sitio_web = models.CharField(max_length=32, verbose_name='sitio web')

	def __str__(self):
		return str(self.nombre)

class Publicaciones_Autores(models.Model):
	publicacion_doi = models.ForeignKey(Publicaciones,on_delete=models.CASCADE,verbose_name='doi')
	autor_id = models.ForeignKey(Autores,on_delete=models.CASCADE,verbose_name='Autor')

class Financiamiento_Instituciones(models.Model):
	financimiento_id = models.ForeignKey(Financiamiento,on_delete=models.CASCADE,verbose_name='financiamiento')
	institucion_id = models.ForeignKey(Instituciones,on_delete=models.CASCADE,verbose_name='institucion')
	monto = models.PositiveIntegerField(verbose_name='monto')

class Instituciones_Autores(models.Model):
	institucion_id = models.ForeignKey(Instituciones,on_delete=models.CASCADE,verbose_name='institucion')
	autor_id = models.ForeignKey(Autores,on_delete=models.CASCADE,verbose_name='Autor')

class Instituciones_registrado(models.Model):
	institucion_id = models.ForeignKey(Instituciones,on_delete=models.CASCADE,verbose_name='institucion')
	registrado_id = models.ForeignKey(Registrado_por,on_delete=models.CASCADE,verbose_name='registrado por')

class Tipo_fuente_agua(models.Model):
	fuente_id = models.AutoField(primary_key=True)
	tipo = models.CharField(max_length=32, verbose_name='Tipo fuente de agua')

	def __str__(self):
		return str(self.tipo)

class Camino(models.Model):
	camino_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='nombre camino')

	def __str__(self):
		return str(self.nombre)

class Funcion_inferida(models.Model):
	inferida_if =models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Funcion inferida')

	def __str__(self):
		return str(self.nombre)

class Site3(models.Model):
	name = models.CharField(max_length=32, verbose_name='nombre')
	longitud = models.CharField(max_length=32,blank=True,null=True, verbose_name='longitud')
	latitud = models.CharField(max_length=32,blank=True,null=True, verbose_name='latitud')
	altitud = models.CharField(max_length=128,blank=True,null=True, verbose_name='altitud')
	localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, blank=True, null=True)
	prov_bio = models.ForeignKey(Provincia_biotica, on_delete=models.CASCADE, null=True, blank=True)
	zona = models.ForeignKey(Zona, on_delete=models.CASCADE, null=True, blank=True)
	ad_cultural = models.ForeignKey(Ad_cultural, on_delete=models.CASCADE,null=True,blank=True)
	visitado = models.CharField(max_length=32,blank=True,null=True,verbose_name='visitado',choices=(('0', 'Si'), ('1', 'No')))
	visibilidad = models.CharField(max_length=32,blank=True,null=True, verbose_name='visibilidad',choices=(('0','Alta'),('1','Media'),('2','Baja'),('3','Nula')))
	pendiente = models.CharField(max_length=32,blank=True,null=True, verbose_name='pendiente',choices=(('0','Plano (0°)'),('1','Suave (1°-5°)'),('2','Mediana (5°-15°'),('3','Marcada (>15°'),('4','No registrado'),('5','Indeterminado'),('6','No aplicable')))
	extension_ns = models.PositiveIntegerField(blank=True,null=True,verbose_name='extensión norte sur')
	extension_we = models.PositiveIntegerField(blank=True,null=True,verbose_name='extensión este oeste')
	observacion = models.CharField(max_length=2560,blank=True,null=True, verbose_name='observaciones')
	fechado = models.CharField(max_length=50, verbose_name='fechado', blank=True, null=True)
	emplazamiento_geo = models.ForeignKey(Emplazamiento_geo, on_delete=models.CASCADE,null=True,blank=True)
	emplazamiento_sitio = models.ForeignKey(Emplazamiento_sitio, on_delete=models.CASCADE,null=True,blank=True)
	sedimento = models.ForeignKey(Tipo_sedimento, on_delete=models.CASCADE,null=True,blank=True)
	deposito = models.ForeignKey(Tipo_deposito, on_delete=models.CASCADE,null=True,blank=True)
	vegetacion = models.ForeignKey(Vegetacion, on_delete=models.CASCADE,null=True,blank=True)
	hallazgo = models.ForeignKey(Tipo_hallazgo, on_delete=models.CASCADE,null=True,blank=True)
	instrumentos = models.ForeignKey(Instrumentos, on_delete=models.CASCADE,null=True,blank=True)
	evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE,null=True,blank=True)
	rasgos = models.ForeignKey(Rasgos, on_delete=models.CASCADE,null=True,blank=True)
	alteracion = models.ForeignKey(Por_alteracion, on_delete=models.CASCADE,null=True,blank=True)
	agentes = models.ForeignKey(Agentes, on_delete=models.CASCADE,null=True,blank=True)
	registrado = models.ForeignKey(Registrado_por, on_delete=models.CASCADE,null=True,blank=True)
	publicacion = models.ForeignKey(Publicaciones, on_delete=models.CASCADE,null=True,blank=True)
	imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE,null=True,blank=True)
	funcion_inferida = models.ForeignKey(Funcion_inferida, on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return str(self.name)

class distancia_camino(models.Model):
	camino_id = models.ForeignKey(Camino,on_delete=models.CASCADE,verbose_name='camino')
	sitio_id = models.ForeignKey(Site3,on_delete=models.CASCADE)
	distancia = models.PositiveIntegerField(verbose_name='distancia')

class distancia_fuente_agua(models.Model):
	sitio_id = models.ForeignKey(Site3,on_delete=models.CASCADE)
	fuente_id = models.ForeignKey(Tipo_fuente_agua,on_delete=models.CASCADE)
	distancia = models.PositiveIntegerField(verbose_name='distancia')
	nombre = models.CharField(max_length=32,verbose_name='nombre')

class Objeto(models.Model):
	objeto_id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=32, verbose_name='Objeto')
	descripcion = models.CharField(max_length=32, verbose_name='Descripcion')
	sitio_id = models.ForeignKey(Site3, on_delete=models.CASCADE)
	subtipo_id = models.ForeignKey(Subtipo, on_delete=models.CASCADE)

	def __str__(self):
		return "{} ({})".format(self.nombre, self.sitio_id)

class Imagen_objeto(models.Model):
	imagen_id = models.ForeignKey(Imagenes,on_delete=models.CASCADE)
	objeto_id = models.ForeignKey(Objeto,on_delete=models.CASCADE)
