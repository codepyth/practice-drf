from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CustomUserCreateView.as_view(), name='register')
]