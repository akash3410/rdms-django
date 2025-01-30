from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Blog

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



@login_required
def edit_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, user=request.user)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'post_app/edit_post.html', {'form': form})

@login_required
def delete_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, user=request.user)
    blog.delete()
    return redirect('profile_page')
