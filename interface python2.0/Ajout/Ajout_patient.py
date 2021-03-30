

############# Ajout patient ################
# Lecture des valeurs
def ajout_patient (cur,conn):
    nom = input("Entrez le nom du patient (animal) : ")
    espece = input("Entrez son espèce : ")
    print ("Entrer la date de naissance du patient :")
    erreur = False
    while (not erreur):
        try:
            Jour = int(input("    Jour (JJ): "))
            Mois = int(input("    Mois (MM) : "))
            Année = int(input("    Année (AAAA): "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")

    erreur1=False
    while (not erreur1):
        try :
            nb_puce=int(input("Entrez le numéro de puce du patient (entrer 0 si il en a pas): "))
            erreur1= True
        except :
            print("Erreur, veuillez entrer des entiers positifs")
    erreur2=False
    while (not erreur2):
        try :
            num_passeport =int( input("Entrez le numéro de passeport (entrer 0 si il en a pas) : "))
            erreur2=True
        except :
            print("Erreur, veuillez entrer des entiers positifs")

    try :

    #   Creation de la reqûete sql parametrée pour l'insertion
        sql = "INSERT INTO patient (nom,espece,date_naissance,nb_puce,num_passeport) VALUES ('%s', '%s', '%i-%i-%i', %i, %i)"%(nom,espece,Année, Mois, Jour, nb_puce,num_passeport)

        # chaque %s correspond à un paramètre de la requête
    # Exécuter la requête
    # cur.execute() à deux paramètres :
    # le preimer est la requête sql paramètrée
    # le deuxième est un tuple qui contient les valeurs ordonnées des paramètres
        cur.execute(sql)

        print("-------Ajout pris en compte--------")
        input("Appuyer sur entrer pour continuer")
        ############# FIN ################
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)
