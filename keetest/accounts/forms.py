from dataclasses import fields
from django import forms
from .models import Profile

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User

#login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

#register Form
class UserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    email = forms.CharField(label='Email Address', widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    phonenumber = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    class Meta:
        model = Profile
        fields = ('birthday', 'phonenumber', 'image')