from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Create your models here.

class LoginUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        abstract = True

class User(AbstractBaseUser):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)

    REQUIRED_FIELDS = ["password"]
    USERNAME_FIELD = "email"

    list_display = ("id","name","email")