
############ Mise à jour client ################
def modif_medicament(cur,conn) :
    entree=input("voulez vous modifier les données d'un médicament ? si oui taper 1 sinon taper 0 :")
    if entree == "1":
         print("------ modification ------")
         molecules=input("Taper sa molécule : ")
         # Lecture des valeurs
         rep=input("Voulez-vous modifier la quantité à prendre par jour de ce médicament ? : si oui taper 1 sinon taper 0 ")
         if rep == "1":
             qte_jour=input("Entrez la quantité à modifier : ")
             sql= "UPDATE medicament SET qte_jour= %s WHERE molecule=%s"
             cur.execute(sql, (qte_jour, molecules) )

         rep=input("Voulez-vous modifier l'effet du médicament ? : si oui taper 1 sinon taper 0 ")
         if rep == "1":
             effet=input("Entrez l'effet à modifier : ")
             sql= "UPDATE medicament SET effet= %s WHERE molecule=%s"
             cur.execute(sql, (effet, molecules) )

    print("--------Modification prise en compte--------")
    input("Appuyer sur entrer pour continuer")
    ############# FIN ################
    conn.commit()
