#!/usr/bin/python3

import psycopg2
import os
import Ajout.Ajout_vet
import Ajout.Ajout_assistant
import Ajout.Ajout_patient
import Ajout.Ajout_medicament
import Ajout.Ajout_client
import modif.Modif_veterinaire
import modif.Modif_assistant
import modif.Modif_client
import modif.Modif_patient
import modif.Modif_medicament
import modif.Modif_dossier_medical
import consulter_dossier_med.consultation_dossier_medical
import Consultation.consultation
import statistique.nb_animaux
import statistique.nb_med
import affichage.afficher_patient
import affichage.afficher_veterinaire
import affichage.afficher_assistant
import affichage.afficher_client
#variable de connection
host ="localhost"
user="evangoet"
password="CHICAGO19"
DATABASE="clinique_veto"

#connection a la base de données
try :
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (host, DATABASE, user, password))
except :
    print("Erreur de connexion a la base de connexion")

#ouvrir curseur
cur = conn.cursor()
choix=-1
menu_lance=True
while menu_lance :
    os.system('clear')
    print ("Bienvenue dans le logiciel de gestion de la clinique")
    print("\n")
    print("----------------------------------------------------")
    print ("----------------------Menu-------------------------")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("\n")
    print("Afficher personnel, client et patient                taper 1")
    print("Ajouter personnel,client,animaux ou medicament       taper 2")
    print("mettre a jour les données                            taper 3")
    print("Effectuer une consultation                           taper 4")
    print("Consulter le dossier médicale d'un patient           taper 5")
    print("Informations statistiques                            taper 6")
    print("\n")
    print("----------------------------------------------------")
    print("\n")
    print("quitter                                              taper 0")
    choix= input()
    #choix=int(choix)
    if choix == "0" :
        menu_lance=False

    elif choix == "1" :
        os.system('clear')
        print("\n\n\n")
        print("Afficher les vétérinaires                        taper 1")
        print("Afficher les assistants                          taper 2")
        print("Afficher les clients                             taper 3")
        print("Afficher les patients                            taper 4")
        print("\n" )
        print("retour                                           taper 0")
        choix1=input()
        if choix1 =="1":
            os.system('clear')
            affichage.afficher_veterinaire.afficher_veterinaire(cur,conn)
            continue
        if choix1=="2" :
            os.system('clear')
            affichage.afficher_assistant.afficher_assistant(cur,conn)
            continue
        if choix1=="3":
            os.system('clear')
            affichage.afficher_client.afficher_client(cur,conn)
            continue

        if choix1=="4" :
            os.system('clear')
            affichage.afficher_patient.afficher_patient(cur,conn)
            continue



    elif choix =="2" :
        os.system('clear')
        print("\n\n\n")
        print("Ajouter veterinaire                              taper 1")
        print("Ajouter assistant                                taper 2")
        print("Ajouter client                                   taper 3")
        print("Ajouter patient                                  taper 4")
        print("Ajouter medicament                               taper 5")
        print("\n")
        print("Retour                                           taper 0")
        choix2 =input()
        #choix2=int(choix2)
        if choix2 =="0" :
            continue
        if choix2 == "1" :
            os.system('clear')
            Ajout.Ajout_vet.ajout_veterinaire(cur,conn)
            continue
        if choix2 == "2" :
            os.system('clear')
            Ajout.Ajout_assistant.ajout_assistant(cur,conn)
            continue
        if choix2 == "3":
            os.system('clear')
            Ajout.Ajout_client.ajout_client(cur,conn)
            continue
        if choix2 == "4" :
            os.system('clear')
            Ajout.Ajout_patient.ajout_patient(cur,conn)
            continue
        if choix2== "5" :
            os.system('clear')
            Ajout.Ajout_medicament.ajout_medicament(cur,conn)
        else:
            pass


    elif choix == "3" :
        os.system('clear')
        print("\n\n\n")
        print("Modifier les informations d'un veterinaire       taper 1")
        print("Modifier les informations d'un assitant          taper 2")
        print("Modifier les informations d'un client            taper 3")
        print("Modifier les informations d'un patient           taper 4")
        print("Modifier les informations d'un medicament        taper 5")
        print("Modifier les informations d'un dossier medical   taper 6")
        print("\n")
        print("retour                                           taper 0")
        choix3=input()
        #choix3 =int(choix3)
        if choix3 =="0" :
            continue
        if choix3 == "1" :
            os.system('clear')
            modif.Modif_veterinaire.modif_veterinaire(cur,conn)
            continue
        if choix3 == "2" :
            os.system('clear')
            modif.Modif_assistant.modif_assitant(cur,conn)
            continue
        if choix3 == "3":
            os.system('clear')
            modif.Modif_client.modif_client(cur,conn)
            continue
        if choix3 == "4" :
            os.system('clear')
            modif.Modif_patient.modif_patient(cur,conn)
            continue
        if choix3== "5" :
            os.system('clear')
            modif.Modif_medicament.modif_medicament(cur,conn)
            continue
        if choix3=="6" :
            os.system('clear')
            modif.Modif_dossier_medical.modif_dossier_medical(cur,conn)
            continue
        else:
            pass

    elif choix =='4' :
        os.system('clear')
        Consultation.consultation.consultation(cur,conn)
        continue

    elif choix == "5" :
        os.system('clear')
        consulter_dossier_med.consultation_dossier_medical.consul_doss_med(cur,conn)
        continue


    elif choix == "6" :
        os.system('clear')
        print("\n\n\n")
        print("Connaitre le nombre total d'animaux traités       taper 1")
        print("Connaitre le nombre de médicaments vendus         taper 2")
        print("\n")
        print("retour                                            taper 0")

        choix4=input()
        if choix4=="1" :
            os.system('clear')
            statistique.nb_animaux.statistiques_animaux(cur,conn)
            continue
        if choix4 =="2":
            os.system('clear')
            statistique.nb_med.stat_med(cur,conn)
            continue

    else :
        print("erreur")
conn.close()
os.system('clear')
