from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blogapi'
urlpatterns = [
    path('blogapi/<int:pk>', BlogDetailView.as_view()),
    path('blogapi/', BlogListView.as_view(), name='blogapihome'),
]
