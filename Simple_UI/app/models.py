from django.db import models

# Create your models here.
class Users(models.Model):
    CHOICES = (
        ('EPS', 'EPS'),
        ('IPS', 'IPS'),
        ('ARL', 'ARL'),
    )
	idUser = models.IntegerField(primary_key=True)
	Nombre = models.CharField(max_length=45)
	Apellido = models.CharField(max_length=45)
	Email = models.EmailField(max_length=60, unique=true)
	Cedula = models.IntegerField
	Imagen_de_Perfil = models.ImageField(use_url='User Pic')
	Pais = models.CharField(max_length=45)
	Entidad = models.CharField(max_length=45, choices=CHOICES)
	Contraseña = models.CharField(max_length=16, min_length=4, allow_blank=False)
