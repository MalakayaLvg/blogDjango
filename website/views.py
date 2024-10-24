from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from website.models import Article


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    return render(request, "website/index.html")

def articles(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "article/index.html", context)

def detail(request, article_id):
    article = get_object_or_404(Article,pk=article_id)
    return render(request, "article/detail.html", {"article": article})