
def ajout_medicament(cur,conn):
    molecule = input("Entrez le nom de la molécule propre au médicament : ")
    quantite_jour = input("Entrez la quantité de médicament à prendre par jour : ")
    effet = input("Entrez l'effet du médicament : ")

    #Creation de la reqûete sql parametrée pour l'insertion
    sql = "INSERT INTO medicament VALUES (%s, %s, %s)"

    # chaque %s correspond à un paramètre de la requête
    # Exécuter la requête
    # cur.execute() à deux paramètres :
    # le preimer est la requête sql paramètrée
    # le deuxième est un tuple qui contient les valeurs ordonnées des paramètres
    try :
        cur.execute(sql, (molecule, quantite_jour, effet) )

        print("--------Ajout pris en compte--------")
        input("Appuyer sur entrer pour continuer")
        ############# FIN ################
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print ("Erreur, message système : ", e)
