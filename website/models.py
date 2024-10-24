from django.db import models

class Article(models.Model):
    content = models.CharField(max_length=400)
    numbers = models.IntegerField(default=0)
