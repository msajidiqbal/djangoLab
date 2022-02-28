from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Book, BookStatus, Author, Genre
from .forms import RenewBook
# Create your views here.

def index(request):
    # return render(request,'catalog/index.html',{'Hello':'Hello From Library page 1'})
    total_books = Book.objects.all().count()
    total_instances = BookStatus.objects.all().count()
    # available books 
    available_books = BookStatus.objects.filter(status__exact='a')
    all_authors = Author.objects.count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'total_books':total_books,
        'total_instances':total_instances,
        'available_books':available_books,
        'all_authors':all_authors,
        'num_visits':num_visits,
    }
    return render(request,'catalog/index.html',context)

def home(request):
    return render(request,'catalog/index.html',{'Hello':'Hello From Library page 2'})
from django.views.generic import ListView, DetailView
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'catalog/index.html'
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book_detailsss'
    template_name = 'catalog/detailview.html'


