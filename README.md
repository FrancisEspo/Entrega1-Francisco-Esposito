# Proyecto_Coder

## Table of Contents
1. [General Info](#general-info)
2. [Models](#models)
3. [Technologies](#technologies)
4. [Functions](#functions)
### General Info
***
Trabajo práctico realizado para practicar las metodologias de desarrollo MVT y ABM en Base de Datos. 
La pagina web consiste en un Inicio el cual le permite buscar cursos registrados en la base de datos a partir del numero de la camada. Así mismo se posee un header para navegar en la distintas vistas para la creación de nuevos registros en los modelos.
### Screenshot
![Pagina de Inicio](https://github.com/FrancisEspo/Proyecto_Coder/blob/0cfb64725a11fe3b5536930dd9236c282fed80af/app_coder/static/app_coder/assets/img/Inicio.png)
## Models
***
Curso

    nombre = CharField(max_length=40)
    camada = IntegerField()

Estudiante

    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()

Profesor

    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    profesion = CharField(max_length=30)

## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org/): Version 3.10 
* [Django](https://www.djangoproject.com/): Version 4.0.5
* [SQLite](https://www.sqlite.org/index.html): Version 3.35.5
* [Bootstrap](https://getbootstrap.com/): Version 5.1.13

## Functions
***
La pagina web permite crear Cursos, Estudiantes y Profesores con sus respectivos campos y también la busqueda de cursos a partir del número especifico de la camada. Además cuenta con una barra de navegación en la parte superior de la pagina web para crear nuevos registros en sus respectivos modelos. 

### Buscador
http://127.0.0.1:8000/app_coder/

La primera funcionalidad que se puede observar es el buscador de cursos por camada, en el mismo es necesario ingresar el numero de camada y la pagina web arrojará todos los cursos registrados que tengan ese numero. 

### Profesores
http://127.0.0.1:8000/app_coder/profesores

Permite dar de alta nuevos profesores en la base de datos. 

### Cursos
http://127.0.0.1:8000/app_coder/cursos

Permite dar de alta nuevos cursos en la base de datos. 

### Estudiantes
http://127.0.0.1:8000/app_coder/estudiantes

Permite dar de alta nuevos estudiantes en la base de datos. 

