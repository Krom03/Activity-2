from django.contrib import admin
from .models import UserProfile, PetProfile, Appointment, Services, PetRecord

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'contact_number', 'age')

class PetProfileAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'breed', 'weight', 'sex', 'owner', 'vaccination_status')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet', 'date_time', 'status')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_description', 'price')

class PetRecordAdmin(admin.ModelAdmin):
    list_display = ('pet', 'owner', 'check_in_time', 'check_out_time', 'activities', 'notes')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(PetProfile, PetProfileAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(PetRecord, PetRecordAdmin)