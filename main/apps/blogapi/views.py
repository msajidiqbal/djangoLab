from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogkSerializer
# permission settings
from rest_framework import permissions

# Create your views here.


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogkSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permissions can also be set here. better to set at project level in settings.py file
    # set permissions for authenticated users
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # retrive, update, and delete
    queryset = Blog.objects.all()
    serializer_class = BlogkSerializer
