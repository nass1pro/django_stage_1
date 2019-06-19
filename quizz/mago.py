
#CODING
import random
from questi.models import *


nom_cl = "programmation"

name_proff = "prof_1"

ref = random.randrange(0,100000)
refe = ref
nom_courr = "rés"
nom_pr = name_proff

expl = "réseau"

ques1 = ("Est-ce qu'internet est un réseau informatique ?",)
rep1 = ("Oui","Non","Partiellement", 1)

ques2 = ("Quel est le nom des connecteurs réseau ?",)
rep2 = ( "RJ11" ,"RJ45", "RJ21","VGA", 2)

ques3 = ("Combien de fils peuvent etre cablés dans un câble réseau?",)
rep3 = ("4","6","8","10",2)

ques4 = ("Et combien sont nécessaires pour un débit de 100 Mbs ?",)
rep4   = ("2","4","6","8",2)

ques5 = ("Peut-on relier directement 2 PC avec un cable réseau ?",)
rep5 = ("oui","non"," oui sauf si l'ordinateur n'est pas de la même marque","peut-être",1)

ques6 = ("Dans un cable croisé, quelles sont les paires qui croisent ?",)
rep6 = ("1-2 et 3-6"," 1-3 et 2-6 ","2-4 et 1-3","4-6 et 2-3",2)

ques7 = ("Qu'est-ce qu'un commutateur ?",)
rep7 = ("Un Hub","Un Switch", "Un Routeur","Un Modem",2)

ques8 = ("Certains fabricants proposent de coupler 2 prises réseau 1gb/s pour profiter d'un débit de 2Gb/s",)
rep8 = ("Vrai","Faux", "mais pour les serveurs professionnels uniquement", 1)

ques9 = ("Peut -on relier windows, mac OS et linux sur un même réseau ?",)
rep9 = ("Oui,Non,Oui", "mais uniquement en filaire", "Oui, mais uniquement en Wifi", "Oui,Non,Oui",1)


ques10 = ("Pour faire communiquer 2 PC avec les IP 192.168.0.1 et 172.10.0.23, je dois utiliser",)
rep10 = ("Un modem", "Un routeur","Un switch","Internet",2)

ques11 = ("Peut-on faire démarrer un PC par le réseau ?",)
rep11 = ("Oui","Non","Non", "mais on peut l'arrêter","Oui")

ques12 = ("Pour relier 2 PC en passant par un switch, j'utilise")
rep12 = ("Des cables droits","Des cables croisés","Des cables electriques","Des cables VGA","Des cables droits")

ques13 = ("Qu'est-ce qu'une adresse MAC ?",)
rep13 = ("Un identifiant attribué lors de la connection au reseau", "Un identifiant attribué lors de la fabrication d'une carte réseau","Une adresse IP compatible avec Mac OS","Un protocole réseau","Un identifiant attribué lors de la fabrication d'une carte réseau")

ques14 = ("Quels types d'adresses sont réservées aux réseaux locaux ?")
rep14  = ("88.xxx.xxx.xxx","127.0.0.1","192.168.xxx.xxx","255.255.xxx.xxx", "192.168.xxx.xxx")

ques15 = ("Qu'est-ce qu'une passerelle ?",)
rep15  = ("La liaison directe entre 2 PC","Un PC connecté en Wifi",  "Un equipement par lequel transitent les données","Un modem/routeur", "Un equipement par lequel transitent les données")

ques16 = ("Quel norme IP est la plus utilisée actuellement ?")
rep16 = ("LAN","IPv4","IPv6","WAN","IPv4")

ques17 = ("Peut-on faire un ping vers un site web ?")
rep17 = ("Oui","Non","Oui")

ques18 = ("Quel protocole utilise le port 110 ?")
rep18 = ("IMAP","POP","SMTP","TCP","POP")

ques19 = ("Quel outil permet le partage de données entre unix et windows ?")
rep19 = ("Outlook","Debian", "Samba","Dansguardian","Samba" )

ques20 = ("Comment s'appelle le service qui permet de faire le lien entre une IP et un nom de domaine ?")
rep20 = ("L'arp","Le http","Le dns", "Internet","Le dns")

ques21 = ("De combien de ports de communication dispose en PC ?")
rep21 = ("128","512","1024","65535")

ques22 = ("Et combien sont réservés ?")
rep22 = ("64","256","512","1024","22,""1024")

ques23 = ("Le VPN permet")
rep23 = ("De relier un PC à un reseau distant","De relier 2 réseaux distants","De relier 2 PC distants","Les 3 propositions ci-dessus", "Les 3 propositions ci-dessus")

ques24 = ("Qu'est-ce que le NAT?")
rep24 = ("Un VPN sécurisé","Une connection ultra haut débit (pour les militaires par exemple)","Un espace de stockage réseau,Le transfert d'adresse","Un espace de stockage réseau,Le transfert d'adresse")

ques25 = ("Qu'est-ce que le NAS ?")
rep25 = ("Un VPN sécurisé","Une connection ultra haut débit (pour les militaires par exemple)","Un espace de stockage réseau","Le transfert de ports,Un espace de stockage réseau","Le transfert de ports")



data = (ques1, ques2,ques3,ques4,ques5,ques6,ques7 ,ques8,ques9,ques10)
data_q = (rep1,rep2,rep3,rep4,rep5,rep6,rep7,rep8,rep9,rep10)
