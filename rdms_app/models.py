from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Many to One (Post:User)
class Todo(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    
    def __str__(self):
        return self.title
    
#One to One (User:Profile)
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.first_name
    
class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name="author")
    
    def __str__(self):
        return self.title

#Many to Many (Author:Books)    
class Myauthor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.first_name

class Mybook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    myauthor = models.ManyToManyField(Myauthor, related_name="myauthor")
    
    def __str__(self):
        return self.title