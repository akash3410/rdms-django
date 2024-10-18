from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home_page, name="home_page"),
    path('todos/', views.all_todos, name="all_todos"),
    path('todo/<int:pk>/', views.single_todo, name="single_todo"),
    path('todos/user/<int:user_id>/', views.todo_by_user, name="todo_by_user"),
    path('books/', views.all_books, name="all_books"),
    path('books/<int:pk>/', views.single_book, name="book"),
    path('books/user/<int:author_id>/', views.book_by_author, name="book_by_author"),
    path('mybooks/', views.all_mybooks, name="all_mybooks"),
    path('mybooks/<int:pk>/', views.mybook, name="mybook"),
    path('mybook/author/<int:myauthor_id>/', views.mybook_by_author, name="mybook_by_author"),
]