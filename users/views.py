from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer






class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
