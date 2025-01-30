from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'categories', 'photos']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']
        labels = {
            "comments": ""
        }
        widgets = {
            "comments": forms.Textarea(attrs={"style": "border: none; font-size: 18px; cursor: text; resize: vertical;", "placeholder": "Add Your Comments!", "rows": 2, "cols": 20})
        }