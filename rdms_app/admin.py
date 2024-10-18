from django.contrib import admin
from .models import Todo, Author, Books, Myauthor, Mybook

# Register your models here.
admin.site.register(Todo),
admin.site.register(Author),
admin.site.register(Books),
admin.site.register(Myauthor),
admin.site.register(Mybook),
