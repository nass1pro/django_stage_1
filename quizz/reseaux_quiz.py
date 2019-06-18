from questi.models import matiere



ques1 = ("Est-ce qu'internet est un réseau informatique ?",)
rep1 = ("Oui","Non","Partiellement", "oui")

ques2 = ("Quel est le nom des connecteurs réseau ?",)
rep2 = ( "RJ11" ,"RJ45", "RJ21","VGA", "RJ45")

ques3 = ("Combien de fils peuvent etre cablés dans un câble réseau?",)
rep3 = ("4","6","8","10","6")
ques4 = ("Et combien sont nécessaires pour un débit de 100Mb/s ?",)
rep4   = ("2","4","6","8","4")

ques5 = ("Peut-on relier directement 2 PC avec un cable réseau ?",)
rep5 = ("oui","non","oui")

ques6 = ("Dans un cable croisé, quelles sont les paires qui croisent ?")
rep6 = ("1-2 et 3-6"," 1-3 et 2-6 ","2-4 et 1-3","4-6 et 2-3","1-3 et 2-6")

ques7 = ("Qu'est-ce qu'un commutateur ?",)
rep7 = ("Un Hub","V Un Switch", "Un Routeur","Un Modem")

ques8 = ("Certains fabricants proposent de coupler 2 prises réseau 1gb/s pour profiter d'un débit de 2Gb/s",)
rep8 = ("Vrai","Faux", "mais pour les serveurs professionnels uniquement", "vrai")

ques9 = ("Peut -on relier windows, mac OS et linux sur un même réseau ?",)
rep9 = ("Oui,Non,Oui", "mais uniquement en filaire", "Oui, mais uniquement en Wifi", "Oui,Non,Oui")


ques10 = ("Pour faire communiquer 2 PC avec les IP 192.168.0.1 et 172.10.0.23, je dois utiliser",)
rep10 = ("Un modem", "Un routeur","Un switch","Internet","Un routeur")

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





def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)





    #url(r'^$',views.listing, name="listing"),
    """
    def listing(request):
        print ("oeoeoeoeoeo")
        ques = prof.objects.all()
        #formatted_albums = ["<li>{}</li>".format(pr_name) for pr_name in ques]
        template = loader.get_template('liste.html')
        context = {'ques':ques}
        return HttpResponse(template.render(context,request=request))
    """


ques1 = ("Comment s'appelle la table de laboratoire sur laquelle le chimiste fait ses expériences ?",)
rep1 = ("Le comptoir","L'établi","La paillasse",3)

ques2 = ("Quel grand physicien, prix Nobel, découvrit la radioactivité ?",)
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
