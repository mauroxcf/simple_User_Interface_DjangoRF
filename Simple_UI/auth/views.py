from app.models import Users
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
