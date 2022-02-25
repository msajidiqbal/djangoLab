from locale import currency
from pipes import Template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from main import settings
import stripe

# Create your views here.


class HomeViewOrder(TemplateView):
    template_name = 'orders/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = "enter string here key"
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']

        )
    return render(request, 'orders/charge.html')
