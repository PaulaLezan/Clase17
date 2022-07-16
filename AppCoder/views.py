from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso    

# Create your views here.

def curso(self):

    curso= Curso (nombre="Django", comision=939393)
    curso.save()
    texto= f"Curso creado: {curso.nombre} {curso.comision}"
    return HTTPResponse (texto)

