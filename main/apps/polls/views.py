from django.core.exceptions import RequestAborted
from django.db.models import fields
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Question, Choice
from django.template import context, loader
from django.http import Http404
from django.urls import reverse

# Create your views here.


class HomeListView(ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class PollsDetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'question'


class PollsResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'
    context_object_name = 'question'

# more views functions


def vote(request, question_id):
    # return HttpResponse("You are voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def owner(request):
    return HttpResponse("Hello, world. 46384036 is the polls owner.")
