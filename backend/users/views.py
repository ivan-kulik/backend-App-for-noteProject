from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
