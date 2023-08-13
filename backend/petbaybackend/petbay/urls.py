from django.urls import path
from .views import LoginUserAPIView

urlpatterns = [
    path('login/', LoginUserAPIView.as_view(), name='login-user'),
]
