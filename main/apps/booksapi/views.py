from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer
# Create your views here.


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
