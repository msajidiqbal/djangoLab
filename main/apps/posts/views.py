from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Post
# Create your views here.

class PostsHomeView(TemplateView):
    template_name = 'posts/index.html'
class PostsListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    # by default, object_list return all model fields
    # we can change object_list to different name using context_object_name
    context_object_name = 'posts'