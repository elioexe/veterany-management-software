
############ Mise à jour client ################
def modif_patient(cur,conn):
    entree=input("voulez vous modifier les données d'un patient ? si oui taper 1 sinon taper 0 :")
    if entree == "1":
         print("------ modification ------")
         id=input("Taper son id : ")
         if id != "0":
         # Lecture des valeurs
          rep=input("Voulez-vous modifier le nom du patient ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             nom=input("Entrez le nom à modifier : ")
             sql= "UPDATE patient SET nom= %s WHERE id=%s"
             cur.execute(sql, (nom, id) )

          rep=input("Voulez-vous modifier l'espèce du patient ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             espece=input("Entrez l'espèce à modifier : ")
             sql= "UPDATE patient SET espece= %s WHERE id=%s"
             cur.execute(sql, (espece, id) )

          rep=input("Voulez-vous modifier la date de naissance du patient ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
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
             try :
                 sql= "UPDATE patient SET date_naissance= '%i-%i-%i' WHERE id='%s'"%(Année,Mois,Jour,id)
                 cur.execute(sql)
             except psycopg2.Error as e:
                 conn.rollback()
                 print ("Erreur, message système : ", e)



          rep=input("Voulez-vous modifier le numéro de puce ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             numero_puce=input("Entrez le numéro de puce à modfier : ")
             sql= "UPDATE patient SET num_puce= %s WHERE id=%s"
             cur.execute(sql, (numero_puce, id) )

          rep=input("Voulez-vous modifier le numéro de passeport du patient ? : si oui taper 1 sinon taper 0 ")
          if rep == "1":
             numero_passeport=input("Entrez le numéro de passeport à modifier : ")
             sql= "UPDATE patient SET num_passeport= %s WHERE id=%s"
             cur.execute(sql, (numero_passeport, id) )

    print("--------Modification prise en compte--------")
    input("Appuyer sur entrer pour continuer")
    ############# FIN ################
    conn.commit()
