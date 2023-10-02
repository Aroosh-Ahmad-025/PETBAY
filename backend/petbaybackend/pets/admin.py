from django.contrib import admin
from .models.pet_models import *

# Register your models here.
admin.site.register(Pet)
admin.site.register(PetType)
admin.site.register(PetBreed)
admin.site.register(PetPrice)
admin.site.register(Feed)

