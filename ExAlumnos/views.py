from django.shortcuts import render, get_object_or_404 #render loq  te permite hacer una concatenacion 
	#entre el html con los datos ejemplo lista de clientes al html desde backend 

from django.contrib import messages # permite mandar mensajes desde el backend al front parael client
from .models import *
from django.template import loader # cargar los templates 
from django.http import HttpResponse, HttpResponseRedirect #responder al cluente, responder conuna redireccion
from django.db.models import Count
from django.http import JsonResponse # convertimos a formato json 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q # hacer operaciones con los modelos de mi db
from .forms import * #importar lso forms

#paginador 
from django.core.paginator import Paginator
from django.shortcuts import render




def index(request):
	exAlumnos = Exalumnos.objects.all()
	testimonios_list = Testimonios.objects.all()[:3]
	template = loader.get_template('ExAlumnos/inicio_exalumnos.html') #hacemos un metodo de carga del template
	context = {
		'testimonios_list': testimonios_list
	}
	return HttpResponse(template.render(context,request))
				#envio al template 		datos 	tipo de peticion  

#cargamos todos los testimonios para ser vistos 
def testimonios_all(request):

	#testimonios_all = Testimonios.objects.select_related('exalumnos');
	testimonios_all = Exalumnos.objects.all()
	template= loader.get_template('Testimonios/testimonios_all.html')

	paginator = Paginator(testimonios_all, 2) # Show 2 testimonios por pagina
	page = request.GET.get('page')
	testimonios_todos = paginator.get_page(page)

	context = {
		'testimonios_all': testimonios_todos
	}
	return HttpResponse(template.render(context,request))


# filtramoslos testimonios 
def testimonios_filter(request):
	buscar_testimonio = request.GET['buscar_testimonio'] #GET ES UN DICCIONARIO obyteemos el valor
	print(buscar_testimonio)

	testimonios_all = Exalumnos.objects.filter(nombres__icontains=buscar_testimonio)
	
		#testimonios_all = Testimonios.objects.select_related('exalumnos');
	#testimonios_all = Exalumnos.objects.all()
	template= loader.get_template('Testimonios/testimonios_all.html')

	paginator = Paginator(testimonios_all, 2) # Show 2 testimonios por pagina
	page = request.GET.get('page')
	testimonios_todos = paginator.get_page(page)

	context = {
		'testimonios_all': testimonios_todos
	}
	return HttpResponse(template.render(context,request))
