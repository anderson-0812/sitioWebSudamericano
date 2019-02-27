from django.shortcuts import render

#paginador 
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *# siempr importar los modelos
from django.template import loader # cargar los templates 
from django.http import HttpResponse, HttpResponseRedirect #responder al cluente, responder conuna redireccion



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