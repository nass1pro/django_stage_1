from mago import *
from questi.models import *
from django.contrib.auth.models import User


### donnée user groupe and utilisateur



#profff = prof.objects.create_user(name = name_proff,password = passe, email = email_)

pro = prof.objects.get(name = name_proff)

classe = classe.objects.get(name_prof = prof)
cu = cours.objects.get(name_prof = prof)

###ici !!!!!
questionnair = pro.questionnaire_set.create(reference = refe,nom_du_cours = nom_courr, nom_prof = name_proff,explication = expl)

quest_ref = questionnaire.objects.get(nom_prof = name_proff)

i = 0
j = 0
k = 0
p = 1

while i < len(data):

    vrai = data_q[j][-1]

    if len(data_q[j]) == 3:
        quest_ref.questions_set.create(reference = refe,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1], rep_tru_id= vrai)

    elif len(data_q[j]) > 3:
        quest_ref.questions_set.create(reference = refe,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1],rep_3 = data_q[j][2], rep_tru_id = vrai)

    elif len(data_q[j]) > 4:
        quest_ref.questions_set.create(reference = refe,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1],rep_3 = data_q[j][2],rep_4 = data_q[j][3],rep_tru_id = vrai)


    i += 1
    j += 1
