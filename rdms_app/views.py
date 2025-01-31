from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Todo, Books, Mybook, Myauthor
from users_app.models import Userinfo
from post_app.models import Blog
from post_app.forms import CommentForm

# Create your views here.
def home_page(request):
    blogs = Blog.objects.all()

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
        return render(request, "rdms/index.html", {'blogs': blogs, 'form': form})
    else:
        message = "No Post to Show!"
        return render(request, "rdms/index.html", {'message': message})

# Many to One
def all_todos(request):
    # todos = Todo.objects.filter(user_id=user_id).values()
    todos = Todo.objects.all().values()
    return JsonResponse({'todos': list(todos)})

def single_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    result = {
        'id': todo.pk,
        'title': todo.title,
        'decription': todo.decription,
        'created_at': todo.created_at,
        'due_date': todo.due_date,
        'users': todo.user.first_name
    }
    return JsonResponse({'todo': result})

def todo_by_user(request, user_id):
    todos = Todo.objects.filter(user_id=user_id).values()
    return JsonResponse({'todos': list(todos)})

def all_books(request):
    books = Books.objects.all().values()
    return JsonResponse({'books': list(books)})

def single_book(request, pk):
    try:
        book = Books.objects.get(pk=pk)
        result = {
            'pk': book.pk,
            'title': book.title,
            'description': book.description,
            'author': book.author.first_name
        }
        return JsonResponse({'book': result})
    except Books.DoesNotExist:
        return redirect("all_books")

def book_by_author(request, author_id):
    try:
        book = Books.objects.filter(author_id=author_id).values()
        return JsonResponse({'book:': list(book)})
    except Books.DoesNotExist:
        return redirect("all_mybooks")

def all_mybooks(request):
    mybooks = Mybook.objects.all()
    result = []
    for book in mybooks:
        result.append({
            'id': book.pk,
            'title': book.title,
            'description': book.description,
            'myauthors': [
                {
                    'id': author.id,
                    'first_name': author.first_name,
                    'last_name': author.last_name,
                    'bio': author.bio
                } for author in book.myauthor.all()
            ]
        })
    return JsonResponse({'mybooks': result})

def mybook(request, pk):
    try:
        book = Mybook.objects.get(pk=pk)
        result = {
            'id': book.pk,
            'title': book.title,
            'description': book.description,
            'authors': [
                {
                'author': f'{author.first_name} {author.last_name}' 
                } for author in book.myauthor.all()
            ]
        }
        return JsonResponse({'book': result})
    except Mybook.DoesNotExist:
        return redirect("all_mybooks")

def mybook_by_author(request, myauthor_id):
    try:
        author = Myauthor.objects.get(pk=myauthor_id)
        author_details = {
            'id': author.pk,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'bio': author.bio,
            'books:': [book.title for book in author.myauthor.all()]
        }
        return JsonResponse({'author_details': author_details})
    except Myauthor.DoesNotExist:
        return redirect("all_mybooks")