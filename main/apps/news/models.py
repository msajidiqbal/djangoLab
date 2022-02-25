from pyexpat import model
from statistics import mode
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import get_urlconf, reverse, reverse_lazy
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # get_user_model will get 'users.CustomUser' automatically. or use 'users.CustomUser' instead.
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("news:detail", args=[str(self.id)])


class Comments(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("news:home", args=[str(self.id)])
