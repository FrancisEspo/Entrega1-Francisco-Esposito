from django.urls import path
from app_coder import views

urlpatterns = [

    path('', views.inicio, name="inicio"),#esta era nuestra primer view
    path('cursos', views.curso, name="Curso"),
    path('profesores', views.profesor, name="Profesor"),
    path('estudiantes', views.estudiante, name="Estudiante"),
    path('entregables', views.entregable, name="Entregable"),
    path('buscar/', views.buscar,)

]