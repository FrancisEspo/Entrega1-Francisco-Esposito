from django.contrib import admin
from .models import * #se importan todos los models  de la app_coder

# Register your models here.

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)