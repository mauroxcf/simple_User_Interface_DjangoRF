from authentication.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		# fields = '__all__'
		exclude = ('is_verified', 'is_staff', 'is_active',
             'created_at', 'updated_at', 'groups', 'user_permissions', 'last_login', 'password', 'is_superuser')
		# exclude = ('contraseña',)

class UserUpdateSerializer(serializers.ModelSerializer):
	password = serializers.CharField( max_length=68, min_length=6, write_only=True)

	class Meta:
		model = User
		exclude = ('email', 'cedula', 'is_verified', 'is_staff', 'is_active',
             'created_at', 'updated_at', 'groups', 'user_permissions', 'last_login', 'is_superuser')
