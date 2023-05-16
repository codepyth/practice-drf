from django.urls import path
from . import views


urlpatterns = [
    path('upload-image/', views.ImageCreateAPIView.as_view(), name='upload-image')
]