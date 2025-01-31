from django.db import models
from django.conf import settings
from django.urls import reverse

class PetProfile(models.Model):
    pet_name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    VACCINATION_STATUS_CHOICES = [
        ('vaccinated', 'Vaccinated'),
        ('not_vaccinated', 'Not Vaccinated'),
    ]
    
    vaccination_status = models.CharField(
        max_length=20,
        choices=VACCINATION_STATUS_CHOICES,
        default='not_vaccinated'
    )

    pet_image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.pet_name
    
    def get_absolute_url(self):
        return reverse('pet_profile_detail', kwargs={'pk': self.pk})


class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk})


class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed')
    ])

    services = models.ManyToManyField(Services)

    def __str__(self):
        return f"Appointment for {self.pet.pet_name} on {self.date} at {self.time}"

    def get_absolute_url(self):
        return reverse('appointment_detail', kwargs={'pk': self.pk})


class PetRecord(models.Model):
    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    activities = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.pet} - {self.date}"


    def get_absolute_url(self):
        return reverse('pet_record_detail', kwargs={'pk': self.pk})
