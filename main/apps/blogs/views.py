from django.db import models
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  UpdateView, CreateView, DeleteView
from .models import Blog
# Create your views here.

class BlogHomeListView(ListView):
    model = Blog
    template_name = 'blogs/index.html'
    context_object_name = 'bloglist'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detail.html'
    context_object_name = 'blogdetail'
class BlogCreateNew(CreateView):
    model = Blog
    template_name = 'blogs/createblog.html'
    fields = '__all__'
class BlogEditView(UpdateView):
    model = Blog
    template_name = 'blogs/editblog.html'
    fields =['title','body']
class BlogDelView(DeleteView):
    model = Blog
    template_name = 'blogs/delblog.html'
    success_url = reverse_lazy('blogs:home')
