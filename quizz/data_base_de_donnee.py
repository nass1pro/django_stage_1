from mago import *
from questi.models import *


"""field_values = []
for field in self._meta.get_fields():
    field_values.append(str(getattr(self, field.name, '')))
return ' '.join(field_values)
"""


profff = prof.objects.create(name = name_proff,password = passe, email = email_)

pro = prof.objects.get(name = name_proff)

questionnair = pro.questionnaire_set.create(reference = refe,nom_du_cours = nom_courr, nom_prof = name_proff,explication = expl)

quest_ref = questionnaire.objects.get(nom_prof = name_proff)

i = 0
j = 0
k = 0
p = 1

while i < len(data):

    vrai = data_q[j][-1]

    if len(data_q[j]) == 3:
        q = quest_ref.questions_set.create(reference = 212,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1], rep_tru = vrai)

    elif len(data_q[j]) > 3:
        quest_rep3 = quest_ref.questions_set.create(reference = 212,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1],rep_3 = data_q[j][2], rep_tru = vrai)

    elif len(data_q[j]) > 4:
        quest_rep4 = quest_ref.questions_set.create(reference = 212,nom_du_cours = nom_courr,quest = data[i][0],rep_1 = data_q[j][0],rep_2 = data_q[j][1],rep_3 = data_q[j][2],rep_4 = data_q[j][3],rep_tru = vrai)


    i += 1
    j += 1
