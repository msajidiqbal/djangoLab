from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Photo, Category
# Create your views here.


class CoursesListView(ListView):
    model = Photo
    template_name = 'courses/index.html'
    # template_name = 'pages/about.html'
    context_object_name = 'coursesList'


class CoursesDetailView(DetailView):
    model = Photo
    template_name = 'courses/index.html'
    context_object_name = 'coursesDetail'
