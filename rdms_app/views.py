from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo, Books, Mybook, Myauthor

# Create your views here.
def home_page(request):
    return render(request, "rdms/index.html")

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