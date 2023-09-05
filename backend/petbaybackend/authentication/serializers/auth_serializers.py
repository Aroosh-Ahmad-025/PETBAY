from rest_framework import serializers

from authentication.models.auth_models import LoginUser, User


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ('username','password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password')