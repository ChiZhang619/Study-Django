
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html',context)   #template 下的文件目录


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request, 'polls/detail.html', {'question':question})


def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
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
    return HttpResponse("Hello, world. dfa61ee5 is the polls index.")


def cookice(request):
    print(request.COOKIES)
    resp = HttpResponse('c is for cookice and that is good enough for me')
    resp.set_cookie('zap',42)
    resp.set_cookie('sakaicar',42, max_age=1000)
    resp.set_cookie('dj4e_cookie', 'dfa61ee5', max_age=1000)
    return resp
