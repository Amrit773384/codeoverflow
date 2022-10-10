from django.db import models

# Create your models here.

class User_Data(models.Model):
    email = models.CharField(max_length=200,default="",primary_key=True)
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=True)
    username = models.CharField(max_length=200,blank=False)
    password = models.CharField(max_length=200,blank=False)
