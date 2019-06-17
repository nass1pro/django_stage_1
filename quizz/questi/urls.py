
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('profil', views.profil, name='profil'),
    path('connexion', views.connexion, name='connexion'),
    path('<int:groupe>/detail', views.detail, name='detail'),
    path('formulaire', views.formulair, name='formulaire'),

    path('questionnaire', views.detail_questionnaire, name='questionnaire'),
    path('<int:questionnaire_id>/questions', views.detail_questions, name='detail_questions'),
    path('<int:questions_id>/submit',views.submit, name = 'submit'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),

]
