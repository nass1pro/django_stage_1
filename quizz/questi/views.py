
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    print("eee")
    que = prof.objects.all()
    template = loader.get_template('questi/index.html')
    context = {'que':que}
    return render(request, 'questi/index.html', context)


def detail(request, prof_id):
    print ('mois _ eee')
    ques = questionnaire.objects.filter(profs=prof_id)

    template = loader.get_template('questi/questionnaire.html')
    context = {'ques':ques}
    return render(request, 'questi/questionnaire.html', context)

def detail_questionnaire(request, prof_id):
    print ('mo')
    ques = questionnaire.objects.get(profs=prof_id)
    template = loader.get_template('questi/questionnaires.html')
    context = {'ques':ques}
    return render(request, 'questi/questionnaires.html', context)

def detail_questions(request, questionnaire_id):
    print ('moissss')
    quess = questions.objects.get(questionnaires=questionnaire_id)
    template = loader.get_template('questi/questions.html')
    context = {'quess':quess}
    return render(request, 'questi/questions.html', context)
