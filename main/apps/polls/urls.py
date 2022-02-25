from django.urls import path
from . import views
from .views import HomeListView, PollsDetailView, PollsResultsView
app_name = 'polls'
urlpatterns = [

    path('polls/', HomeListView.as_view(), name='home'),
    path('polls/<int:pk>/', PollsDetailView.as_view(), name='detail'),
    path('polls/<int:pk>/results/', PollsResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/owner/', views.owner, name='owner'),
]
