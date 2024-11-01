from .models import Article
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        label = {
        "content" : "Content",
        "number" : "number",
        }

        widgets ={
        "content" : forms.TextInput(attrs={"placeholder":"Buy Groceries"}),
        "description" : forms.TextInput(attrs={"placeholder":"Visit super market and buy some groceries"}),
        }

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username','password1',"password2")