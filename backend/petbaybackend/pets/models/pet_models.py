from django.db import models
from authentication.models import User
from ..constants import CURRENCY_CHOICES
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



