from django.urls import path
from .views.pet_views import CREATEPETTYPEAPIVIEW,CREATEPETAPIVIEW

urlpatterns = [
    path('create_pet/', CREATEPETAPIVIEW.as_view(), name='create_pet'),
    path('create_pettype/', CREATEPETTYPEAPIVIEW.as_view(), name='create_pettype'),
]
