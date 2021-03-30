

############# Ajout veterinaire ################
# Lecture des valeurs
def ajout_veterinaire (cur,conn):
    nom = input("Entrez le nom du vétérinaire : ")
    prenom = input("Entrez le prenom du vétérinaire : ")
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

    adresse = input("Entrez l'adresse du vétérinaire : ")
    telephone = input("Entrez le numéro de téléphone du vétérinaire : ")

    try :
        #Creation de la reqûete sql parametrée pour l'insertion
        sql = "INSERT INTO veterinaire (nom,prenom,date_naissance,adresse, telephone) VALUES ('%s', '%s', '%i-%i-%i', '%s', '%s')"%(nom,prenom,Année,Mois,Jour,adresse,telephone)

        # chaque %s correspond à un paramètre de la requête
        # Exécuter la requête
        # cur.execute() à deux paramètres :
        # le deuxième est un tuple qui contient les valeurs ordonnées des paramètres
        cur.execute(sql )

        print("--------Ajout pris en compte--------")
        input("Appuyer sur entrer pour continuer")
        ############# FIN ################
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)
