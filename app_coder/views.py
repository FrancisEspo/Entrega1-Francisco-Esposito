from distutils.log import info
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app_coder.models import Curso, Estudiante, Profesor

from .forms import curso_formulario, profesor_formulario, estudiante_formulario

# Create your views here.

def inicio(request):
    return render(request, 'app_coder/inicio.html')

def curso(request):
    if request.method == 'POST':

        mi_formulario = curso_formulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            curso = Curso(
                nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            # Volver a cargar formulario
            return render(request, "app_coder/inicio.html")
    else:

        mi_formulario = curso_formulario()  # Formulario vacio para construir el HTML

    return render(request, "app_coder/cursos.html", {"mi_formulario": mi_formulario})

def estudiante(request):
    if request.method == 'POST':

        mi_formulario = estudiante_formulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            estudiante = Estudiante(
                nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])

            estudiante.save()

            # Volver a cargar formulario
            return render(request, "app_coder/inicio.html")
    else:

        # Formulario vacio para construir el HTML
        mi_formulario = estudiante_formulario()

    return render(request, "app_coder/estudiantes.html", {"mi_formulario": mi_formulario})

def profesor(request):
    if request.method == 'POST':

        mi_formulario = profesor_formulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                email=informacion['email'], profesion=informacion['profesion'])

            profesor.save()

            # Volver a cargar formulario
            return render(request, "app_coder/inicio.html")
    else:

        mi_formulario = profesor_formulario()  # Formulario vacio para construir el HTML

    return render(request, "app_coder/profesores.html", {"mi_formulario": mi_formulario})

def buscar(request):
    if request.GET['camada']:

        camada = request.GET['camada']
        print(camada)
        cursos = Curso.objects.filter(camada__icontains=camada)
        print(cursos)
        return render(request, 'app_coder/inicio.html', {'cursos':cursos, 'camada':camada})
    
    else:
        respuesta = "No hay datos ingresados"
    
    return render(request, 'app_coder/inicio.html', {'respuesta':respuesta})

def get_profesor(request):
    profesores = Profesor.objects.all() 

    contexto = {'profesores': profesores}

    return render(request, 'app_coder\getters\get_profesor.html', contexto)

def get_estudiante(request):
    estudiantes = Estudiante.objects.all() 

    contexto = {'estudiantes': estudiantes}

    return render(request, 'app_coder\getters\get_estudiante.html', contexto)

def get_curso(request):
    cursos = Curso.objects.all() 

    contexto = {'cursos': cursos}

    return render(request, 'app_coder\getters\get_curso.html', contexto)