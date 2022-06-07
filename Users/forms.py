from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'username':{
                'unique': 'unique',
                'max_length': 'max_length'
            }
        }

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class EditProfile(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ['image']

