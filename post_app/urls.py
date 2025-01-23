from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:blog_id>', views.edit_post, name='edit_post'),
    path('delete/<int:blog_id>', views.delete_post, name='delete_post'),
]