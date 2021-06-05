from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from app.models import Users
from app.serializers import UserCreateSerializer, UserListSerializer


class UserViewSet(ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserCreateSerializer

	def list(self, request):
			queryset = Users.objects.all()
			serializer = UserListSerializer(queryset, many=True)
			return Response(serializer.data)
