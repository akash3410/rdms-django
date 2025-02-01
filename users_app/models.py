from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')
    bio = models.CharField(max_length=20, null=True, blank=True)
    secondary_phone = models.IntegerField(null=True, blank=True)
    seconday_email = models.EmailField(null=True, blank=True)
    present_address = models.TextField(max_length=100, null=True, blank=True)
    permanent_address = models.TextField(max_length=100, null=True, blank=True)
    profile_picture = models.FileField(upload_to='document/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Otp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otp')
    otp = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f'Username: {self.user.username}, otp: {self.otp}'