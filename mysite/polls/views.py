from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    latest_questions_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_questions_list': latest_questions_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # original implementation
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # implementation with the shortcut "get_object_or_404"
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # there is also a "get_list_or_404()" function

def results(request, question_id):
    response = "youre looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("youre voting on question %s" % question_id)