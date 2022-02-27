from django.urls import path
from .views import BookListView


app_name = 'booksapi'
urlpatterns = [
    path('booksapi/', BookListView.as_view(), name="booksapihome"),
]
