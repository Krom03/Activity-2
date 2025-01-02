from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PetProfile

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )

    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'Email'
        })
    )

    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'First Name'
        })
    )

    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Last Name'
        })
    )
    
    SEX_CHOICES = [
        ('', 'Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Prefer not to say'),
    ]

    sex = forms.ChoiceField(
        choices=SEX_CHOICES, 
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    contact_number = forms.CharField(
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Contact Number'
        })
    )

    age = forms.IntegerField(
        required=True, 
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 'placeholder': 'Age'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2',
            'first_name',
            'last_name', 
            'sex',
            'contact_number',
            'age'
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].help_text = ""
        self.fields['email'].help_text = ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""
        self.fields['first_name'].help_text = ""
        self.fields['last_name'].help_text = ""
        self.fields['sex'].help_text = ""
        self.fields['contact_number'].help_text = ""
        self.fields['age'].help_text = ""

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Username'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )

class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['pet_name', 'breed', 'weight', 'sex', 'vaccination_status'] 
        widgets = {
            'pet_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter pet name'
            }),
            'breed': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter breed'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter weight in kg'
            }),
            'sex': forms.Select(attrs={
                'class': 'form-control'
            }), 
            'vaccination_status': forms.Select(attrs={
                'class': 'form-control'
            })
        }

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight <= 0:
            raise forms.ValidationError("Weight must be a positive number.")
        return weight