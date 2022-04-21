from re import A
from django.core import validators
from django import forms
from .models import User,CustomerDetails
class PatientRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','Email','Password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
class CustomerDetailsRegistration(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['name','Email','Order']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Order': forms.TextInput(attrs={'class':'form-control'})
        }