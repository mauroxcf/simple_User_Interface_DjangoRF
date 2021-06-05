# Interfaz de Usuario en Django Rest Framework

el siguiente proyecto es una implementacion sencilla de una basedatos usuarios utilizando Json Web Tokens como autenticacion en la API, implementar un CRUD, se utilizando Viewsets, dando una explicacion en cada segmento del desarrollo de este proyecto.

### Requerimientos

- Ubuntu 16 en adelante
- Python 3 o cualquier version en adelante
- Django Rest Framework
- Mysql Client para la base de datos
- Entorno Virtual (opcional )para encapsular el proyecto

### Instalacion

1. Clonar repositorio
git clone https://github.com/mauroxcf/simple_User_Interface_DjangoRF.git
2. Instalar entorno virtual
Dentro del directorio del repositorio:
Pip install virtualenv --> instalar el entorno virtual en tu maquina
virtualenv venv --> crear entorno
source venv/bin/activate --> activar entorno virtual
pip freeze > requirements.txt --> crear el documento de requerimientos
pip install -r requirements.txt --> es recomendable ejecutar este comando para instalar todas las dependencias incluyendo django que se encuentran en el archivo requirements.txt de este repo.

## Ejecucion
1. hacer la migracion de la base de datos
python manage.py migrate
