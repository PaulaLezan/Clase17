from django.urls import path 
from .views import  curso, cursos, profesores, entregables, estudiantes, inicio




urlpatterns = [
       path('curso/', curso), 
       path('cursos/', cursos),
       path('curso/', profesores), 
       path('curso/', estudiantes), 
       path('curso/', entregables), 
       path('', inicio), #que si no le pongo nada, que vaya a inicio



],