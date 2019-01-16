from django.contrib import admin
from .models import *

# Register your models here.

# Perzonalizacion exalumnos 
class ExalumnosAdmin(admin.ModelAdmin):
	list_filter = ["cedula"]
	
admin.site.register(Exalumnos,ExalumnosAdmin)	