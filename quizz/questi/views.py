
from django.http import HttpResponse
from .models import *
from django.template import loader

# Create your views here.

def index(request):
    print("eee")
    que = prof.objects.all()

    #formatted_albums = ["<li>{}</li>".format(pr_name) for pr_name in que]
    template = loader.get_template('index.html')
    context = {'que':que}
    return HttpResponse(template.render(context,request=request))

def listing(request):
    print ("oeoeoeoeoeo")
    ques = prof.objects.all()
    #formatted_albums = ["<li>{}</li>".format(pr_name) for pr_name in ques]
    template = loader.get_template('liste.html')
    context = {'ques':ques}
    return HttpResponse(template.render(context,request=request))

def detail(request, prof_id):
    print ('mois _ eee')
    ques = questionnaire.objects.filter(profs=prof_id)

    template = loader.get_template('questionnaire.html')
    context = {'ques':ques}
    return HttpResponse(template.render(context,request=request))

def detail_questionnaire(request, prof_id):
    print ('mo')
    ques = questionnaire.objects.get(profs=prof_id)
    template = loader.get_template('questions.html')
    context = {'ques':ques}
    return HttpResponse(template.render(context,request=request))

def detail_questions(request, questionnaire_id):
    print ('moissss')
    quess = questions.objects.get(questionnaires=questionnaire_id)
    template = loader.get_template('questions.html')
    context = {'ques':ques}
    return HttpResponse(template.render(context,request=request))
