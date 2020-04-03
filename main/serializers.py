from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['display_name', 'email', 'gender']
