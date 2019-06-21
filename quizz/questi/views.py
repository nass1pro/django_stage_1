
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


@login_required(redirect_field_name='/index/')
def formulair(request):
    c = 0
    classe = prof_class.objects.filter(proff__name = request.user.username)

    for c in classe:
        pass

    cour = cours.objects.filter(name_prof = c.proff.id)
    cl = {'classe':classe,'cour':cour}
    print(cour)
    template = loader.get_template('questi/formulaire.html')
    return render(request, 'questi/formulaire.html', cl)

@login_required(redirect_field_name='/index/')
def sub_questionnaire(request):

    data_q = []
    data = []
    j = 4
    info = 0
    
    cu = cours.objects.get(name_classe = clas.id, name_prof = pro.id)
    clas = classe.objects.get(name_classe = nom_cl)
    pro = prof.objects.get(name = name_proff)
    questionnair = cu.questionnaire_set.create(nom_du_cours = nom_courr, nom_prof = name_proff,explication = expl, reference = refe)
    quest_ref = questionnaire.objects.get(nom_prof = name_proff, reference = refe)

    k=request.POST

    for i in k:
        data.append(i)

    while j < 60:
    #print(request.POST.get(data[j]))

        print(request.POST.get(data[j]))
        j +=1
        print(request.POST.get(data[j]))
        j +=1
        print(request.POST.get(data[j]))
        j +=1
        print(request.POST.get(data[j]))
        j +=1
        print(request.POST.get(data[j]))
        j +=1
        if j < 59:
            print(request.POST.get(data[j]))
            j +=1
            quest_ref.questions_set.create(reference = refe,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1],rep_3 = data_q[j][2],rep_4 = data_q[j][3],rep_tru_id = vrai)


    template = loader.get_template('questi/submit.html')
    return render(request, 'questi/submit.html')

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
                    groupe = []
                    grou = {}
                    for pro in users_prof:
                        pass

                    us_prof       = prof.objects.get(name = pro)
                    cl            = prof_class.objects.filter(proff = us_prof.id)

                    context = {'cl': cl , 'num': 2, 'class': cl, 'group':cl, 'user': us_prof.id, 'utils': username}
                    return render(request, 'questi/profil.html', context)

                elif (len (users_eleve) != 0):
                    ele = 0
                    cour = 0
                    for ele in users_eleve:
                        pass
                    us_eleve = user_elev.objects.get(name = ele)
                    classe_eleves = us_eleve.name_classe


                    cont = {'groupe': classe_eleves.id, 'num': 1,'classe': classe_eleves.name_classe, 'user':us_eleve.id}
                    return render(request, 'questi/profil.html', cont)

            else:
                error = True
                return render(request, 'questi/index.html', locals())

@login_required(redirect_field_name='/index/')
def profil(request):

    template = loader.get_template('questi/profil.html')
    return render(request, 'questi/profil.html')

@login_required(redirect_field_name='/index/')
def detail(request, groupe, nume, users_id):

    if nume == 1:

        ques = classe.objects.filter(pk=groupe)
        cour = cours.objects.filter(name_classe =  groupe)
        template = loader.get_template('questi/detail.html')
        cour = {'cour':cour, 'groupe':groupe, 'num':nume}
        return render(request, 'questi/detail.html', cour)

    if nume == 2:
        print(groupe)
        i = 0
        pro       = score.objects.filter(s_prof = users_id, classe = groupe)
        name_ques = questionnaire.objects.filter(nom_prof = request.user.username)
        print(pro)
        for i in name_ques:
            name = i
        template  = loader.get_template('questi/detail.html')
        sc = {'score':pro, 'num':nume, 'quest': name}
        return render(request, 'questi/detail.html', sc)

@login_required(redirect_field_name='/index/')
def detail_questionnaire(request, cours_id):

    q = cours.objects.get(pk = cours_id)
    ques = questionnaire.objects.filter(cours = q.id)
    template = loader.get_template('questi/questionnaire.html')

    context = {'ques':ques}
    return render(request, 'questi/questionnaire.html', context)

@login_required(redirect_field_name='/index/')
def detail_questions(request, questi_id):

    quess = questions.objects.filter(questionnaires=questi_id)
    template = loader.get_template('questi/questions.html')
    context = {'quess':quess}
    return render(request, 'questi/questions.html', context)

@login_required(redirect_field_name='/index/')
def submit(request, questions_id):


    reponsse_juste = 0
    sub = questions.objects.get(pk = questions_id)
    n_cours = sub.nom_du_cours

    d = sub.reference
    pr = questionnaire.objects.get(nom_du_cours = n_cours, reference = d)
    count = pr.questions_set.count()


    c = cours.objects.get(name_cour = pr.cours)
    cl = classe.objects.get(name_classe = c.name_classe)
    p = prof.objects.get(name = c.name_prof)

    classe_x = classe.objects.get(pk = c.name_classe.id)

    print(request.user.username)
    eleve = user_elev.objects.get(name = request.user.username)
    print(request.POST.get(questions_id))
    i = 1
    while (i <= count):

        questions_id = str(questions_id)
        k = request.POST.get(questions_id)
        print(request.POST.get(questions_id))
        questions_id = int(questions_id)
        #print(k)
        sub = questions.objects.filter(pk = questions_id, questionnaires = pr.id)
        sub = questions.objects.get(pk = questions_id, questionnaires = pr.id)
        j = sub.rep_tru_id

        if (k == 'None'):
            k = 0

        if (k == None):
            k = 0
        if (int(k) == j):
            reponsse_juste += 1

        i += 1

        questions_id = int(questions_id)
        questions_id -= 1


    #score.objects.create(reference = sub.reference, score_champ = reponsse_juste, question = pr.nom_du_cours, s_elevs = eleve, s_prof = p, rep_tru = 10, cours = c, classe = classe_x)
    template = loader.get_template('questi/submit.html')
    context = {'reponse_juste': reponsse_juste}
    return render(request, 'questi/submit.html', context)


def deconnexion(request):

    logout(request)
    form = ConnexionForm()
    context = {'form':form}
    template = loader.get_template('questi/index.html')
    return render(request,'questi/index.html', context)
