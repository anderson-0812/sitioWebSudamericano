from django.urls import path
from academia import views

from django.conf.urls import url

urlpatterns = [
	path(r'get_fechas_importantes_all/',views.get_fechas_importantes_all, name = 'get_fechas_importantes_all'),
	#path(r'get_fecha_importante/<int:id_fecha_importante>',views.get_fecha_importante, name = 'get_fecha_importante'),
	path(r'get_fecha_importante/',views.get_fecha_importante, name = 'get_fecha_importante'),
	path(r'get_malla_actual/',views.get_malla_actual, name = 'get_malla_actual'),
	path(r'get_malla/',views.get_malla, name = 'get_malla'),
	path(r'get_info_malla_by_ciclo/<int:mallaid>',views.get_info_malla_by_ciclo, name = 'get_info_malla_by_ciclo'),
	
]