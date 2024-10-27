from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),

    path("articles/", views.articles, name="articles"),
    path("articles/<int:article_id>", views.article_detail, name="article_detail"),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/<int:article_id>/edit/', views.article_edit, name='article_edit'),
    path('articles/<int:article_id>/delete/', views.article_delete, name='article_delete'),

    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

]