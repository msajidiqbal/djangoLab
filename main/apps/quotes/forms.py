from django import forms 
from django.forms import ModelForm
from .models import Quote

class QuoteForm(ModelForm):
    required_css_class = 'required'

    # meta class to import all attribute of model
    class Meta:
        model = Quote
        # getting input data from user
        fields = ['name','position','company','address',
                    'phone','email','web','description',
                    'sitestatus','priority','jobfile']
        
