from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .models import User
from .responses import HttpRespEnum


class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Get username and password from the request data
        username = request.data.get('email')
        password = request.data.get('password')

        # Query the LoginUser model to check if a matching user exists
        try:
            user = User.objects.get(email=username, password=password)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user:
            return JsonResponse({"status":HttpRespEnum.OK.name,"message":"User Found"})
        else:
            return JsonResponse({"status": HttpRespEnum.NOT_FOUND.name,"message":"User Not Found"})
