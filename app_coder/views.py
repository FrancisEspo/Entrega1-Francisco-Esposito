from distutils.log import info
from django.shortcuts import render
from app_coder.forms import curso_formulario
from app_coder.models import Curso

# Create your views here.

def inicio(request):
    return render(request, 'app_coder/inicio.html')

def Curso(request):
    return render(request, 'app_coder/cursos.html')

def Entregable(request):
    return render(request, 'app_coder/entregables.html')

def Estudiante(request):
    return render(request, 'app_coder/estudiantes.html')

def Profesor(request):
    return render(request, 'app_coder/profesores.html')

def curso_formulario(request):
    
    if request.method == 'post':

        mi_formulario = curso_formulario(request.POST)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "app_coder/curso_formulario.html") #Volver a cargar formulario
    else:

        mi_formulario = curso_formulario() #Formulario vacio para construir el HTML

    return render(request, "app_coder/curso_formulario.html", {"mi_formulario":mi_formulario})