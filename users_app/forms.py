from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Userinfo, Otp

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

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}))

class OtpForm(forms.Form):
    otp = forms.CharField(max_length=6, widget = forms.TextInput(attrs={'placeholder': "OTP"}))