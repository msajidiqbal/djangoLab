from ast import Delete
from hashlib import new
from pyexpat import model
import django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.


class HomeNewsView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'  # default: object_list
    login_url = 'login'


class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'newsobject'  # default - object
    login_url = 'login'


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    fields = ('title', 'body',)
    template_name = 'news/edit.html'
    success_url = reverse_lazy('news:home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = reverse_lazy('news:home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'news/create.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsHomeLanding(TemplateView):
    template_name = 'news/landing.html'
