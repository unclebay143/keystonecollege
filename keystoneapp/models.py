from django.db import models
from django import forms

# Create your models here.

class RegistrationData(models.Model):
    jambnumber = models.CharField(max_length=12)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.username
        return self.jambnumber
