from django.urls import path 
from .views import  *



urlpatterns = [
       path('curso/', curso), 
       path('cursos/', cursos, name='cursos'),
       path('profesores/', profesores, name='profesores'), 
       path('estudiantes/', estudiantes,name='estudiantes'), 
       path('entregables/', entregables, name='entregables'), 
       path('', inicio, name='inicio'), #que si no le pongo nada, que vaya a inicio
       path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
       

]