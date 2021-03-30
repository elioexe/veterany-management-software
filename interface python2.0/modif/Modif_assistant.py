
############ Mise à jour assistant ################
def modif_assitant(cur,conn) :
    entree=input("voulez vous modifier les données d'un assistant ? si oui taper 1 sinon taper 0 :")
    if entree == "1":
         print("------ modification ------")
         id=input("Taper son id : ")
         if id != "0" :
         # Lecture des valeurs
          rep=input("Voulez-vous modifier le nom de l'assistant ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             nom=input("Entrez le nom à modifier : ")
             sql= "UPDATE assistant SET nom= %s WHERE id=%s"
             cur.execute(sql, (nom, id) )


          rep=input("Voulez-vous modifier le prenom de l'assistant ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             prenom=input("Entrez le prenom à modifier : ")
             sql= "UPDATE assistant SET prenom= %s WHERE id=%s"
             cur.execute(sql, (prenom, id) )

          rep=input("Voulez-vous modifier la date de naissance de l'assistant ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             print ("Entrer la date de naissance de l'assistant :")
             erreur = False
             while (not erreur):
                 try:
                     Jour = int(input("    Jour (JJ): "))
                     Mois = int(input("    Mois (MM) : "))
                     Année = int(input("    Année (AAAA): "))
                     erreur = True
                 except:
                     print ("Erreur, veuillez entrer des entiers positifs")
             try :
                 sql= "UPDATE assistant SET date_naissance='%i-%i-%i' WHERE id='%s'"%(Année,Mois,Jour,id)
                 cur.execute(sql)
             except psycopg2.Error as e:
                 conn.rollback()
                 print ("Erreur, message système : ", e)
                 

          rep=input("Voulez-vous modifier l'adresse de l'assistant ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             adresse=input("Entrez l'adresse à modifier : ")
             sql= "UPDATE assistant SET adresse= %s WHERE id=%s"
             cur.execute(sql, (adresse, id) )

          rep=input("Voulez-vous modifier le téléphone de l'assistant ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             telephone=input("Entrez le téléphone à modifier : ")
             sql= "UPDATE assistant SET telephone= %s WHERE id=%s"
             cur.execute(sql, (telephone, id) )

    print("--------Modification prise en compte--------")
    print("Appuyer sur entrer pour continuer")
    ############# FIN ################
    conn.commit()
