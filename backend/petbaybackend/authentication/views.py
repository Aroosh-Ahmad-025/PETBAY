from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User

class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Get username and password from the request data
        username = request.data.get('email')
        password = request.data.get('password')

        # Query the LoginUser model to check if a matching user exists
        user = authenticate(username=username, password=password)

        if user:

            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return JsonResponse({"status": "NotFound","message":"User Not Found"})
