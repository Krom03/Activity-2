from django.contrib import admin
from .models import PetProfile, Appointment, Services, PetRecord

admin.site.register(PetProfile)
admin.site.register(Appointment)
admin.site.register(Services)
admin.site.register(PetRecord)