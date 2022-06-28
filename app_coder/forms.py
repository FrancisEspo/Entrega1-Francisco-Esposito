from django import forms

class curso_formulario(forms.Form):

    #Especificar los campos
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