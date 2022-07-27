from re import template
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DeleteView, DetailView, UpdateView

from app_coder.models import Curso, Estudiante, Profesor

from .forms import curso_formulario, profesor_formulario, estudiante_formulario, UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    return render(request, 'app_coder/inicio.html')

#Buscador de cursos
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

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenna = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenna)

            if user is not None:
                login(request, user)
                return render(request, 'app_coder/inicio.html', {'mensaje':f'Bienvenid@ {usuario}'} )
            else:
                return render(request, 'app_coder/inicio.html', {'mensaje':f'Error! Datos incorrectos'} )
            
        else:
            return render(request, 'app_coder/inicio.html', {'mensaje':f'Error! Formulario erroneo'} )
    
    form = AuthenticationForm()

    return render(request, 'app_coder/login.html', {'form':form} )

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'app_coder/inicio.html', {'mensaje':'Usuario creado :)'} )

    else:
        form = UserRegisterForm()

    return render(request, 'app_coder/register.html', {'form':form})

#Creadores de registros

@login_required
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

@login_required
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

@login_required
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

#Lists

class curso_list(ListView):
    model = Curso
    template_name = "app_coder/lists/curso_list.html"

class estudiante_list(ListView):
    model = Estudiante
    template_name = "app_coder/lists/estudiante_list.html"

class profesor_list(ListView):
    model = Profesor
    template_name = "app_coder/lists/profesor_list.html"

#Details

class curso_detail(DetailView):
    model = Curso
    template_name = 'app_coder/details/curso_detail.html'

class estudiante_detail(DetailView):
    model = Estudiante
    template_name = 'app_coder/details/estudiante_detail.html'

class profesor_detail(DetailView):
    model = Profesor
    template_name = 'app_coder/details/profesor_detail.html'

#Updates

class curso_update(UpdateView):
    model =  Curso
    success_url = reverse_lazy('curso_list')
    fields = ['nombre', 'camada']

class estudiante_update(UpdateView):
    model =  Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido', 'email']

class profesor_update(UpdateView):
    model =  Profesor
    success_url = reverse_lazy('profesor_list')
    fields = ['nombre', 'apellido', 'email', 'profesion']

#Deleters

class curso_delete(DeleteView):
    model = Curso
    success_url = reverse_lazy('curso_list')

class estudiante_delete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')

class profesor_delete(DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesor_list')