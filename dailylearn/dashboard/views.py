from rest_framework import generics
from .models import ImageModel
from .serializers import ImageSerializer


class ImageCreateAPIView(generics.CreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
