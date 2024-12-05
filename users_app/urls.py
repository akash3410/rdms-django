from django.urls import path, include
from .import views

urlpatterns = [
    path("profile/", views.profile_page, name='profile_page'),
    path("register/", views.register, name='register'),
]