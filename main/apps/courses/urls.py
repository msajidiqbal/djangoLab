from django.urls import path
from .views import CoursesListView, CoursesDetailView

app_name = 'courses'
urlpatterns = [
    path('courses/', CoursesListView.as_view(), name='courseList'),
    path('courses/', CoursesDetailView.as_view(), name='courseList'),
]
