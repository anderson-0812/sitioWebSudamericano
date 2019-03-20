from django.shortcuts import render

#paginador 
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *# siempr importar los modelos
from django.template import loader # cargar los templates 
from django.http import HttpResponse, HttpResponseRedirect #responder al cluente, responder conuna redireccion


def index(request):
	return render(request,"")

def get_fechas_importantes_all(request):
	fechas_importantes_all = fecha_academica_importante.objects.all();
	template = loader.get_template('academia/list_fechas_importantes.html')

	# valido el query
	fechas_importantes_todos = True
	if(fechas_importantes_all.count() > 0):

		paginator = Paginator(fechas_importantes_all, 2) # Show 2 fechas importantes por pagina
		page = request.GET.get('page')
		fechas_importantes_todos = paginator.get_page(page)
	else:
		fechas_importantes_todos = False

	context = {
		'fechas_importantes_all': fechas_importantes_todos
	}
	return HttpResponse(template.render(context,request))


# mostrar fechaimportante csegun id 
def get_fecha_importante(request):
	id_fecha_importante = request.GET['fechaid'];
	fecha_importante = fecha_academica_importante.objects.get(id = id_fecha_importante)
	template = loader.get_template("academia/fecha_importante_view.html") # es un directoriod e template
	context = {
		'fecha_importante':fecha_importante,
	}

	return HttpResponse(template.render(context,request))


# MALLA CURRICULAR
def get_malla_actual(request):
	malla_actual = malla.objects.filter(isMallaActiva = True);
	template = loader.get_template("academia/malla/malla_main.html");
	context = {
		'malla_actual':malla_actual,
	}

	return HttpResponse(template.render(context,request))

def get_malla(request):
	mallaid = request.GET['mallaid'] 
	malla_actual = malla.objects.get(id = mallaid)
	template = loader.get_template("academia/malla/malla_details.html")
	context = {
		'malla_actual':malla_actual,
	}

	return HttpResponse(template.render(context,request))