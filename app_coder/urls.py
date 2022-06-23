from django.urls import path
from app_coder import views

urlpatterns = [

    path('', views.inicio),#esta era nuestra primer view
    path('cursos', views.Curso, name="Cursos"),
    path('profesores', views.Profesor),
    path('estudiantes', views.Estudiante),
    path('entregables', views.Entregable),

]