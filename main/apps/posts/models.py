from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, blank=True,help_text='Post Title', editable=True)
    text = models.TextField(max_length=1500,blank=True, help_text='Post Details', editable=True)

    def __str__(self):
        return self.title