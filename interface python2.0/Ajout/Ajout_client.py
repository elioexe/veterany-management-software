
def ajout_client(cur,conn):
    nom = input("Entrez le nom du client : ")
    prenom = input("Entrez le prenom du client : ")
    print ("Entrer la date de naissance du client :")
    erreur = False
    while (not erreur):
        try:
            Jour = int(input("    Jour (JJ): "))
            Mois = int(input("    Mois (MM) : "))
            Année = int(input("    Année (AAAA): "))
            erreur = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")
    adresse = input("Entrez l'adresse du client : ")
    telephone = input("Entrez le numéro de téléphone du client : ")

    try :
        #Creation de la reqûete sql parametrée pour l'insertion
        sql = "INSERT INTO client(nom,prenom,date_naissance,adresse,telephone) VALUES ('%s', '%s','%i-%i-%i' , '%s', '%s')"%(nom,prenom,Année,Mois,Jour, adresse, telephone)

        # chaque %s correspond à un paramètre de la requête
        # Exécuter la requête
        # cur.execute() à deux paramètres :
        # le preimer est la requête sql paramètrée
        # le deuxième est un tuple qui contient les valeurs ordonnées des paramètres
        cur.execute(sql )

        print("--------Ajout pris en compte--------")
        input("Appuyer sur entrer pour continuer")
        ############# FIN ################
        conn.commit()

    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)
