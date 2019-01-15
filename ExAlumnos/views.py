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

# Create your views here.
def index(request):
	return render(request,"ExAlumnos/inicio_exalumnos.html")

def lista_testimonios(request):
	testimonios_list = Testimonios.objects.all()
	template = loader.get_template('ExAlumnos/inicio_exalumnos.html') #hacemos un metodo de carga del template
	context = {
		'testimonios_list': testimonios_list
	}
	return HttpResponse(template.render(context,request)) 
				#envio al template 		datos 	tipo de peticion  