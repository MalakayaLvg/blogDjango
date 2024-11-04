from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from website.forms import PostForm
from website.models import Post
from django.contrib.auth.models import User
from .forms import SignUpForm



def index(request):
    return render(request, "website/home.html")

def posts(request):
    all_posts = Post.objects.all()
    context = {"posts": all_posts}
    return render(request, "post/index.html", context)

def post_show(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request, "post/detail.html", {"post": post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit.html', {'form': form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('posts')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('posts')
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
                return redirect('posts')
    else:
        form = AuthenticationForm()
    return render(request, "users/templates/registration/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request):
    user = request.user  # L'utilisateur connecté
    return render(request, 'users/profile.html', {'user': user})


