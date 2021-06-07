from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app.models import Users
from app.serializers import UserCreateSerializer, UserListSerializer, UserUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Users.objects.all()
	serializer_class = UserCreateSerializer

	def list(self, request):
			permission_classes = (permissions.IsAuthenticated,)
			queryset = Users.objects.all()
			serializer = UserListSerializer(queryset, many=True)
			return Response(serializer.data)

	def retrieve(self, request, pk=None):
        	queryset = Users.objects.all()
        	user = get_object_or_404(queryset, pk=pk)
        	serializer = UserListSerializer(user)
        	return Response(serializer.data)

	def update(self, request, pk=None):
			queryset = Users.objects.all()
			user = get_object_or_404(queryset, pk=pk)
			serializer = UserUpdateSerializer(user, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
