from django.db import models
from authentication.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class PetType(models.Model):
    """
        Contains the available pet types like, cat, dog etc.
    """
    pettype_id = models.AutoField(primary_key=True,db_column="id")
    name = models.CharField(max_length=50)

class Pet(models.Model):
    """
        - name
        - age
        - type
        - breed
        -properties
            - height
            - weight
            - color
            - is_vaccinated
    """
    id = models.AutoField(primary_key = True,db_column='pet_id')
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Age must be at least 1."),
            MaxValueValidator(30, message="Age must be at most 30.")
        ]
    )
    type = models.ForeignKey(PetType,on_delete=models.CASCADE)
    height = models.CharField(max_length = 10)
    weight = models.CharField(max_length = 10)
    color = models.CharField(max_length = 15)
    is_vacinated = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class PetBreed(models.Model):
    """
        Contains the breeds list, associated with pet types
    """
    petbreed_id = models.AutoField(primary_key=True,db_column="id")
    name = models.CharField(max_length=200)
    pettype_id = models.ForeignKey(PetType,on_delete=models.CASCADE)


