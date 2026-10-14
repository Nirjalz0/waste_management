from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=[
        ('citizen','Citizen'),
        ('collector','Collector'),
        ('admin','Admin'),

    ]
    role=models.CharField(max_length=20, choices=ROLE_CHOICES, default='citizen')
    phone= models.CharField(max_length=15, blank=True)
    address= models.TextField(blank=True)

# Create your models here.
