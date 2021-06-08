from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app.models import Users
from app.serializers import UserCreateSerializer, UserListSerializer, UserUpdateSerializer
from django_filters import rest_framework as filters


class UsersFilter(filters.FilterSet):

    class Meta:
        model = Users
        fields = ['Nombre', 'Apellido', 'Cedula', 'Email']


class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Users.objects.all()
	serializer_class = UserListSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	search_fields = ['^Nombre', '^Apellido', '^Cedula', '^Email']
	ordering_fields = ['Apellido', 'idUser']
	ordering = ['idUser']
	filterset_class = UsersFilter

	def create(self, request):
			serializer = UserCreateSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
