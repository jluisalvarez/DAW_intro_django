from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    publish = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
