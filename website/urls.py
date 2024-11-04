from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("posts/", views.posts, name="posts"),
    path("posts/<int:post_id>", views.post_show, name="post_show"),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),

    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile', views.user_profile,name='profile')

]