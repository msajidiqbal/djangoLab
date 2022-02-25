from django.urls import path
from . import views

app_name = 'bookstore'
urlpatterns = [
    path('<int:pk>', views.BookStoreDetailView.as_view(), name='detail'),
    path('bookstore/', views.BookStoreListView.as_view(), name='home'),
    path('search/', views.BookSearchView.as_view(), name='search'),
]
