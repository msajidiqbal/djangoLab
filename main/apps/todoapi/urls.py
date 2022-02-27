from django.urls import path
from .views import TodoListView, TodoDetailView

app_name = 'todoapi'

urlpatterns = [
    path('todoapi/<int:pk>/', TodoDetailView.as_view()),
    path('todoapi/', TodoListView.as_view(), name='todoapihome'),
]
