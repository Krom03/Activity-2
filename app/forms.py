from django import forms
from .models import PetProfile, Appointment, Services

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
    

class AppointmentForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Services.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Appointment
        fields = ['pet', 'date', 'time', 'status', 'services']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

