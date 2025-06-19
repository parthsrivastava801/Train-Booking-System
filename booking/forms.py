from django import forms
from django.contrib.auth.models import User
from .models import Booking

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seat_number']
