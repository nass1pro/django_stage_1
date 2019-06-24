
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('profil', views.profil, name='profil'),
    path('connexion', views.connexion, name='connexion'),
    path('<int:groupe>/<int:nume>/<int:users_id>/detail', views.detail, name='detail'),
    path('formulaire', views.formulair, name='formulaire'),
    path('sub_questionnaire', views.sub_questionnaire, name='sub_questionnaire'),
    path('<int:cours_id>/questionnaire', views.detail_questionnaire, name='questionnaire'),
    path('<int:questi_id>/questions', views.detail_questions, name='questions'),
    path('<int:questions_id>/submit',views.submit, name = 'submit'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),

]
