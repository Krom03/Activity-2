from django.urls import path
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import PetProfile, Services, Appointment, PetRecord
from django.contrib.auth import get_user_model
from .forms import AppointmentForm
from collections import defaultdict

class HomePageView(TemplateView):
    template_name ='app/home.html'

class PetProfileListView(LoginRequiredMixin, ListView):
    model = PetProfile
    template_name = 'pet_profile/pet_profile_list.html'
    context_object_name = 'pets'

    def get_queryset(self):
        if self.request.user.is_authenticated and not self.request.user.is_staff:
            return PetProfile.objects.filter(owner=self.request.user)
        return PetProfile.objects.all()

class PetProfileDetailView(LoginRequiredMixin, DetailView):
    model = PetProfile
    template_name = 'pet_profile/pet_profile_detail.html'
    context_object_name ='pet'

class PetProfileCreateView(LoginRequiredMixin, CreateView):
    model = PetProfile
    fields = ['pet_name', 'owner', 'breed', 'weight', 'sex', 'vaccination_status', 'pet_image']
    template_name = 'pet_profile/pet_profile_create.html'
    success_url = reverse_lazy('pet_profile_list')

    def get_form(self):
        form = super().get_form()
        
        if self.request.user.is_staff:
            form.fields['owner'].queryset = get_user_model().objects.all()
        
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_staff:
            context['users'] = get_user_model().objects.filter(is_staff=False)
        return context

class PetProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = PetProfile
    fields = ['pet_name', 'breed', 'weight', 'sex', 'vaccination_status', 'pet_image']
    template_name = 'pet_profile/pet_profile_update.html'
    context_object_name ='pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('pet_profile_detail', kwargs={'pk': self.object.pk})
    
class PetProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = PetProfile
    template_name = 'pet_profile/pet_profile_delete.html'
    success_url = reverse_lazy('pet_profile_list')

    def get_queryset(self):
        if self.request.user.is_staff:
            return PetProfile.objects.all()
        return PetProfile.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = self.object
        return context

class ServicesListView(LoginRequiredMixin, ListView):
    model = Services
    template_name = 'services/services_list.html'
    context_object_name = 'services'

class ServicesDetailView(LoginRequiredMixin, DetailView):
    model = Services
    template_name = 'services/services_detail.html'
    context_object_name ='service'

class ServicesCreateView(LoginRequiredMixin, CreateView):
    model = Services
    fields = ['service_name', 'service_description', 'price']
    template_name = 'services/services_create.html'
    success_url = reverse_lazy('services_list')

class ServicesUpdateView(LoginRequiredMixin, UpdateView):
    model = Services
    fields = ['service_name', 'service_description', 'price']
    template_name = 'services/services_update.html'
    success_url = reverse_lazy('services_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        context['service'] = service  
        return context

class ServicesDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    template_name = 'services/services_delete.html'
    success_url = reverse_lazy('services_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        context['service'] = service  
        return context

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        if self.request.user.is_authenticated and not self.request.user.is_staff:
            return Appointment.objects.filter(pet__owner=self.request.user)
        return Appointment.objects.all()

class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_create.html'
    success_url = reverse_lazy('appointment_list')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        response = super().form_valid(form)  
        
        selected_services = self.request.POST.getlist('services')  
        if selected_services:
            form.instance.services.set(selected_services) 
        
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = PetProfile.objects.filter(owner=self.request.user)
        context['services'] = Services.objects.all() 
        return context

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_update.html'
    success_url = reverse_lazy('appointment_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        self.object.services.set(self.request.POST.getlist('services'))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_staff:
            context['pets'] = PetProfile.objects.all()  
        else:
            context['pets'] = PetProfile.objects.filter(owner=self.request.user)
        
        context['services'] = Services.objects.all()  
        return context

class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_delete.html'
    success_url = reverse_lazy('appointment_list')


class PetRecordListView(LoginRequiredMixin, ListView):
    model = PetRecord
    template_name = 'pet_record/pet_record_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        if self.request.user.is_staff:  
            return PetRecord.objects.all()
        else:  
            user_pets = PetProfile.objects.filter(owner=self.request.user)
            return PetRecord.objects.filter(pet__in=user_pets)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet_records = defaultdict(list)
        for record in context['records']:
            pet_records[record.pet].append(record)

        context['pet_records'] = dict(pet_records)  
        return context

class PetRecordDetailView(LoginRequiredMixin, DetailView):
    model = PetRecord
    template_name = 'pet_record/pet_record_detail.html'
    context_object_name = 'record'

class PetRecordCreateView(LoginRequiredMixin, CreateView):
    model = PetRecord
    fields = ['pet', 'date', 'check_in_time', 'check_out_time', 'activities', 'notes']
    template_name = 'pet_record/pet_record_create.html'
    success_url = reverse_lazy('pet_record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = PetProfile.objects.all() 
        return context

class PetRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = PetRecord
    fields = ['activities', 'notes']
    template_name = 'pet_record/pet_record_update.html'
    success_url = reverse_lazy('pet_record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = self.object  
        context['pets'] = PetProfile.objects.all()  
        return context

class PetRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = PetRecord
    template_name = 'pet_record/pet_record_delete.html'
    success_url = reverse_lazy('pet_record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = self.object 
        return context

