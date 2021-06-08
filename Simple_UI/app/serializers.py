from authentication.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
	"""
		Esta clase combierte el objeto usuario listado en un JSON
	"""
	class Meta:
		model = User
		# fields = '__all__'
		exclude = ('is_verified', 'is_staff', 'is_active',
             'created_at', 'updated_at', 'groups', 'user_permissions', 'last_login', 'password', 'is_superuser')
		# exclude = ('contraseña',)

class UserUpdateSerializer(serializers.ModelSerializer):
	"""
		Esta clase combierte el objeto usuario listado para uso del metodo PUT en un JSON
	"""
	password = serializers.CharField( max_length=68, min_length=6, write_only=True)

	class Meta:
		model = User
		exclude = ('email', 'cedula', 'is_verified', 'is_staff', 'is_active',
             'created_at', 'updated_at', 'groups', 'user_permissions', 'last_login', 'is_superuser')
