from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=24, null=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200, blank=True,
                            null=True, editable=True)
    image = models.ImageField(upload_to='covers/', blank=True)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.name
