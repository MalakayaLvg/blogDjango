from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CASCADE


class Post(models.Model):
    title = models.CharField(max_length=100,default="no title")
    content = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True )
    created_at = models.DateTimeField(auto_now=True, null=True)

class Comment(models.Model):
    content = models.TextField()
    author = ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now=True,null=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="likes")
    class Meta:
        unique_together = ("user","post")

