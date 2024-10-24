from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),

    path("articles/", views.articles, name="articles"),

    path("articles/<int:article_id>", views.detail, name="detail"),
]