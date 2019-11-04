<p align="center">
<img src="https://www.python.org/static/img/python-logo.png">

</p>
<p align="center"><img src="https://static.djangoproject.com/img/logos/django-logo-positive.png" width="500px"></p>
<p align="center"><img src="https://www.ucundinamarca.edu.co/images/iconos/escudo-inferior-optimizado.png"></p>

<p align="center">

> **Note:** The **Publish now** button is disabled if your file has not been published yet.
</p>

# Siaa

Asignación de horarios Mediante AG - Algoritmos genéticos

### Requerimientos

* Python >= 3.7.*
* Django >= 2.*
* <a href="https://www.django-rest-framework.org/#installation">django RestFramework</a>
* <a href="https://github.com/davesque/django-rest-framework-simplejwt">django RestFramework - simplejwt</a>


### Instalación

El proyecto esta Python mediante el framework Django en [Django 2.2.4](https://docs.djangoproject.com/en/2.2)

```sh
"Los puntos con simbolo ($) son comandos desde consola
 ubicado en la ruta del proyecto"
 
1- Clonar proyecto desde GitKraken

2- Inicializar GifFlow y hacer Pull con la rama develop
   (rama la cual se trabajara en el proyecto)
   
3. $ composer install  

4- Copiar el archivo .env.example 
   (.env - copia.example) y cambiar el nombre a .env 
   
5- Dejar la configuracion DB de developer
   y del modulo asignado (Eliminar los demas modulos) ejemplo
   
    DB_CONNECTION=pgsql
    DB_HOST=postgres
    DB_PORT=5432
    DB_DATABASE=developer
    DB_USERNAME=default
    DB_PASSWORD=secret

6- $ php artisan passport:install
7- $ php artisan passport:keys
8- $ php artisan key:generate
9- $ php artisan storage:link
10- $ php artisan migrate --path=/database/migrations/[name] --database=pgsql
```
