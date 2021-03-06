from django.urls import path 
from . import views
# from .views import BookListView
app_name = 'catalog'
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('books/',views.BookListView.as_view(), name='books'),
    path('books/<int:pk>',views.BookDetailView.as_view(),name='book_detail'),
    path('books/uuid:pk/renew/',views.renew_book_librarian, name="renew-book-librarion"),

]
