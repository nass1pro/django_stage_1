
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('connexion', views.connexion, name='connexion'),
    path('acceuille', views.acceuille, name='acceuille'),
    path('formulaire', views.formulair, name='formulaire'),
    path('<int:prof_id>/', views.detail, name='detail'),
    path('<int:questionnaire_id>/questionnaire/', views.detail_questionnaire, name='detail_questionnaire'),
    path('<int:questionnaire_id>/questions', views.detail_questions, name='detail_questions'),
    path('<int:questions_id>/submit',views.submit, name = 'submit'),
]
