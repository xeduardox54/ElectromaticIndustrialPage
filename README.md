# ElectromaticIndustrialPage
## Table of Contents
1. [Información general](#informacion-general)
2. [Technologies](#tecnologias)
3. [Installation](#instalacion)
4. [Preguntas](#preguntas)
5. [Información de contacto](#informacion-contacto)
<a name="general-info"></a>
### Información general
***
Este proyecto consta del desarrollo de una página web con capacidades de administración y con enfoque informativo sobre grupos electrógenos, cuya propiedad le pertenece a la empresa Electromatic Industrial S.R.L. El estado de este proyecto es finalizado.
<a name="tecnologias"></a>
## Tecnologías
***
* [Python](https://www.python.org): Versión 3.8.3
* [Framework Django](https://www.djangoproject.com): Versión 3.1.6
* [Base de datos PostgreSQL](https://www.postgresql.org): Version 10.15
* [asgiref]: Versión 3.3.1
* [gunicorn]: Versión 20.0.4
* [Pillow]: Versión 8.1.0
* [psycopg2]: Versión 2.8.6
* [pytz]: Versión 2021.1
* [sqlparse]: Versión 0.4.1

<a name="instalacion"></a>
## Instalación
***
Estos son los pasos para instalar este proyecto con Django:
```
Primero se debe crear un entorno virtual y activarlo. Puede ver como se hace con el siguiente link: https://docs.python.org/es/3/tutorial/venv.html
$ git clone https://github.com/xeduardox54/ElectromaticIndustrialPage.git
$ cd ElectromaticIndustrialPage
$ pip install -r requirements.txt
$ python manage.py makemigrations servicios
$ python manage.py migrate
$ python manage.py createsuperuser (Creamos el usuario administrador para el sitio web)
$ python manage.py runserver
```
Información adicional: Usted puede utilizar la base de datos SQLite 3 que Django crea por defecto o utilizar una base de datos PostgreSQL. En caso de utilizar la segunda, luego de clonar el proyecto ingrese a la carpeta "ElectromaticIndustrialPage" 2 veces, abra el archivo "settings.py" y cambié allí el uso de la base de datos por defecto a la configuración que está allí para PostgreSQL; la cuenta y contraseña de esta base de datos ya están por colocadas, por lo que debe cambiarlas a las credenciales de la base de datos PostgreSQL vaya a utilizar para el proyecto.
<a name="preguntas"></a>
## Preguntas
***
1. **¿Por qué no me salen imágenes o contenido cuando inicio el proyecto en el navegador?**
Primero debe de insertar las imágenes y el contenido desde el panel de administrador del sitio web, donde la primera vez tendrá que crear un objeto y llenarlo con la información e imágenes que se requieran; la segunda vez solo tendrá que editar las características de dicho objeto. Si crea más de un objeto, se tomará en cuenta el último que haya agregado siempre.
2. **¿Como ingreso al administrador del sitio web?**
Para ingresar, debe colocar "/admin" al final de la IP o dominio en la URL del sitio web desde el que esté accediendo al proyecto. Ejemplo: https://"IP o Dominio"/admin

<a name="informacion-contacto"></a>
## Información de contacto
* Nombre: Eduardo Rodríguez
* Correo: xeduardox54@hotmail.com
* Número: 983848610
