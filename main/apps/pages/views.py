from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import PagesTechnicalSkills

# Create your views here.


def index(request):
    return HttpResponse("welcome to pages home page")

# view template using TemplateView class


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class TechnicalSkillsList(ListView):
    model = PagesTechnicalSkills
    template_name = 'pages/about.html'
    context_object_name = 'technical'
