from django.db import models


class Users(models.Model):
	"""Modelo de la tabla de usuarios.
	contiene campos de datos personales de la
	persona registrada.

	Args:
		models ([model]): [modela la tabla db]
	"""

	CHOICES = ( ('EPS', 'EPS'),
            ('IPS', 'IPS'),
            ('ARL', 'ARL'),
    )
	idUser = models.AutoField(primary_key=True)
	Nombre = models.CharField(max_length=45)
	Apellido = models.CharField(max_length=45)
	Email = models.EmailField(max_length=60, unique=True)
	Cedula = models.IntegerField()
	Imagen_de_Perfil = models.FileField(upload_to='imagenes/', null=True, blank=True)
	Pais = models.CharField(max_length=45)
	Entidad = models.CharField(max_length=45, choices=CHOICES)
	Contraseña = models.CharField(max_length=16)
