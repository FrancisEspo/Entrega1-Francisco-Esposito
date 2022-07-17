from django.urls import path
from app_coder import views

urlpatterns = [

    path('', views.inicio, name="inicio"),#esta era nuestra primer view
    
    #Create
    path('cursos', views.curso, name="Curso"),
    path('profesores', views.profesor, name="Profesor"),
    path('estudiantes', views.estudiante, name="Estudiante"),
    
    path('buscar/', views.buscar,),

    #Lists
    path('curso_list', views.curso_list.as_view(), name='curso_list'),
    path('estudiante_list', views.estudiante_list.as_view(), name='estudiante_list'),
    path('profesor_list', views.profesor_list.as_view(), name='profesor_list'),

    #Details
    path(r'^curso/(?P<pk>\d+)$', views.curso_detail.as_view(), name="curso_detail"),
    path(r'^estudiante/(?P<pk>\d+)$', views.estudiante_detail.as_view(), name="estudiante_detail"),
    path(r'^profesor/(?P<pk>\d+)$', views.profesor_detail.as_view(), name="profesor_detail"),

    # Update
    path(r'^curso_update/(?P<pk>\d+)$', views.curso_update.as_view(), name='curso_update'),
    path(r'^estudiante_update/(?P<pk>\d+)$', views.estudiante_update.as_view(), name='estudiante_update'),
    path(r'^profesor_update/(?P<pk>\d+)$', views.profesor_update.as_view(), name='profesor_update'),
    
    #Delete
    path(r'^curso_delete/(?P<pk>\d+)$', views.curso_delete.as_view(), name='curso_delete'),
    path(r'^estudiante_delete/(?P<pk>\d+)$', views.estudiante_delete.as_view(), name='estudiante_delete'),
    path(r'^profesor_delete/(?P<pk>\d+)$', views.profesor_delete.as_view(), name='profesor_delete'),
]