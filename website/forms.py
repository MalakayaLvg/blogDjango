from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content"]

        label = {
        "title": "title",
        "content" : "Content",
        }

        widgets ={
        "title": forms.TextInput(attrs={"placeholder": "post title"}),
        "content" : forms.TextInput(attrs={"placeholder":"post content"}),
        }

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username','password1',"password2")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

        label = {"content":"content"}

        widget = {
            "content" : forms.TextInput(attrs={"placeholder":"comment content"})
        }



