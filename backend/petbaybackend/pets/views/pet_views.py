from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.pet_models import Pet

@login_required
def create_pet(request):
    """
        Recieve json object for pets and save pet
    """
    new_pet = request.pet

    is_created = Pet.create_pet_from_json(new_pet)

    if is_created:
        return HttpResponse("Pet Created Successfully !")
    else:
        return HttpResponse("Failed to Create New Pet")



