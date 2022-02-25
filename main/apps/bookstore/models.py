from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
# Create your models here.


class Book(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False,
    #     blank=True,
    # )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # use filefield for any type of document
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bookstore:detail", args=[str(self.id)])

# add review model


class Review(models.Model):
    # related name is use to access this model in templates
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=254)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review
