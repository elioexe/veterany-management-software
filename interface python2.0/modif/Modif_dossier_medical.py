############ Mise à jour dossier médical ################
def modif_dossier_medical(cur,conn):
    entree=input("voulez vous modifier les données d'un dossier médical d'un patient ? si oui taper 1 sinon taper 0 :")
    if entree == "1":
         print("------ modification ------")
         id=input("Taper l'id d'un patient : ")
         if id != "0" :
         # Lecture des valeurs
          rep=input("Voulez-vous modifier la taille d'un patient ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             valeur=input("Entrez la taille à modifier : ")
             sql= "UPDATE taille  SET valeur= %s WHERE taille.id_dossier_medical=%s"
             cur.execute(sql, (valeur,id))


          rep=input("Voulez-vous modifier le poids du patient ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             poids=input("Entrez le poids à modifier : ")
             sql= "UPDATE poids SET poids= %s WHERE id=%s"
             cur.execute(sql, (poids, id) )

          rep=input("Voulez-vous modifier une procédure de son dossier médical ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             description=input("Entrez une nouvelle description : ")
             sql= "UPDATE procedure SET description= %s WHERE id_dossier_medical=%s"
             cur.execute(sql, (description, id) )

          rep=input("Voulez-vous modifier les résultats d'analyses d'un patient ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             lien=input("Entrez le lien vers les résultats d'analyse : ")
             sql= "UPDATE resultats_analyse SET lien= %s WHERE id_dossier_medical=%s"
             cur.execute(sql, (lien, id) )

          rep=input("Voulez-vous modifier une observation générale du dossier médical ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             description=input("Entrez une nouvelle observation : ")
             sql= "UPDATE observation_generale SET description= %s WHERE id_dossier_medical=%s"
             cur.execute(sql, (description, id) )

    print("--------Modification prise en compte--------")
    input("Appuyer sur entrer pour continuer")
    ############# FIN ################
    conn.commit()
