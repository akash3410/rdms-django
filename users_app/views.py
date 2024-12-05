from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm

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