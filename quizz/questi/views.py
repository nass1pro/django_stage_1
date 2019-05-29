
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    que = prof.objects.all()
    template = loader.get_template('questi/index.html')
    context = {'que':que}
    return render(request, 'questi/index.html', context)


def detail(request, prof_id):

    ques = questionnaire.objects.filter(profs=prof_id)
    template = loader.get_template('questi/questionnaire.html')
    context = {'ques':ques}
    return render(request, 'questi/questionnaire.html', context)

def detail_questionnaire(request, questionnaire_id):

    ques = questions.objects.get(pk=questionnaire_id)
    template = loader.get_template('questi/questionnaire.html')
    context = {'ques':ques}
    return render(request, 'questi/questionnaire.html', context)

def detail_questions(request, questionnaire_id):

    quess = questions.objects.filter(questionnaires=questionnaire_id)
    template = loader.get_template('questi/questions.html')
    context = {'quess':quess}
    return render(request, 'questi/questions.html', context)

def submit(request):
    v = questions.objects.get(pk = 25)
    
    va = '25'

    k = request.POST.get(va)
    j = v.rep_tru_id
    print(k)
    if (int(k) == j):
        print('quel')
        return HttpResponse(request.POST['25'])
    else:
        message = 'non'
        return HttpResponse(message)
