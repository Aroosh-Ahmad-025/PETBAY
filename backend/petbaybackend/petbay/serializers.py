from rest_framework import serializers
from .models import User,LoginUser

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ('username','password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password')