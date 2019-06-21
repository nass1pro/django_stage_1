from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class classe(models.Model):

    name_classe     = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return self.name_classe

class prof(models.Model):

    user           = models.OneToOneField(User, on_delete= models.CASCADE, default= False)
    name           = models.CharField(max_length=200, unique=False)
    password       = models.CharField(max_length=200, unique=False)
    email          = models.EmailField(max_length = 70, unique= False)
    name_classe    = models.ForeignKey(classe, on_delete=models.CASCADE,default= False)

    def __str__(self):
        return self.name
class prof_class(models.Model):

    proff         = models.ForeignKey(prof,on_delete=models.CASCADE,default= False)
    classe        = models.ForeignKey(classe,on_delete=models.CASCADE,default= False)


class cours(models.Model):

    name_cour       = models.CharField(max_length=200, unique=False)
    name_classe     = models.ForeignKey(classe, on_delete=models.CASCADE,default= False)
    name_prof       = models.ForeignKey(prof, on_delete=models.CASCADE,default= False)
    def __str__(self):
        return self.name_cour

class questionnaire(models.Model):

    reference       = models.IntegerField(null=True)
    nom_du_cours    = models.CharField(max_length=200)
    nom_prof        = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    available       = models.BooleanField(default=True)
    explication     = models.CharField(max_length=200)
    cours           = models.ForeignKey(cours, on_delete=models.CASCADE, default= False)
    def __str__(self):
        return self.nom_du_cours


class questions(models.Model):

    reference      = models.IntegerField(null=True)
    nom_du_cours   = models.CharField(max_length=200)
    created_at     = models.DateTimeField(auto_now_add=True)
    quest          = models.CharField('la question',max_length=40000)
    rep_tru        = models.CharField(max_length=40000)
    rep_1          = models.CharField('reponse 1',max_length=40000)
    rep_2          = models.CharField('reponse 2',max_length=40000)
    rep_3          = models.CharField('reponse 3',max_length=40000)
    rep_4          = models.CharField('reponse 4',max_length=40000)
    rep_tru_id     = models.IntegerField('indiquer le numero de la reponse juste',null=True)
    questionnaires = models.ForeignKey(questionnaire, on_delete=models.CASCADE, default= False)

    def __str__(self):
        return self.quest


class user_elev(models.Model):

    user           = models.OneToOneField(User, on_delete= models.CASCADE, default= False)
    reference      = models.IntegerField(null=True)
    name           = models.CharField(max_length=200, unique=True)
    password       = models.CharField(max_length=200, unique=False)
    email          = models.EmailField(max_length = 100, unique= False)
    name_classe    = models.ForeignKey(classe, on_delete=models.CASCADE, default= False)

    def __str__(self):
        return self.name


class score (models.Model):
    reference       = models.IntegerField(null=True)
    score_champ     = models.IntegerField(null=True)
    question        = models.CharField(max_length=40000)
    rep_tru         = models.IntegerField(null= False)
    s_elevs         = models.ForeignKey(user_elev, on_delete= models.CASCADE, default= False)
    s_prof          = models.ForeignKey(prof, on_delete= models.CASCADE, default= False)
    cours           = models.ForeignKey(cours, on_delete= models.CASCADE, default= 0)
    classe          = models.ForeignKey(classe, on_delete= models.CASCADE, default= 0)

    def __str__(self):
        return self.question
