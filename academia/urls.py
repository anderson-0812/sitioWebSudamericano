from django.urls import path
from academia import views

from django.conf.urls import url

urlpatterns = [
	path(r'get_fechas_importantes_all/',views.get_fechas_importantes_all, name = 'get_fechas_importantes_all'),
	
]