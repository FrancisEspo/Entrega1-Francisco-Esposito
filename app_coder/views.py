from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
#from app_coder.models import Curso, Profesor, Estudiante, Entregable
from django.template import loader

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