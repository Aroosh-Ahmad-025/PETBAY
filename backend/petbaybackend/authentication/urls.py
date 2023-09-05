from django.urls import path
from authentication.views import LoginUserAPIView

urlpatterns = [
    path('login/', LoginUserAPIView.as_view(), name='login-user'),
]