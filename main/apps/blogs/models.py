from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True,editable=True,help_text='Blog Title')
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField(help_text='Blog Details',editable=True,blank=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blogs:detail", args=[str(self.id)])
        
