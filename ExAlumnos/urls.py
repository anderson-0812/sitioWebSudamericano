from django.urls import path
from ExAlumnos import views

urlpatterns = [
	path(r'',views.lista_testimonios, name = 'lista_testimonios'),
	path(r'inicio_exalumnos/',views.lista_testimonios, name = 'lista_testimonios'),
]