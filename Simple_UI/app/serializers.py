from app.models import Users
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		exclude = ('Contraseña',)
