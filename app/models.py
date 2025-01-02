from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ])
    contact_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()

class PetProfile(models.Model):
    pet_name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    VACCINATION_STATUS_CHOICES = [
        ('vaccinated', 'Vaccinated'),
        ('not_vaccinated', 'Not Vaccinated'),
    ]
    
    vaccination_status = models.CharField(
        max_length=20,
        choices=VACCINATION_STATUS_CHOICES,
        default='not_vaccinated'
    )

    def __str__(self):
        return self.pet_name

class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ])

    services = models.ManyToManyField(Services)

class PetRecord(models.Model):
    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    activities = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)