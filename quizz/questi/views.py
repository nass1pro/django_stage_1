
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.shortcuts import render
from django.template.loader import render_to_string

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


def submit(request, questions_id):
    print('mois')
    reponsse_juste = 0
    cours_nom = questions.objects.get(pk = questions_id)
    print(cours_nom)

    v = questions.objects.get(pk = questions_id)
    j = v.nom_du_cours
    pr = questionnaire.objects.get(nom_du_cours = j)
    count = pr.questions_set.count()
    i = 0
    while (i < count):

        questions_id = str(questions_id)
        k = request.POST.get(questions_id)
        print(k)
        j = v.rep_tru_id
        if (int(k) == j):
            reponsse_juste += 1
        i += 1
        questions_id = int(questions_id)
        questions_id -= 1

    template = loader.get_template('questi/submit.html')
    contexte = {'reponsse_juste':reponsse_juste}

    return render(request, 'questi/submit.html', contexte)
