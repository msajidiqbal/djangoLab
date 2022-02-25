from django.urls import path
from .views import HomeViewOrder, charge

app_name = 'orders'
urlpatterns = [
    path('orders/', HomeViewOrder.as_view(), name="orders"),
    path('charge', charge, name='charge'),

]
