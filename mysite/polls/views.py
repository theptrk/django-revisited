from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# def index(request):
#     latest_questions_list = Question.objects.order_by('pub_date')[:5]
#     context = {
#         'latest_questions_list': latest_questions_list
#     }
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    # we are overriding django default template name for ListView
    # <app_name>/<model_name>_list.html
    template_name = 'polls/index.html'

    # by default django would have given as a variable "question_list"
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# def detail(request, question_id):
#     # original implementation
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})

#     # implementation with the shortcut "get_object_or_404"
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

#     # there is also a "get_list_or_404()" function and it raises the exception
#     # if the list is empty

class DetailView(generic.DetailView):
    model = Question
    # we are overriding django default template name for ListView
    # <app_name>/<model_name>_detail.html
    # django default would have been: polls/question_detail.html
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now())

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     response = "youre looking at the results of question %s"
#     return HttpResponse(response % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # .POST['choice'] will raise a KeyError if choice wasnt provided in POST data
    except (KeyError, Choice.DoesNotExist):
        # redisplay question voting form with error
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # always return an HttpResponseRedirect after successfully dealing with POST
        # data. This prevents data from being posted twice if a user hits the back
        # button
        # return HttpResponse("youre voting on question %s" % question_id)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))