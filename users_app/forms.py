from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userinfo

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['bio','secondary_phone','seconday_email','present_address','permanent_address','profile_picture']