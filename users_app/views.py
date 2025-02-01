from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegisterForm, UpdateForm, UserinfoForm, LoginForm, OtpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from post_app.models import Blog
from post_app.forms import CommentForm
from users_app.models import Userinfo, Otp
import random

# Create your views here.
@login_required
def profile_page(request):
    blogs = Blog.objects.filter(user=request.user).prefetch_related('categories')
    if blogs:
        if request.method == "POST":
            blog_id = request.POST.get('blog_id')
            blog = get_object_or_404(Blog, id=blog_id)

            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog
                comment.user = request.user
                comment.save()
                form = CommentForm()
                return redirect(f'{request.path}#comments-{blog.id}')
        else:
            form = CommentForm()

        return render(request, "rdms/dashboard.html", {'blogs': blogs, 'form': form})
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
    if request.user.is_authenticated:
        return redirect('home_page')
    
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            otp = ''.join([str(random.randint(0,9)) for _ in range(6)])
            user_otp, created = Otp.objects.get_or_create(user=user)
            user_otp.otp = otp
            user_otp.save()
            print(f"{user.username}'s {otp}")
            request.session['pre_otp_user_id'] = user.id
            return redirect('Otp_verify')
        
    form = LoginForm()
    return render(request, 'users_app/login.html', {'form': form})

def Otp_verify(request):
    user_id = request.session['pre_otp_user_id']
    if not user_id:
        return redirect('login_view')
    
    user = User.objects.get(id=user_id)
    user_otp = Otp.objects.get(user=user)
    if request.method == "POST":
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            if otp == user_otp.otp:
                user_otp.otp = ''
                user_otp.save()
                login(request, user)
                del request.session['pre_otp_user_id']
                return redirect('profile_page')
            else:
                form.add_error('otp', 'invalid otp')
    else:
        form = OtpForm()
    return render(request, 'users_app/otpform.html', {'form': form})

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
    user = request.user

    if not hasattr(user, 'userinfo'):
        Userinfo.objects.create(user=user)

    if request.method == 'POST':
        form = UserinfoForm(request.POST, request.FILES, instance=user.userinfo)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = UserinfoForm(instance=user.userinfo)
    return render(request, 'users_app/user_info.html', {'form': form})