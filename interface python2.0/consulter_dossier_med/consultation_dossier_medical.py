
############# consulter dossier médical ################
def consul_doss_med(cur,conn):
    entree=input("voulez vous accéder au dossier médical d'un patient ? si oui taper 1 sinon taper 0 :")
    if entree == "1":
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
         # Lecture des valeurs
         rep=input("Voulez-vous accéder à sa taille ? : si oui taper 1 sinon taper 0 ")
         try:
             if rep == "1":
                 sql= "SELECT valeur FROM taille WHERE id_dossier_medical=%s"
                 cur.execute(sql,id) #methode 1
                 row=cur.fetchone()
                 print(row[0])

         except:
             print ("Ce dossier médical ne comporte pas de taille")

         rep=input("Voulez-vous accéder à son poids ? : si oui taper 1 sinon taper 0 ")
         try:
            if rep == "1":
                sql= "SELECT valeur FROM poids, dossier_medical WHERE ((poids.id_dossier_medical=%s) AND (dossier_medical.id=%s))"
                cur.execute(sql,(id,id))
                row=cur.fetchone()
                print(row[0])  #methode 2

         except:
            print ("Ce dossier medical ne contient pas de poids")

         rep=input("Voulez-vous accéder à son observation générale ? : si oui taper 1 sinon taper 0 ")
         try:
            if rep == "1":
               sql ="SELECT description FROM observation_generale WHERE id_dossier_medical=%s"
               cur.execute(sql,id)
               row=cur.fetchone()
               print(row[0])

         except:
            print ("Ce dossier medical ne contient pas d'observation general")

         rep=input("Voulez-vous accéder a ses procédures ? : si oui taper 1 sinon taper 0 ")
         try:
             if rep == "1":
                 sql= "SELECT description FROM procedure WHERE id_dossier_medical=%s"
                 cur.execute(sql,id)
                 row=cur.fetchone()
                 print(row[0])

         except:
            print ("Ce dossier medical ne contient pas de procedure")

         rep=input("Voulez-vous accéder aux résultats d'analyse ? : si oui taper 1 sinon taper 0 ")
         try:
             if rep == "1":
                 sql= "SELECT lien FROM resultats_analyse WHERE id_dossier_medical=%s"
                 cur.execute(sql,id)
                 row=cur.fetchone()
                 print(row[0])

         except:
            print ("Ce dossier medical ne contient pas de resultats d'analyse")

         rep=input("Voulez-vous accéder aux traitements ? : si oui taper 1 sinon taper 0 ")
         try:
            if rep == "1":
                sql= "SELECT nom,date FROM traitement WHERE id_dossier_medical=%s"
                cur.execute(sql,id)
                row=cur.fetchone()
                print(row[0])
         except:
            print ("Ce dossier medical ne contient pas de traitement")



    print("------AUREVOIR------")
    input("Appuyer sur entrer pour continuer")
    ############# FIN ################
    conn.commit()
