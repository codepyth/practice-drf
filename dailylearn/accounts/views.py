from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import CustomUserCreateSerializer


# Create your views here.


class CustomUserCreateView(generics.CreateAPIView):
    # authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = CustomUserCreateSerializer
