from django.urls import path, include
from .import views

urlpatterns = [
    path("profile/", views.profile_page, name='profile_page'),
    path("register/", views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('update/profile/', views.update_view, name='update_view'),
    path('edit/userinfo/', views.edit_profile_info, name='edit_profile_info'),
]