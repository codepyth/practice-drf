from rest_framework import serializers
from .models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES, default='customer')

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role']

    extra_kwargs = {
        'email': {'required': False},
        'first_name': {'required': False},
        'last_name': {'required': False},
    }
