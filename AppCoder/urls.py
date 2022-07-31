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
       path('profeFormulario/', profeFormulario, name='profeFormulario'),
       path ('busquedaComision/', busquedaComision, name='busquedaComision'), 
       path ('buscar/', buscar, name= 'buscar'), 
       path('leerProfesores/', leerprofesores, name='leerprofesores' ),
       path('eliminarProfesor/<nombre_profesor>', eliminarProfesor, name='eliminarProfesor' ),
       path('editarProfesor/<nombre_profesor>', editarProfesor, name='editarProfesor' ),
       #------------------------------------------------
       path('estudiante/list/', EstudianteList.as_view(), name='estudiante_listar'),
       path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
       path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
       path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name='estudiante_editar'),
       path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name='estudiante_borrar'),
]