from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.pet_models import Pet
from rest_framework.decorators import api_view

# @login_required
@api_view(['POST'])
def create_pet(request):
    """
        Recieve json object for pets and save pet
    """
    if request.method == "POST":
        new_pet = request.data

        is_created = Pet.create_pet_from_request_data(new_pet)

        if is_created:
            return HttpResponse("Pet Created Successfully !")
        else:
            return HttpResponse("Failed to Create New Pet")



