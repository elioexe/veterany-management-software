def consultation (cur,conn) :
    print("La consultation peut commencer")
    print("------------------------------")
    print ("Entrer la date et l'heure de la consultation :")
    erreur = False
    while (not erreur):
        try:
            Jour = int(input("  Jour (JJ): "))
            Mois = int(input("  Mois (MM) : "))
            Année = int(input("  Année (AAAA): "))
            heure =int(input("  Heure (HH):"))
            minute =int(input(" minute (MM):"))
            erreur = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")

    id=int(input("Veuillez entrer l'id du dossier medical :"))
    erreur = False
    while (not erreur):
        sql = "SELECT id FROM dossier_medical"
        cur.execute(sql)
        row = cur.fetchone()
        while row:
            if row[0] == id:
                erreur = True
            row = cur.fetchone()
        if (not erreur):
            id = int(input ("Erreur, veuillez entrer un numéro de dossier existant : "))

    erreur1 =False
    while(not erreur1):
        try :
            poids =int(input("Veuillez entrer le poids du patient (en kg, au kg près) :"))
            erreur1=True
        except :
            print("Erreur, veuillez entrer un entier positif")

    try :
        sql ="INSERT INTO poids(date,valeur,id_dossier_medical) VALUES('%i-%i-%i %i:%i:00','%i','%i')"%(Année, Mois,Jour,heure,minute,poids,id)
        cur.execute(sql)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print("Erreur, message systeme :",e)

    erreur2=False
    while (not erreur2):
        try :
            taille=int(input("Veuillez entrer la taille du patient (en cm) :"))
            erreur2=True
        except :
            print ("Erreur, veuillez entrer un entier positif")

    try :
        sql1="INSERT INTO taille (date,valeur, id_dossier_medical) VALUES('%i-%i-%i %i:%i:00','%i','%i')"%(Année, Mois,Jour,heure,minute,taille,id)
        cur.execute(sql1)
        conn.commit()
    except psycopg2.Error as e :
        conn.rollback()
        print("Erreur, message systeme :",e)

    resultats =input("Veuillez joindre le lien des résultats d'analyse : ")
    try :
        sql3 ="INSERT INTO resultats_analyse(date,lien, id_dossier_medical) VALUES ('%i-%i-%i %i:%i:00','%s','%i') "%(Année, Mois,Jour,heure,minute,resultats,id)
        cur.execute(sql3)
        conn.commit()
    except psycopg2.Error as e :
        conn.rollback()
        print("Erreur, message systeme :",e)


    observation=input("Observation :")
    try :
        sql4 ="INSERT INTO observation_generale(date,description,id_dossier_medical) VALUES ('%i-%i-%i %i:%i:00','%s','%i') "%(Année, Mois,Jour,heure,minute,observation,id)
        cur.execute(sql4)
        conn.commit()
    except psycopg2.Error as e :
        conn.rollback()
        print("Erreur, message systeme :",e)


    procedure=input("Veuillez entrer la procedure que le patient doit suivre :")
    try :
        sql2 ="INSERT INTO procedure(date,description, id_dossier_medical) VALUES   ('%i-%i-%i %i:%i:00','%s','%i')"%(Année, Mois,Jour,heure,minute,procedure,id)
        cur.execute(sql2)
        conn.commit()
    except psycopg2.Error as e :
        conn.rollback()
        print("Erreur, message systeme :",e)

    traitement =input("Traitement :")
    print ("Entrer la date de debut du traitement :")
    erreur3 = False
    while (not erreur3):
        try:
            debJour = int(input("    Jour (JJ): "))
            debMois = int(input("    Mois (MM) : "))
            debAnnée = int(input("    Année (AAAA): "))
            erreur3 = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")


    print ("Entrer la date de fin du traitement :")
    erreur4 = False
    while (not erreur4):
        try:
            finJour = int(input("    Jour (JJ): "))
            finMois = int(input("    Mois (MM) : "))
            finAnnée = int(input("    Année (AAAA): "))
            erreur4 = True
        except:
            print ("Erreur, veuillez entrer des entiers positifs")

    try :
        sql5 ="INSERT INTO traitement(date,nom,debut_traitement,fin_traitement, id_dossier_medical) VALUES ('%i-%i-%i %i:%i:00','%s','%i-%i-%i','%i-%i-%i','%i') "%(Année, Mois,Jour,heure,minute,traitement,debAnnée,debMois,debJour,finAnnée,finMois,finJour,id)
        cur.execute(sql5)
        conn.commit()
    except psycopg2.Error as e :
        conn.rollback()
        print("Erreur, message systeme :",e)

    print("--------Fin de la consultation--------")
    input("Appuyer sur entrer pour continuer")
