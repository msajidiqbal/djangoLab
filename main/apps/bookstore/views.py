from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from apps.bookstore.models import Book

#  add authentication and permissions
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.


class BookStoreHome(TemplateView):
    template_name = 'bookstore/index.html'


class BookSearchView(ListView):
    model = Book
    context_object_name = 'booklist'
    template_name = 'bookstore/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(title__icontains=query))


class BookStoreListView(ListView):
    model = Book
    template_name = 'bookstore/index.html'
    context_object_name = 'booklist'


class BookStoreDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'bookstore/detail.html'
    context_object_name = 'bookdetail'
    login_url = 'login'
    permission_required = 'bookstore.special_status'
