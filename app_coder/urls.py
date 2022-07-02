from django.urls import path
from app_coder import views

urlpatterns = [

    path('', views.inicio, name="inicio"),#esta era nuestra primer view
    path('cursos', views.curso, name="Curso"),
    path('profesores', views.profesor, name="Profesor"),
    path('estudiantes', views.estudiante, name="Estudiante"),
    path('buscar/', views.buscar,),

    path('leer_profesores', views.get_profesor, name='get_profesor'),
    path('leer_estudiantes', views.get_estudiante, name='get_estudiante'),
    path('leer_cursos', views.get_curso, name='get_curso'),

]