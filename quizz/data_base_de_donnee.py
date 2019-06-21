from mago import *
from questi.models import *
from django.contrib.auth.models import User




clas = classe.objects.get(name_classe = nom_cl)
pro = prof.objects.get(name = name_proff)


cu = cours.objects.get(name_classe = clas.id, name_prof = pro.id)


questionnair = cu.questionnaire_set.create(nom_du_cours = nom_courr, nom_prof = name_proff,explication = expl, reference = refe)

quest_ref = questionnaire.objects.get(nom_prof = name_proff, reference = refe)


i = 0
j = 0
k = 0
p = 1

while i < len(data):

    vrai = data_q[j][-1]

    if len(data_q[j]) == 3:
        quest_ref.questions_set.create(reference = refe,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1], rep_tru_id= vrai)
        print(1)
    elif len(data_q[j]) == 4:
        quest_ref.questions_set.create(reference = refe,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1],rep_3 = data_q[j][2], rep_tru_id = vrai)
        print(2)
    elif len(data_q[j]) == 5:
        quest_ref.questions_set.create(reference = refe,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1],rep_3 = data_q[j][2],rep_4 = data_q[j][3],rep_tru_id = vrai)
        print(3)

    i += 1
    j += 1
