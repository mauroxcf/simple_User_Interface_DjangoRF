from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Users
from app.serializers import UserCreateSerializer, UserListSerializer, UserUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserCreateSerializer

	def list(self, request):
			queryset = Users.objects.all()
			serializer = UserListSerializer(queryset, many=True)
			return Response(serializer.data)

	# estas funciones comentadas son para revision
	""" def update(self, request, pk=None):
			user_obj = Users.objects.get(pk=pk)
			serializer = UserUpdateSerializer(user_obj, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
	""" def update(self, request, *args, **kwargs):
			partial = True # Here I change partial to True
			instance = self.get_object()
			serializer =  UserUpdateSerializer(instance, data=request.data, partial=partial)
			serializer.is_valid(raise_exception=True)
			self.perform_update(serializer)

			return Response(serializer.data) """

