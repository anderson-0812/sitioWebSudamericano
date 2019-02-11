from django.db import models

# Create your models here.

# OJO PARA CADA BUSQUEDA DE SACAR LOS PREREQUISITOS 
#ciclos
class ciclo(models.Model):
	"""docstring for ciclos"""
	CICLOS_CHOICE = (
			("Primer Ciclo","Primer Ciclo"),
			("Segundo Ciclo","Segundo Ciclo"),
			("Tercer Ciclo","Tercer Ciclo"),
			("Cuarto Ciclo","Cuarto Ciclo"),
			("Quinto Ciclo","Quinto Ciclo"),
			("Sexto Ciclo","Sexto Ciclo"),
			("Septimo Ciclo","Septimo Ciclo"),
			("Octavo Ciclo","Octavo Ciclo"),
			("Noveno Ciclo","Noveno Ciclo"),
			("Decimo Ciclo","Decimo Ciclo"),
		)

	nombre = models.CharField(max_length=255, choices = CICLOS_CHOICE, default = "Primer Ciclo")
	class Meta:
		verbose_name = "Ciclo"
		verbose_name_plural = "Ciclos"
		db_table = "ciclo"


	def __str__(self):
		return self.nombre

# Malla Academica
class malla(models.Model):
	nombre = models.CharField(max_length=255, blank = False)
	descripcion = models.CharField(max_length=255, blank =False)
	fecha_hora_creacion = models.DateTimeField(auto_now_add=True)
	
	ESTADO_CHOICE = (
			("Activo","1"),
			("Desactivado","0")
		)
	estado = models.CharField(max_length=1,choices = ESTADO_CHOICE, default= "Activo")

	#fecha_inicio = models.DateField(input_formats=settings.DATE_INPUT_FORMATS) #desde cuando se pone activa la malla 
	fecha_inicio = models.DateField(auto_now_add=True) #desde cuando se pone activa la malla 
	#fecha_fin = models.DateField(input_formats=settings.DATE_INPUT_FORMATS) # cuando culmina esta malla
	fecha_fin = models.DateField(auto_now_add=True) # cuando culmina esta malla
	nro_ciclos = models.CharField(max_length=2, blank = False)

	# controla que malla esla actual en caso de q haya una malla vigente antigua pero las nuevas matriculas sean de otra malla 
	MALLA_ACTIVA_CHOICES = (
			("Actual","1"),
			("Antigua","0")
		)
	malla_activa = models.CharField(max_length = 1, choices = MALLA_ACTIVA_CHOICES, default = "Actual")
	
	class Meta:
		verbose_name = "Malla"
		verbose_name_plural = "Mallas"
		db_table = "malla"

	def __str__(self):
		return self.nombre

# Materias 	para cada malla
class materia(models.Model):
	nombre_materia = models.CharField(max_length = 255)
	descripcion = models.CharField(max_length=255)
	# para saber si tiene que consultar en alsotras tablas a ver cadena de que materias es
	es_cadena = models.CharField(max_length=1, choices = (("Si","1"),("No","0")),default="Si")
	# para saber que matrias tienen q haber aprobado antes de poder tomar esta
	tiene_prerequisitos = models.CharField(max_length=1, choices = (("Si","1"),("No","0")),default="No")
	fecha_hora_creacion = models.DateTimeField(auto_now_add=True)
	fecha_hora_edicion = models.DateTimeField(auto_now_add=True)

	MATERIA_EXTRAORDINARIO_CHOICE = (
			("Si","1"),
			("No","0")
		)
	es_materia_periodo_extraordinario = models.CharField(max_length=1, choices = MATERIA_EXTRAORDINARIO_CHOICE, default = "No")

	class Meta:
		verbose_name = "Materia"
		verbose_name_plural = "Materias"
		db_table = "materia"

	def __str__(self):
		return self.nombre_materia

# relaciones
# Materia - Malla - Ciclo de donde consulto que materia esta en que mallas y es dada en que ciclos
class materia_malla_ciclo(models.Model):
	id_materia = models.ForeignKey(materia,on_delete = models.CASCADE, related_name='+') # related_name='+', => Django no cree una relación hacia atrás, establezca related_name en '+' o finalícelo con '+'.
	id_malla = models.ForeignKey(malla,on_delete = models.CASCADE, related_name='+')
	id_ciclo = models.ForeignKey(malla,on_delete = models.CASCADE, related_name='+')
	
	class Meta:
		verbose_name = "materia_malla_ciclo"
		verbose_name_plural = "materias_mallas_ciclos"
		db_table = "materia_malla_ciclo"

	def __str__(self):
		return self.id_materia

# aqui estaran solo registros de los prerequisitos de  las materias que para tomarlas tengan q tener aprobada una amteria previa
#ejemplo: Fundamentos de Base de datos 2 => tendra un registro en esta tabla que apunte a un id de la tabla materia_malla_ciclo
# que sacara los datos de la materia Fundamentos de base de datos 1 que no constara en esta tabla ya que es cadena pero no 
# necesita prerequisitos 
class materia_prerequisito(models.Model):
	id_materia = models.ForeignKey(materia,on_delete = models.CASCADE)
	id_materia_malla_ciclo_antecesora = models.ForeignKey(materia_malla_ciclo, on_delete = models.CASCADE)

	class Meta:
		verbose_name = "materia_prerequisito"
		verbose_name_plural = "materias_prerequisitos"
		db_table = "materia_prerequisito"
	def __str__(self):
		return self.id_materia