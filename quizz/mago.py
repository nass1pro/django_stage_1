
#CODING
import random
from questi.models import *




name_proff = "thomas"
passe = "123456789"
email_ = "mago-emi12@mail.ru"

ref = random.randrange(0,100000)
refe = ref
nom_courr = "les histoire de thomas"
nom_pr = name_proff

expl = "historique sur la science et la chimie"


ques1 = ("Comment s'appelle la table de laboratoire sur laquelle le chimiste fait ses expériences ?",)
rep1 = ("Le comptoir","L'établi","La paillasse",3)

ques2 = ("Quel grand physicien, prix Nobel, découvrit la radioactivité ?")
rep2 = ("Henri Becquerel","John Dalton","Frédéric Joliot-Curie",1)

ques3 = ("Quel est le troisième état de la matière les deux premiers étant : solide, liquide?",)
rep3 = ("Air","Émulsion","Gaz",3)

ques4 = ("À quelle température, l'eau se change-t-elle en gaz ?",)
rep4 = ("90°C","100°C","1000°C",2)

ques5 = ("Quels sont les principaux éléments nécessaires à la vie ?",)
rep5 = ("Arsenic, azote hydrogène, oxygène.","Carbone, azote, hydrogène, oxygène, phosphore, soufre.","Hydrogène, oxygène, phosphore, potassium, soufre.",3)

ques6 = ("Qui découvrit la pénicilline ?",)
rep6 = ("Pierre et Marie Curie","Ernest Duchêne","Sir Alexandre Flemming","Sir Alexandre Flemming",)

ques7 = ("Comment s'appelle l'unité d'énergie ?",)
rep7 = ("La calorie","Le dalton","Le joule","Le joule" )

ques8 = ("Pourquoi la Révolution lança-t-elle une campagne de récupération de salpêtre ?",)
rep8 = ("Ajouté au paillis il permet d'améliorer les récoltes","Mélangé avec du charbon et du soufre il permet de fabriquer de la poudre à canon","On en extrait du nitrate de potassium utilisé à l'époque comme anti-infectueux","Mélangé avec du charbon et du soufre il permet de fabriquer de la poudre à canon" )

ques9 = ("Qu'est-ce qu'un neutrino ?",)
rep9 = ("Un atome neutre","Un électron libre","Une particule élémentaire","Une particule élémentaire")

ques10 = ("Automobilistes trop rapides, une question pour vous : Qu'utilisent les radars pour détecter une distance ou un objet et sa vitesse ?",)
rep10 = ("Une antenne bipolaire miniaturisée","Les fréquences radio","Les ondes électromagnétiques","Les ondes électromagnétiques")

ques11 = ("Par quelle théorie, Einstein révolutionna-t-il la physique ?",)
rep11 = ("De l'espace-temps","De l'évolution","De la relativité","De la relativité")

ques12 = ("En 1887, Hertz démontrait l'existence des ondes radioélectriques appelées depuis ondes hertziennes. On en fait divers usages. Quel intrus s'est glissé dans la liste ?",)
rep12 = ("Transmission téléphonique","Transport spatial","Wi-Fi","Transport spatial" )

ques13 = ("Chimiste et philosophe, il identifia l'oxygène. Cependant, il tirait ses revenus de sa charge de fermier général des impôts. Qui a, de ce fait, été guillotiné en 1794 ?",)
rep13 = ("Jean-Baptiste de Lamarck","Antoine-Laurent de Lavoisier","René-Antoine Ferchault de Réaumur","Antoine-Laurent de Lavoisier")


data = (ques1, ques2,ques3,ques4,ques5)
data_q = (rep1,rep2,rep3,rep4,rep5)
