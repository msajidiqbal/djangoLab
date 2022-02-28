from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# Create your models here.

statusChoices = (
    # db,printvalue
    ('New', 'New Site'),
    ('Ex','Existing Site'),
)
priorityChoices = (
    ('U','Urgent- 1 week or less'),
    ('N','Normal - 2-4 weeks'),
    ('L','Low - Still Searching'),
)

class Quote(models.Model):
    name = models.CharField(max_length=156)
    position = models.CharField(max_length=60,blank=True)
    company = models.CharField(max_length=86,blank=True)
    address = models.CharField(max_length=200,blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    web = models.URLField(blank=True)
    description = models.TextField()
    sitestatus = models.CharField(max_length=20,choices=statusChoices)
    priority = models.CharField(max_length=48,choices=priorityChoices)
    jobfile = models.FileField(upload_to='uploads/',blank=True)

    # use by siteadmin so, we will not access these in modelfom meta class
    submitted = models.DateField(auto_now_add=True)
    quotedate = models.DateField(blank=True, null=True)
    quoteprice = models.DecimalField(decimal_places=2, max_digits=7,blank=True,default=0.0)
    username = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id

    