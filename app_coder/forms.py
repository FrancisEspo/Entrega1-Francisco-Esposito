from django import forms
from dataclasses import field

from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User

class curso_formulario(forms.Form):
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class estudiante_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', min_length=5, max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Reingrese la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}