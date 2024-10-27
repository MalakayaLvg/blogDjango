from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from website.forms import ArticleForm
from website.models import Article
from django.contrib.auth.models import User
from .forms import SignUpForm



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    return render(request, "website/index.html")

def articles(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "article/index.html", context)

def article_detail(request, article_id):
    article = get_object_or_404(Article,pk=article_id)
    return render(request, "article/detail.html", {"article": article})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm()
    return render(request, 'article/create.html', {'form': form})


def article_edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article/edit.html', {'form': form})

def article_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('articles')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('articles')
    else:
        form = SignUpForm()
    return render(request,"users/signup.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('articles')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html" , {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


