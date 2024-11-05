from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from website.forms import PostForm, CommentForm
from website.models import Post, Comment, Like
from django.contrib.auth.models import User
from .forms import SignUpForm



def index(request):
    return render(request, "website/home.html")

def posts(request):
    all_posts = Post.objects.prefetch_related("comments","likes")
    context = {"posts": all_posts}
    for post in all_posts:
        post.user_has_liked = post.likes.filter(user=request.user).exists
    return render(request, "post/index.html", context)

def post_show(request, post_id):
    post = get_object_or_404(Post,pk=post_id)

    return render(request, "post/detail.html", {"post": post})

def post_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                form.save()
                return redirect('posts')
        else:
            form = PostForm()
        return render(request, 'post/create.html', {'form': form})
    else:
        return redirect("login")


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


def comment_create(request, post_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = get_object_or_404(Post, pk=post_id)
                form.save()
                return redirect("posts")
        else:
            form = CommentForm()
            context = {"form":form}
            return render(request,"comment/create.html",context)
    else:
        redirect("login")

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    if comment.author == request.user:
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect("posts")
        else:
            form = CommentForm(instance=comment)
            context = {"form":form}
            return render(request,"comment/edit.html", context)
    else:
        return redirect("posts")

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    if comment.author == request.user:
        comment.delete()
    return redirect("posts")

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect("posts")

###################################################################

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
    return render(request, "registration/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})






