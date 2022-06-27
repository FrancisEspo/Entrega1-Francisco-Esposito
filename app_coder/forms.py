from django import forms

class curso_formulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class profesor_formulario(forms.Form):
    mombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)