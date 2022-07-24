from http.client import HTTPResponse
import re
from django.shortcuts import render
from AppCoder.models import Curso, Profesor   
from AppCoder.forms import CursoForm, ProfeForm


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

def entregables (request):
    return render (request, "AppCoder/entregables.html")

def cursoFormulario (request):

    if (request.method == "POST"):

        form= CursoForm(request.POST) #VIENEN LOS DATOS DE UNA CLASE FORMULARIO
        print(form)

        if form.is_valid(): #si pasa la validacion de Django
            info=form.cleaned_data    #traigo a una variable info, la info del formulario (limpiame los datos y guardalos aca)
            print(info)
            nombre= info["nombre"]
            comision= info["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save () # los ultimos cuatro son los mismo que en html, solo que los sacamos de un form
            return render (request, "AppCoder/inicio.html")
    else: 
        form= CursoForm() #creo el formulario vacio   
    return render (request, "AppCoder/cursoFormulario.html", {"formulario":form}) #traigo el cursoform, lo renderiso y lo mando por diccionario
            #si va por get, le muestra un form vacio y lo llena, cuando lo llena, vuelve a entrar pero por POST. 

def profeFormulario (request):

    if (request.method == "POST"):

        form= ProfeForm(request.POST) #VIENEN LOS DATOS DE UNA CLASE FORMULARIO
        print(form)

        if form.is_valid(): #si pasa la validacion de Django
            info=form.cleaned_data    #traigo a una variable info, la info del formulario (limpiame los datos y guardalos aca)
            print(info)
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "AppCoder/inicio.html")

    else: 
        form= ProfeForm() #creo el formulario vacio   
    return render (request, "AppCoder/profeForm.html", {"formulario":form}) #traigo el cursoform, lo renderiso y lo mando por diccionario
            #si va por get, le muestra un form vacio y lo llena, cuando lo llena, vuelve a entrar pero por POST. 


    


"""def cursoFormulario (request):

    if (request.method == "POST"):
        nombre= request.POST.get("curso")
        comision=request.POST.get("comision")
        curso= Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "AppCoder/inicio.html")





    return render (request, "AppCoder/cursoFormulario.html")""" #Vista para formulario HTML