from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate
from .models import UserData
from django import forms


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=255)

    class Meta:
        model = UserData
        fields = ['username', 'email', 'password1', 'password2']


class CompleteProfile(UserChangeForm):

    class Meta:
        model = UserData
        fields = ['first_name', 'last_name', 'profile_image']


class ImageUploadForm(forms.Form):
    name = forms.CharField(max_length=10)
    image = forms.ImageField()
