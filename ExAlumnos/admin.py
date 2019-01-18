from django.contrib import admin
from .models import *

# Register your models here.

#creamos la clase que tendra la configuracion para concatenar los testimonios  vinculadas al ex alumno 
class TestimoniosInline(admin.StackedInline):
		model  = Testimonios
		extra = 1
		
# Perzonalizacion exalumnos 
class ExalumnosAdmin(admin.ModelAdmin):
	inlines =[TestimoniosInline]


		
	
admin.site.register(Exalumnos,ExalumnosAdmin)	