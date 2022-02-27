from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics
# Create your views here.


class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
