from django.db import models
import datetime

from django.db.models.base import Model
from django.db.models.fields import AutoField
from django.db.models.lookups import StartsWith
# Create your models here.
receivedByChoices = (
    ('CS','Customer Service'),
    ('QA','Quality Assurance'),
    ('SE', 'Security'),
    )
complainantChoices = (
    ('Customer','Customer'),
    ('Doctor','Doctor'),
    ('Hospital','Hospital'),
    ('Regulatory','Regulatory'),
    )
productChoices = (
    ('select','select'),
    ('Dry Flower','Dry Flower'),
    ('Pre-Rolls','Pre-Rolls'),
    ('Extracts','Extracts'),
    ('Oil','Oil'),
    ('Vape','Vape Cartridge'),
    ('Battery','Battery'),
)
complaintTypeChoices = (
    ('select','select'),
    ('Quality','Quality'),
    ('Packaging','Packaging'),
    ('Shipping','Shipping'),
    ('Wrong Order','Wrong Order'),
    ('Defective','Defective'),
    ('Loss/Theft','Loss/Theft'),
    ('Adverse Rx', 'Adverse Reaction'),
    ('Serious Adx','Serious Adverse Reaction'),
)
contactViaChoices = (
    ('select','select'),
    ('Email','Email'),
    ('Phone','Phone'),
    ('Fax','Fax'),
)
provinceChoice = (
    ('select','select'),
    ('AB','AB'),
    ('BC','BC'),
    ('MB','MB'),
    ('SK','SK'),
    ('YK','YK'),
    ('ON','ON'),
    ('QC','QC'),
    ('NB','NB'),
    ('NS','NS'),
    ('NF','NF'),
)
def incrementComplaintId():
    last_complaint_id = Complaint.objects.all().last()
    if not last_complaint_id:
        return 'CC-' + str(datetime.date.today().year)+'-' + str(1).zfill(4)
    return 'CC-' + str(datetime.date.today().year)+'-' + str(last_complaint_id.id + 1).zfill(4)

def abrIdGenerator(className, abr):
    # return > abr-year-xxxx
    lastId = className.objects.all().last()
    if not lastId:
        return str(abr) +'-' + str(datetime.date.today().year)+'-' + str(1).zfill(4)
    return str(abr) +'-' + str(datetime.date.today().year)+'-' + str(lastId.id + 1).zfill(4)

class Complaint(models.Model):
    # def autoNumber():
    #     # return ABR-Year-XXXX
    #     lastComplaint = Complaint.objects.all().last()
    #     if not lastComplaint:
    #         return 'CC-' + str(datetime.date.today().year)+'-' + str(1).zfill(4)
    #     return 'CC-' + str(datetime.date.today().year)+'-' + str(lastComplaint.id + 1).zfill(4)
    def abrIdGenerator():
        # return > abr-year-xxxx
        abr = 'CC'
        lastId = Complaint.objects.all().last()
        if not lastId:
            return str(abr) +'-' + str(datetime.date.today().year)+'-' + str(1).zfill(4)
        return str(abr) +'-' + str(datetime.date.today().year)+'-' + str(lastId.id + 1).zfill(4)

    complaintId = models.CharField(editable=False,default=abrIdGenerator, max_length=36) #models.CharField(max_length=24, default= incrementComplaintId(),editable=False,unique=True) #models.IntegerField(auto_created=True)
    creationDate = models.DateTimeField('Date Created',auto_now_add=True)
    receivedBy = models.CharField('Received By',choices=receivedByChoices,max_length=24,default='Customer Service')
    complainant = models.CharField('Complainant',choices=complainantChoices,max_length=24,default='Customer')
    complaintType = models.CharField('Complaint Type', choices=complaintTypeChoices,default='complaint type', max_length=32, blank=False)
    description = models.TextField('Complaint Description', blank=False)
    contactVia = models.CharField('Contact', choices=contactViaChoices,default=None, max_length=32)
    confirmation = models.CharField('Complaint is', choices=(('Not Confirmed','Not Confirmed'),('Confirmed','Confirmed'),), default='Not Confirm', max_length=42)
    def __str__(self):
        return self.complaintId


class Customer(models.Model):
    customerId = models.ForeignKey(Complaint,on_delete=models.CASCADE)
    firstName = models.CharField('First Name', max_length=24)
    lastName = models.CharField('Last Name',max_length=24)
    identificatioId = models.CharField('Identification ID', max_length=24)
    address = models.TextField('Address',default=None,editable=True,max_length=64)
    zipcode = models.CharField('Postal Code',max_length=7,default=None)
    province = models.CharField('Province', default=None,editable=True,choices=provinceChoice, max_length=12)
    customerInstanceId = models.AutoField(primary_key=True,unique=True)

    def __str__(self):
        return self.firstName

class Product(models.Model):
    productId = models.ForeignKey(Complaint,on_delete=models.CASCADE)
    productName = models.CharField('Product Name', max_length=24)
    productLot = models.CharField('Lot #', max_length=24)
    NumOfUnits = models.IntegerField('Units #' , default=1)
    weight = models.FloatField('Weight',default=0.0,max_length=24, help_text='in grams or ml')
    productType = models.CharField('Product Type', choices=productChoices,default=None,max_length=24)
    
    def __str__(self):
        return self.productLot
    


class Quality(models.Model):
    incidentId = models.ForeignKey(Complaint,on_delete=models.CASCADE)
    investigationTitle = models.CharField('Title',max_length=256,editable=True)
    investigation = models.TextField('Quality Investigation', max_length=3000, blank=True, editable=True)
    conclusion = models.TextField('Conclusions',editable=True,max_length=2000)
    correctAction =models.TextField('Corrective Actions',editable=True,max_length=2000)
    capa = models.CharField('CAPA',max_length=250,editable=True)
    qualityInstanceId = models.AutoField(primary_key=True,unique=True)

    def __str__(self):
        return self.investigationTitle
    

if __name__=="__main__":
    print(Complaint.abrIdGenerator())




