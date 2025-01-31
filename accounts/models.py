from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    sex = models.CharField(null=True, max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ])
    contact_number = models.CharField(max_length=15, null=True)
    age = models.PositiveIntegerField(null=True)

