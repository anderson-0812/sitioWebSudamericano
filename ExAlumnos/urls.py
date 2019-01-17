from django.urls import path
from ExAlumnos import views

urlpatterns = [
	path(r'',views.index, name = 'index'),
	path(r'index/',views.index, name = 'index'),
	path(r'testimonios_all/',views.testimonios_all, name = 'testimonios_all'),
]