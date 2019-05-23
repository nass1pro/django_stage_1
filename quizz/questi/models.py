from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
eleve_cour = rajouter un champ reference pour recuperer
le score
"""

ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]

class prof(models.Model):
    name = models.CharField(max_length=200, unique=False)
    password = models.CharField(max_length=200, unique=False)
    email = models.EmailField(max_length = 70, unique= False)
    def __str__(self):
        return self.name

class questionnaire(models.Model):
    reference       = models.IntegerField(null=True)
    nom_du_cours    = models.CharField(max_length=200)
    nom_prof        = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    available       = models.BooleanField(default=True)
    explication     = models.CharField(max_length=200)
    profs           = models.ForeignKey(prof, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_du_cours

class questions(models.Model):
    reference      = models.IntegerField(null=True)
    nom_du_cours   = models.CharField(max_length=200)
    created_at     = models.DateTimeField(auto_now_add=True)
    quest          = models.CharField(max_length=40000)
    rep_tru        = models.CharField(max_length=40000)
    rep_1          = models.CharField(max_length=40000)
    rep_2          = models.CharField(max_length=40000)
    rep_3          = models.CharField(max_length=40000)
    rep_4          = models.CharField(max_length=40000)
    questionnaires = models.ForeignKey(questionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.quest

class user_elev(models.Model):
    reference      = models.IntegerField(null=True)
    name           = models.CharField(max_length=200, unique=True)
    password       = models.CharField(max_length=200, unique=False)
    email          = models.EmailField(max_length = 100, unique= False)

    def __str__(self):
        return self.name


class elev_cour(models.Model):
    prof_name      = models.CharField(max_length=200, unique=True)
    nom_cour       = models.CharField(max_length=200, unique=False)
    nom_elev       = models.CharField(max_length = 200, unique= False)
    explication    = models.CharField(max_length=40000)
    user_elevs     = models.ForeignKey(user_elev, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom_cour

class elev_question(models.Model):
    reference      =  models.IntegerField(null=True)
    nom_du_cours   =  models.CharField(max_length=200)
    created_at     =  models.DateTimeField(auto_now_add=True)
    quest          =  models.CharField(max_length=40000)
    rep_t          =  models.BooleanField(default=False)
    rep_f          =  models.BooleanField(default=False)
    rep_t_2        =  models.BooleanField(default=False)
    rep_t_3        =  models.BooleanField(default=False)
    cours          =  models.ForeignKey(elev_cour, on_delete= models.CASCADE)

    def __str__(self):
        return self.quest

class score (models.Model):
    reference       = models.IntegerField(null=True)
    score_champ     = models.IntegerField(null=True)
    question        = models.CharField(max_length=40000)
    rep_tru         = models.IntegerField(null= False)
    s_elevs         = models.ForeignKey(user_elev, on_delete= models.CASCADE)
    s_cour_elevs    = models.ForeignKey(elev_cour, on_delete= models.CASCADE)
