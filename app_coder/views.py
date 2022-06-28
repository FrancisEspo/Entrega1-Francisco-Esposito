from distutils.log import info
import email
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app_coder.models import Curso, Entregable, Estudiante, Profesor

from .forms import curso_formulario, profesor_formulario, entregable_formulario, estudiante_formulario

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


def entregable(request):
    if request.method == 'POST':

        mi_formulario = entregable_formulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            print(informacion)

            entregable = Entregable(
                nombre=informacion['nombre'], fecha_de_entrega=informacion['fecha_de_entrega'], entregado=['entregado'])

            entregable.save()

            # Volver a cargar formulario
            return render(request, "app_coder/inicio.html")
    else:

        # Formulario vacio para construir el HTML
        mi_formulario = entregable_formulario()

    return render(request, "app_coder/entregables.html", {"mi_formulario": mi_formulario})


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
