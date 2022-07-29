from rest_framework import generics
from user.seralizers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
