from django.db import models
import simplejson as json
import uuid
# Create your models here.

class User_Data(models.Model):
    username = models.CharField(max_length=50,primary_key=True,unique=True,default=uuid.uuid4)
    interests = models.CharField(default='[]',unique=False,max_length=600)
    bio = models.CharField(default='',unique=False,max_length=150)
    git = models.CharField(default='',unique=False,max_length=50)
    linked_in = models.CharField(default='',unique=False,max_length=20)
    instagram = models.CharField(default='',unique=False,max_length=20)
    experiance = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    
