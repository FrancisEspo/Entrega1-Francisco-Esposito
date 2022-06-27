from django.urls import path
from app_coder import views

urlpatterns = [

    path('', views.inicio, name="inicio"),#esta era nuestra primer view
    path('cursos', views.Curso, name="Curso"),
    path('profesores', views.Profesor, name="Profesor"),
    path('estudiantes', views.Estudiante, name="Estudiante"),
    path('entregables', views.Entregable, name="Entregable"),
    path('curso_formulario', views.curso_formulario, name="CursoFormulario"),

]