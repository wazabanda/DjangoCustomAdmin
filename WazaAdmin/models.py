from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profiles',null=True)
    role = models.CharField(max_length=60, null=True)
    
    
    
class Message(models.Model):
    name = models.CharField(max_length=30,default="")
    from_email = models.EmailField(null=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField()