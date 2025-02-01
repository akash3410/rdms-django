from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("profile/", views.profile_page, name='profile_page'),
    path("register/", views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('update-profile/', views.update_view, name='update_view'),
    path('edit-userinfo/', views.edit_profile_info, name='edit_profile_info'),
    path('otp-verify/', views.Otp_verify, name="Otp_verify"),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name = 'registration/password_reset_form.html'
         ),
         name = 'password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete')
]