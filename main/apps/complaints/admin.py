from django.contrib import admin
from .models import Complaint,Customer,Quality,Product
# Register your models here.
admin.site.register(Complaint),
admin.site.register(Customer),
admin.site.register(Product),
admin.site.register(Quality),

