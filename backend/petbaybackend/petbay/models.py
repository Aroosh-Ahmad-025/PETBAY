from django.db import models
from django.contrib import admin

# Create your models here.

class LoginUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    list_display = ("id","name","email")

    # def __str__(self):
    #     return f"{self.name} - {self.email}"
