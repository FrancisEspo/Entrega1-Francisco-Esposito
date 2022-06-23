from django.shortcuts import render
from django.http import HttpResponse
from app_coder.models import Curso
from django.template import loader

# Create your views here.
def curso(self):
    curso = Curso(nombre = "django", camada = "1345")
    curso.save()

    documento = f"El curso es: {curso.nombre}, de la camada: {curso.camada}"

    return HttpResponse(documento)