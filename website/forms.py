from .models import Article
from django import forms

class TodoForm(forms.ModelForm):
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