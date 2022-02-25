from django.urls import path
from .views import BlogHomeListView, BlogDetailView, BlogCreateNew, BlogEditView, BlogDelView

app_name = 'blogs'
urlpatterns = [
    path('blogs/<int:pk>/delete', BlogDelView.as_view(),name='delblog'),
    path('blogs/<int:pk>/edit/', BlogEditView.as_view(),name='editblog'),
    path('blogs/new/', BlogCreateNew.as_view(),name='createblog'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(),name='detail'),
    path('blogs/', BlogHomeListView.as_view(),name='home'),
    
]
