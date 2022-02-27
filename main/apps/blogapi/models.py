from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='blogapi')

    def __str__(self):
        return self.title
