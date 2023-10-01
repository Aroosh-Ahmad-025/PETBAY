from django.urls import path
from .views.pet_views import *

urlpatterns = [
    path("create_pet",create_pet,name="create_pet")
]