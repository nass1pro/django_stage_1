
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

def acceuille(request):
    que = prof.objects.all()
    template = loader.get_template('questi/acceuille.html')
    context = {'que':que}
    return render(request, 'questi/acceuille.html', context)

def connexion(request):

    template = loader.get_template('questi/connexions.html')
    return render(request, 'questi/connexions.html')

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


def formulair(request):
    template = loader.get_template('questi/formulaire.html')
    return render(request, 'questi/formulaire.html')

def submit(request, questions_id):

    reponsse_juste = 0
    cours_nom = questions.objects.get(pk = questions_id)

    sub = questions.objects.get(pk = questions_id)
    n_cours = sub.nom_du_cours

    d = sub.reference
    pr = questionnaire.objects.get(nom_du_cours = n_cours, reference = d)
    count = pr.questions_set.count()
    i = 1
    while (i <= count):

        questions_id = str(questions_id)

        k = request.POST.get(questions_id)
        sub = questions.objects.get(pk = questions_id)
        j = sub.rep_tru_id

        if (k == 'None'):
                k = 0
        if (k == None):
            k = 0
        if (int(k) == j):
            reponsse_juste += 1

        i += 1

        questions_id = int(questions_id)
        questions_id += 1

    template = loader.get_template('questi/submit.html')
    context = {'reponse_juste': reponsse_juste}
    return render(request, 'questi/submit.html', context)
