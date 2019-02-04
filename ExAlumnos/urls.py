from django.urls import path
from ExAlumnos import views

from django.conf.urls import url

urlpatterns = [
	path(r'',views.index, name = 'index'),
	path(r'index/',views.index, name = 'index'),
	path(r'testimonios_all/',views.testimonios_all, name = 'testimonios_all'),
	path(r'testimonios_filter/',views.testimonios_filter, name = 'testimonios_filter'),
]