from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def profile_page(request):
    return HttpResponse("This is rdms Profile Page")

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


def logout_view(request):
    logout(request)
    return redirect('home_page')