# Interfaz de Usuario en Django Rest Framework

el siguiente proyecto es una implementacion sencilla de una basedatos usuarios utilizando Json Web Tokens como autenticacion en la API, implementar un CRUD, se utilizando Viewsets, dando una explicacion en cada segmento del desarrollo de este proyecto.

### Requerimientos

- Ubuntu 16 en adelante
- Python 3.6
- Django Rest Framework
- Mysql Client para la base de datos
- Entorno Virtual (opcional )para encapsular el proyecto

### Instalacion

1. Clonar repositorio
```
git clone https://github.com/mauroxcf/simple_User_Interface_DjangoRF.git
```
2. Crear entorno virtual
Dentro de la carpeta raiz directorio del repositorio:
```
Pip install virtualenv 
virtualenv venv --> crear entorno
source venv/bin/activate --> activar entorno virtual
pip install -r requirements.txt --> Instala todas las depencencias
```
3. Hacer la migracion de la base de datos
```
python manage.py makemigrations
python manage.py migrate
```
4. Activar el Servidor
```
python manage.py runserver
```
Al haber realizado con exito la instalacion de todas las depencias, y correr la aplicacion, ya es posible de acceder a los endpoints que se manejan en el servidor, hacer un CRUD con los usuarios creamos llevado de la mano por un sistema de autenticacion por JWT que sera porporcionado al momento de logearse en el endpoint correspondiente.

NOTA: el proyecto esta configurado para el gestor de base de datos mysql, si se desea hacer cambios, favor de hacer los cambios respectivos en el archivo settings.py ubicado en el directorio 'Simple_UI' en la seccion de DATABASES.

### Funcionamiento

la app consta de una serie de endpoints para poder manipular la base de datos, obtener informacion, etc. siempre y cuando el usuario se encuentre registrado y tengo un token de acceso para acceder a los metodos que se pueden utilizar.
​
| HTTP Method | Endpoint | Descripcion |
| ------ | ------ | ------ |
| GET | /api/v1/ | retorna el estado si funciona la API. |
| POST | /auth/register/ | Crea un usuario nuevo con las especificaciones con derechos de autenticacion. |
| POST | /auth/login/ | Se logea el usuario con permisos de autenticacion y su token. |
| GET | /api/v1/users/ | Accedemos a todos los usuarios registrado. |
| GET | /api/v1/users/[id] | retorna un usuario en especifico por ID. |
| PUT | /api/v1/users/[id] | Actualiza los datos de un usuario ya registrado. |
​

- Se puede hacer pruebas correspondientes con POSTMAN o SWAGGER agregando usuarios con los campos requeridos, hacer consultas sencillas, etc.
![image](https://user-images.githubusercontent.com/66022141/121136872-bc9c2300-c7fb-11eb-80f2-94c5bf07c027.png)

### Estructura del proyecto
![image](https://user-images.githubusercontent.com/66022141/121137478-4946e100-c7fc-11eb-9130-ff0098450aec.png)

La estructura del proyecto consta de tres modulos principales que son app, authentication, Simple_UI.
- app:Es el modulo principal que entrega las respuestas en formato JSON a cada verbo HTTP que se le realiza al servidor dependiendo del endpoint en donde se le solicite, los archivos principales son serializaers.py, views.py, urls.py.
- authentication:Se encarga del manejo de permisos de usuario, para manejo de usuario con facultad de administrador, login y registro segun los campos requeridos establecidos para ello. Sus archivos principales son views.py, models.py, serializers.py
- Simple_UI: Se encarga de la configuracion del proyecto, dependencias instaladas, endpoints, y otras configuraciones.

## Autors ✒️
Mauricio Contreras - [Github :octocat:](https://github.com/mauroxcf) - [Twitter](https://twitter.com/MauroJCF) - [Linkedin](https://www.linkedin.com/in/mauricio-contrerasf/)
