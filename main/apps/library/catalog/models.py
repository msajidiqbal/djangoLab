from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import AbstractUser

# user model 

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre - like Horror')
    def __str__(self):
        return self.name
class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birth_date = models.DateField(null=True,blank=True)
    death_date = models.DateField('Died',null=True,blank=True)

    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    def __str__(self):
        return f'{self.last_name},{self.first_name},{self.birth_date}'
    class Meta:
        ordering = ['last_name','first_name','birth_date']
    
class Book(models.Model):
    title = models.CharField(max_length=256)
    # if book class is defined before author, then model name will come as string as 'Author' to aviod error
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description about Book")
    isbn = models.CharField('ISBN', max_length=13, unique=True,help_text='13 unique charaters code')
    genre = models.ManyToManyField(Genre,help_text='select a genre for this book')
    def __str__(self):
        return f'{self.title},{self.isbn}'
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
        # return reverse('catalog:book_detail', args=(self.id))

class BookStatus(models.Model):
    # class for borrow, return, book status
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book,on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)

    loan_status_choices=(
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved'),
    )
    status = models.CharField(max_length=1,choices=loan_status_choices,blank=True,default='m',help_text='Book Availability Status')
    def __str__(self):
        return f' {self.id},{self.book.title} '
    class Meta:
        ordering = ['due_back','id']
    