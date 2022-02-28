from django.urls import path
from . import views
urlpatterns = [
    # quotes/
    path('',views.quote_req,name='quoteRequest'),
]
