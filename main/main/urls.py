"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls')),
    path('', include('apps.posts.urls')),
    path('', include('apps.blogs.urls')),
    path('', include('apps.polls.urls')),
    path('', include('apps.news.urls')),
    path('', include('apps.bookstore.urls')),
    path('', include('apps.orders.urls')),

    # API urls
    path('', include('apps.booksapi.urls')),
    path('', include('apps.todoapi.urls')),
    path('', include('apps.blogapi.urls')),

    # enrolnew - local app for signup setup
    path('', include('apps.enrolnew.urls')),

    # users app
    path('', include('apps.users.urls')),
    # accounts/users/or any name: using default auth django
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # add permissions provided by rest_framework and user login from rest_frame page
    path('api-auth/', include('rest_framework.urls')),

    # add following urls if rest_auth app is used
    # path('blogapi/rest-auth/', include('rest_auth.urls')),
    # path('blogapi/rest-auth/registration/', include('rest_auth.registration.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
