############ Mise à jour vétérinaire ################
def modif_veterinaire (cur,conn) :
    entree=input("voulez vous modifier les données d'un vétérinaire ? si oui taper 1 sinon taper 0 :")
    if entree == "1":
     print("------ modification ------")
     id=input("Taper son id : ")
     if id != "0":
     # Lecture des valeurs
      rep=input("Voulez-vous modifier le nom du vétérinaire ? : si oui taper 1 sinon taper 0 ")
      if rep == "1":
         nom=input("Entrez le nom à modifier : ")
         sql= "UPDATE veterinaire SET nom= %s WHERE id=%s"
         cur.execute(sql, (nom, id) )

      rep=input("Voulez-vous modifier le prenom du vétérinaire ? : si oui taper 1 sinon taper 0 ")
      if rep == "1":
         prenom=input("Entrez le prenom à modifier : ")
         sql= "UPDATE veterinaire SET prenom= %s WHERE id=%s"
         cur.execute(sql, (prenom, id) )

      rep=input("Voulez-vous modifier la date de naissance du vétérinaire ? : si oui taper 1 sinon taper 0 ")
      if rep == "1":
         print ("Entrer la date de naissance du veterinaire :")
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
             sql= "UPDATE veterinaire SET date_naissance= '%i-%i-%i' WHERE id='%s'"%(Année, Mois,Jour,id)
             cur.execute(sql )
         except psycopg2.Error as e:
             conn.rollback()
             print ("Erreur, message système : ", e)

      rep=input("Voulez-vous modifier l'adresse du vétérinaire ? : si oui taper 1 sinon taper 0 ")
      if rep == "1":
         adresse=input("Entrez l'adresse à modifier : ")
         sql= "UPDATE veterinaire SET adresse= %s WHERE id=%s"
         cur.execute(sql, (adresse, id) )

      rep=input("Voulez-vous modifier le téléphone du vétérinaire ? : si oui taper 1 sinon taper 0 ")
      if rep == "1":
         try :
             telephone=input("Entrez le téléphone à modifier : ")
             sql= "UPDATE veterinaire SET telephone= %s WHERE id=%s"
             cur.execute(sql, (telephone, id) )
         except :
            print("Erreur, le numero n'est pas valable")



    print("--------modification prise en compte--------")
    input("appuyer sur entrer pour continuer")
         ############# FIN ################
    conn.commit()
