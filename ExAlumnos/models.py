from django.db import models

# Create your models here.
class Exalumnos(models.Model):
	id_exalumno = models.AutoField(primary_key=True)

	#cedula = models.CharField(max_length = 10, unique = True)
	nombres = models.CharField(max_length=100,blank=False)
	apellidos = models.CharField(max_length=100,blank=False)
	#telefono = models.IntegerField()
	#direccion = models.CharField(max_length=200,blank=False)
	#ciudad = models.CharField(max_length=100,blank=False)
	#SEX0_CHOICES = (
	#		("M","Mujer"),
	#		("H","Hombre")
	#	)
	#sexo = models.CharField(max_length=1, choices = SEX0_CHOICES, default = "H")

	# cuando presenta  al usuario le va  amostrar estas referencias de los nombres
	class Meta:
		verbose_name = "Exalumnos"
		verbose_name_plural = "Exalumnos"
		db_table = "exalumnos"


	def __str__(self):
		return self

class Testimonios(models.Model):
	"""docstring for testimonios"""
	id_testimonio = models.AutoField(primary_key = True)

	# DE esta manera creo relacion de quemuchos testimonios hacen referencia a un alumno relacion de 1 a muchos
	id_exalumno = models.ForeignKey(Exalumnos,on_delete = models.CASCADE)
	testimonio = models.TextField();
	video = models.CharField(max_length=255,blank =False)

	class Meta:
		verbose_name = "Testimonio"
		verbose_name_plural = "testimonios"
		db_table = "testimonios"

	def __str__(self):
		return self
