from django.urls import path 
from .views import  curso, cursos, profesores, entregables, estudiantes, inicio




urlpatterns = [
       path('curso/', curso), 
       path('cursos/', cursos),
       path('profesores/', profesores), 
       path('estudiantes/', estudiantes), 
       path('entregables/', entregables), 
       path('', inicio), #que si no le pongo nada, que vaya a inicio



]