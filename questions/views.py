from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Answer, Question
# Create your views here.
def index(request):
    question_list = Question.objects.all()
    return render(request, 'questions/main.html', {'question_list': question_list})
def save(request):
    s = ""
    for i in range(30):
        id = "answer" + str(i+1)
        print(id)
        s += (request.POST[id])
    print(s)
    a = Answer(
      answer = s
    )
    a.save()
    return HttpResponseRedirect(reverse('questions:index'))
