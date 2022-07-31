from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .models import Curso, Estudiante, Profesor   
from AppCoder.forms import CursoForm, ProfeForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

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

    if request.method == "POST":

        form= ProfeForm(request.POST) #VIENEN LOS DATOS DE UNA CLASE FORMULARIO
        print(form)

        if form.is_valid(): #si pasa la validacion de Django
            info=form.cleaned_data    #traigo a una variable info, la info del formulario (limpiame los datos y guardalos aca)
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profesor.save()
            return render (request, "AppCoder/inicio.html")

    else: 
        form= ProfeForm() #creo el formulario vacio   
    return render (request, "AppCoder/profeForm.html", {"formulario":form}) #traigo el cursoform, lo renderiso y lo mando por diccionario
            #si va por get, le muestra un form vacio y lo llena, cuando lo llena, vuelve a entrar pero por POST. 

def busquedaComision (request):
     return render (request, "AppCoder/busquedacomision.html")

def buscar (request):
    if request.GET ["comision"]:   #si tengo algo en comision
        comi= request.GET ["comision"] #que me la traiga
        cursos= Curso.objects.filter(comision= comi) #del models Curso, traeme todo los objetos (de curso) que cumplan esa condicion y lo incluye en una lista
        return render (request, 'AppCoder/inicio.html', {"cursos":cursos, "comision": comi})
        
    else: 
        return render(request, 'AppCoder/busquedaComision.html', {"error":"No se ingreso ninguna comision"})


def leerprofesores(request): 
    profesores =Profesor.objects.all()
    return render (request, "AppCoder/leerprofesores.html", {"profesores":profesores})
    
def eliminarProfesor(request, nombre_profesor):
    profe=Profesor.objects.get(nombre= nombre_profesor)
    profe.delete()
    profesores =Profesor.objects.all()
    return render (request, "AppCoder/leerprofesores.html", {"profesores":profesores})

def editarProfesor (request, nombre_profesor):
    profe=Profesor.objects.get(nombre= nombre_profesor)     

    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form. is_valid ():
            info=form.cleaned_data    #traigo a una variable info, la info del formulario (limpiame los datos y guardalos aca)
            profe.nombre= info["nombre"] #al dato que me trae de la base, le agrego el dato se que modifica y lo guardo.
            profe.apellido= info["apellido"]
            profe.email= info["email"]
            profe.profesion= info["profesion"]
            profe.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= ProfeForm (initial={"nombre":profe.nombre, "apellido": profe.apellido, "email":profe.email, "profesion": profe.profesion})
    return render (request, 'AppCoder/editarProfesor.html', {"formulario":form, "nombre_profesor":nombre_profesor}) 


#vistas basadas en clases
class EstudianteList(ListView):
    model= Estudiante
    template_name= "AppCoder/estudiantes_list.html"

class EstudianteDetalle(DetailView):
    model= Estudiante
    template_name= "AppCoder/estudiantes_detail.html"






"""respuesta= "\n No enviaste Datos"
        return HttpResponse(respuesta)"""
""" return render(request, 'AppCoder/busquedaComision.html', {"error":"No se ingreso ninguna comision"})"""

"""#si tengo algo en comision  me va a buscar en la url que contenga comision, porque viene por GET. #que me la traiga"""

""" if request.GET ("comision"):   #si tengo algo en comision
        comi= request.GET ("comision") #que me la traiga
        cursos= Curso.objects.filter(comision= comi) #del models Curso, traeme todo los objetos (de curso) que cumplan esa condicion y lo incluye en una lista
        return render (request, 'AppCoder/resultadosBusqueda.html', {"cursos":curso})
        
 else: 
        return (request, 'AppCoder/busquedaComision.html', {"error":"No se ingreso ninguna comision"})"""
  



"""def cursoFormulario (request):

    if (request.method == "POST"):
        nombre= request.POST.get("curso")
        comision=request.POST.get("comision")
        curso= Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "AppCoder/inicio.html")





    return render (request, "AppCoder/cursoFormulario.html")""" #Vista para formulario HTML