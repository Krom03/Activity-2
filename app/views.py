from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, PetProfileForm
from .models import UserProfile, PetProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff  

    def handle_no_permission(self):
        return redirect('login')  

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm() 
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) 
            
            if user is not None:
                login(request, user)  
                
                if user.is_staff:
                    return redirect('admin-dashboard')  
                else:
                    return redirect('customer-dashboard')  
                
            form.add_error(None, 'Invalid username or password')
        
        return render(request, self.template_name, {'form': form}) 

class RegisterPageView(TemplateView):
    template_name = 'app/register.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm() 
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            
            UserProfile.objects.create(
                user=user,
                sex=form.cleaned_data['sex'],
                contact_number=form.cleaned_data['contact_number'],
                age=form.cleaned_data['age']
            )
            
            return redirect('login')  
        
        return render(request, self.template_name, {'form': form})

class AdminHomePageView(StaffRequiredMixin, TemplateView):
    template_name = 'app/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  
        return context

class CustomerHomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'app/customer_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  
        return context

    def handle_no_permission(self):
        return redirect('login')  

class CustomerPetsPageView(LoginRequiredMixin, ListView):
    model = PetProfile
    template_name = 'app/customer_pets.html'
    context_object_name = 'pets'  

    def get_queryset(self):
        return PetProfile.objects.filter(owner=self.request.user)  

class CustomerPetDetailView(LoginRequiredMixin, DetailView):
    model = PetProfile
    template_name = 'app/customer_petdetails.html'
    context_object_name = 'pet'

    def get_queryset(self):
        return PetProfile.objects.filter(owner=self.request.user)  
    
class CustomerPetCreateView(LoginRequiredMixin, CreateView):
    model = PetProfile
    form_class = PetProfileForm  
    template_name = 'app/customer_addpet.html' 
    success_url = reverse_lazy('customer-pets')  

    def form_valid(self, form):
        form.instance.owner = self.request.user  
        return super().form_valid(form)

class CustomerPetUpdateView(LoginRequiredMixin, UpdateView):
    model = PetProfile
    form_class = PetProfileForm  
    template_name = 'app/customer_updatepet.html'  
    context_object_name = 'pet'
    success_url = reverse_lazy('customer-pets')  

    def get_queryset(self):
        return PetProfile.objects.filter(owner=self.request.user) 

class CustomerPetDeleteView(LoginRequiredMixin, DeleteView):
    model = PetProfile
    template_name = 'app/customer_deletepet.html'  
    context_object_name = 'pet'
    success_url = reverse_lazy('customer-pets')  

    def get_queryset(self):
        return PetProfile.objects.filter(owner=self.request.user)
    

