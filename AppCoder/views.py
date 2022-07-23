from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso    

# Create your views here.

def curso(self):
    curso= Curso (nombre="Django", comision=939393)
    curso.save()
    texto= f"Curso creado: {curso.nombre} {curso.comision}"
    return HTTPResponse (texto)

def inicio (request):
    return render (request, "AppCoder/inicio.html")

def cursos (request):
    return render (request, "AppCoder/cursos.html")

def profesores (request):
    return render (request, "AppCoder/profesores.html")
    
def estudiantes (request):
    return render (request, "AppCoder/estudiantes.html")

def cursoFormulario (request):
    return render (request, "AppCoder/cursoFormulario.html")
    

def entregables (request):
    return render (request, "AppCoder/entregables.html")