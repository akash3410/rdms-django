from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm, UpdateForm, UserinfoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from post_app.models import Blog

# Create your views here.
@login_required
def profile_page(request):
    blogs = Blog.objects.filter(user=request.user).prefetch_related('categories')
    if blogs:
        return render(request, "rdms/dashboard.html", {'blogs': blogs})
    else:
        message = "No Post to Show!"
        return render(request, "rdms/dashboard.html", {'message': message})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
        
    return render(request, 'users_app/register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'users_app/login.html', {'form': form})
    return render(request, 'users_app/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required
def update_view(request):
    if request.method == "POST":
        form = UpdateForm(data = request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = UpdateForm(instance=request.user)

    return render(request, 'users_app/update.html', {'form': form})

@login_required
def edit_profile_info(request):
    if request.method == 'POST':
        form = UserinfoForm(request.POST, request.FILES, instance=request.user.userinfo)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = UserinfoForm(instance=request.user.userinfo)
    return render(request, 'users_app/user_info.html', {'form': form})