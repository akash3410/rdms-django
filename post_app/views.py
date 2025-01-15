from django.shortcuts import render, redirect
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            form.save_m2m()
            return redirect('profile_page')
    else:
        form = BlogForm()
    return render(request, 'post_app/create_post.html', {'form':form})
