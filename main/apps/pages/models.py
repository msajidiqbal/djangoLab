
from django.db import models

# Create your models here.


class PagesTechnicalSkills(models.Model):
    image = models.ImageField(upload_to='covers/', blank=True)
    name = models.CharField(
        max_length=150, editable=True, blank=True, null=True)
    value = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
