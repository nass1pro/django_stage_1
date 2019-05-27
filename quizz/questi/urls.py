
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('<int:prof_id>/', views.detail, name='detail'),
    path('<int:questionnaire_id>/', views.detail_questionnaire, name='detail_questionnaire'),
    path('<int:questions_id>/', views.detail_questions, name='detail_questions'),

]
#url(r'^(?P<prof_id>)/$', views.detail,name="detail"),
#url(r'^search/$', views.search, name="search"),
