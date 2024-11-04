from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100,default="no title")
    content = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True )
    created_at = models.DateTimeField(auto_now=True, null=True)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)
#     created_at = models.DateTimeField(auto_now=True, null=True)

