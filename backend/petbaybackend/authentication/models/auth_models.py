from django.db import models

class LoginUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    list_display = ("id","name","email")