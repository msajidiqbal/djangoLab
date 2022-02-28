from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
from .forms import QuoteForm
from apps.pages.models import Page
# Create your views here.

def quote_req(request):
    submitted=False
    if request.method == 'POST':
        form = QuoteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('quote/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted=True
    context = {
        'form':form, 
        'pageList':Page.objects.all(),
        'submitted':submitted,
    }
    return render(request,'quotes/quote.html',context)
# def quote_req(request):
#     return render(request,'quotes/quote.html')