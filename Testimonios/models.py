from django.db import models



#creamos la clase que tendra la configuracion para concatenar los testimonios  vinculadas al ex alumno 
class TestimoniosInline(admin.StackedInline):
		model  = Testimonios
		extra = 1
		
# Create your models here.
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
