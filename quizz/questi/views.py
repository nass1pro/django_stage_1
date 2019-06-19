
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    form = ConnexionForm()
    template = loader.get_template('questi/index.html')
    context = {'form':form}


    return render(request, 'questi/index.html', context)

def connexion(request):

     error = False

     if request.method == "POST":

            form = ConnexionForm(request.POST)
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                context = {'username':username}
                users_eleve = Group.objects.get(name="eleve").user_set.filter(username = username)
                users_prof = Group.objects.get(name="prof").user_set.filter(username= username)

                if ( len(users_prof) != 0):
                    pro = 0
                    for pro in users_prof:
                        pass


                    us_prof       = prof.objects.get(name = pro)
                    classes_prof  = classe.objects.get(name_classe = us_prof.name_classe)



                    context = {'groupe': classes_prof.id, 'num': 2, 'classe': classes_prof.name_classe}
                    print(context)

                    return render(request, 'questi/profil.html', context)

                elif (len (users_eleve) != 0):
                    ele = 0
                    cour = 0
                    for ele in users_eleve:
                        pass
                    us_eleve = user_elev.objects.get(name = ele)
                    classe_eleves = us_eleve.name_classe


                    cont = {'groupe': classe_eleves.id, 'classe': classe_eleves.name_classe}

                    print(cont)
                    return render(request, 'questi/profil.html', cont)

            else:
                error = True
                return render(request, 'questi/index.html', locals())

@login_required(redirect_field_name='/index/')
def profil(request):

    template = loader.get_template('questi/profil.html')
    return render(request, 'questi/profil.html')

@login_required(redirect_field_name='/index/')
def detail(request, groupe):
    print('ok')
    ques = classe.objects.filter(pk=groupe)
    cour = cours.objects.filter(name_classe =  groupe)
    template = loader.get_template('questi/detail.html')
    cour = {'cour':cour, 'groupe':groupe}
    print(cour)
    print('salut ceee')
    return render(request, 'questi/detail.html', cour)

@login_required(redirect_field_name='/index/')
def detail_questionnaire(request, groupe):
    print(groupe)
    print('salut')
    q = cours.objects.get(name_classe = groupe)
    ques = questionnaire.objects.filter(cours = q.id)
    template = loader.get_template('questi/questionnaire.html')
    print(ques)
    context = {'ques':ques}
    return render(request, 'questi/questionnaire.html', context)

@login_required(redirect_field_name='/index/')
def detail_questions(request, questi_id):

    print (questi_id)
    print('pl')
    quess = questions.objects.filter(questionnaires=questi_id)
    print (quess)
    template = loader.get_template('questi/questions.html')
    context = {'quess':quess}
    return render(request, 'questi/questions.html', context)

@login_required(redirect_field_name='/index/')
def formulair(request):
    template = loader.get_template('questi/formulaire.html')
    return render(request, 'questi/formulaire.html')


@login_required(redirect_field_name='/index/')
def submit(request, questions_id):
    """
    changer prof id avec classe id
    """

    reponsse_juste = 0
    sub = questions.objects.get(pk = questions_id)
    n_cours = sub.nom_du_cours

    d = sub.reference
    pr = questionnaire.objects.get(nom_du_cours = n_cours, reference = d)
    count = pr.questions_set.count()
    print(pr.id)

    c = cours.objects.get(name_cour = pr.cours)
    cl = classe.objects.get(pk = c.id)
    p = prof.objects.get(pk = cl.id)


    print(request.user.username)
    eleve = user_elev.objects.get(name = request.user.username)

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


    score.objects.create(reference = sub.reference, score_champ = reponsse_juste, question = pr.nom_du_cours, s_elevs = eleve, s_prof = p, rep_tru = 10)
    template = loader.get_template('questi/submit.html')
    context = {'reponse_juste': reponsse_juste}
    return render(request, 'questi/submit.html', context)

def deconnexion(request):

    logout(request)
    form = ConnexionForm()
    context = {'form':form}
    template = loader.get_template('questi/index.html')
    return render(request,'questi/index.html', context)
