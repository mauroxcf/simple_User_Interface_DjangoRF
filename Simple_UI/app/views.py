from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from authentication.models import User
from app.serializers import UserListSerializer, UserUpdateSerializer
from django_filters import rest_framework as filters


class UsersFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'cedula', 'email']


class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserListSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	search_fields = ['^nombre', '^apellido', '^cedula', '^email']
	ordering_fields = ['apellido', 'id']
	ordering = ['id']
	filterset_class = UsersFilter


	def retrieve(self, request, pk=None):
			queryset = User.objects.all()
			user = get_object_or_404(queryset, pk=pk)
			serializer = UserListSerializer(user)
			return Response(serializer.data)

	def update(self, request, pk=None):
			queryset = User.objects.all()
			user = get_object_or_404(queryset, pk=pk)
			serializer = UserUpdateSerializer(user, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
