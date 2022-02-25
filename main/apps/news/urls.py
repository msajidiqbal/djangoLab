from django.urls import path
from . import views
app_name = 'news'
urlpatterns = [

    path('news/<int:pk>/edit', views.NewsUpdateView.as_view(), name='edit'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name="delete"),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name="detail"),
    path('news/create/', views.NewsCreateView.as_view(), name='create'),
    path('news/', views.HomeNewsView.as_view(), name='home'),
    path('newslanding/', views.NewsHomeLanding.as_view(), name="landing"),
]
