import json
from django.db import models
from django.http import QueryDict
from authentication.models import User
from ..constants import CURRENCY_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator

class PetType(models.Model):
    """
        Contains the available pet types like, cat, dog etc.
    """
    pettype_id = models.AutoField(primary_key=True,db_column="id")
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)
    
class PetBreed(models.Model):
    """
        Contains the breeds list, associated with pet types
    """
    petbreed_id = models.AutoField(primary_key=True,db_column="id")
    name = models.CharField(max_length=200)
    pettype_id = models.ForeignKey(PetType,on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)

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
    breed = models.ForeignKey(PetBreed,on_delete=models.CASCADE)
    height = models.CharField(max_length = 10)
    weight = models.CharField(max_length = 10)
    color = models.CharField(max_length = 15)
    is_vacinated = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name + " " + str(self.age))

    @classmethod
    def create_pet_from_request_data(cls, request_data):
        try:
            # Convert request.data to a dictionary if it's a QueryDict
            if isinstance(request_data, QueryDict):
                request_data = request_data.dict()

            # Create a new Pet object using the request data
            new_pet = cls(
                name=request_data.get('name'),
                age=request_data.get('age'),
                type_id=request_data.get('type'),
                breed_id=request_data.get('breed'),
                height=request_data.get('height'),
                weight=request_data.get('weight'),
                color=request_data.get('color'),
                is_vacinated=request_data.get('is_vaccinated'),
                creator_id=request_data.get('creator')
            )

            # Save the new_pet object to the database
            new_pet.save()

            return True
        except Exception as e:
            # Handle any exceptions that may occur during the process
            return False

class PetPrice(models.Model):
    """
        Created a Separate Pet Table to keep track of
        price changes made by a user.
        This information can be used to Data Analysis of the website.
    """
    id = models.AutoField(primary_key=True)
    Price = models.IntegerField(
         validators=[
            MinValueValidator(1, message="Price must be greater than 0")
        ]
    )
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES)
    Pet = models.ForeignKey(Pet,on_delete=models.CASCADE)


class Feed(models.Model):
    """
        Contains the Feed Information for a type of pet 
    """

    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    Description = models.CharField(max_length=500)
    price = models.IntegerField(
        MinValueValidator(1,message="Price must be greater than 0")
    )
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES)
    pet_type = models.ForeignKey(PetType,on_delete=models.CASCADE)



