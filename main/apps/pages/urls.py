from django.urls import path
from django.views.generic.base import View
from . import views

app_name = 'pages'
urlpatterns = [
    path('pages/',views.index, name='index'),
    path('',views.HomePageView.as_view(),name="home"),
    path('about/',views.AboutPageView.as_view(),name='about'),
]
