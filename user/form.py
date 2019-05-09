from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='Full Name')
    regno = forms.CharField(max_length=20, label='Registration Number')

    class Meta:
        model = UserProfile
        fields = ['name', 'username', 'regno', 'email', 'password1', 'password2']

