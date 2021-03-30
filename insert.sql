INSERT INTO espece VALUES (’canide’);

INSERT INTO patient (nom,date_naissance,nb_puce,num_passeport,espece) VALUES (’coco’,’06-06-2013’,1320,7890,’canide’);
INSERT INTO patient VALUES (’coco’,’06-06-2013’,1320,7890,’canide’);


INSERT INTO client (nom,prenom,date_naissance,adresse,telephone) VALUES (’Guerin’,’François’,’1999-05-17’,’2 rue des Iris 37530 Cangey’,0247304567);

INSERT INTO est_proprietaire_de VALUES (1,1,’1998-06-15’,’2020-04-01’);

INSERT INTO veterinaire_suivi_patient VALUES (1,1,’1998-06-15’,’2020-04-01’);

INSERT INTO assistant (nom, prenom, date_naissance, adresse, telephone) VALUES (’Durand’,’Martin’,’2001-06-07’,’16 rue de Mirabeau 31550 TALENCE’,0678987654);


INSERT INTO veterinaire (nom,prenom,date_naissance,adresse,telephone) VALUES (’Durande’,’Martina’,’2000-06-07’,’34 rue de Mirabeau 33550 Bordeaux’,0678988754);


INSERT INTO specialite_veterinaire  VALUES (‘félin’,1);

INSERT INTO specialite_assistant  VALUES (‘canide’,1);
INSERT INTO specialite_assistant  VALUES (‘félin’,1);

INSERT INTO dossier_medical (patient)  VALUES (1);

INSERT INTO traitement (date, nom, debut_traitement, fin_traitement, id_dossier_medical) VALUES (’2020-04-02 21:11:03’,’rougeolle’,’2020-04-02’,’2020-04-07’,1);


INSERT INTO poids (date, valeur, id_dossier_medical) VALUES (’2020-04-02 21:11:03’,23,1);

INSERT INTO taille (date, valeur, id_dossier_medical) VALUES (’2020-04-02 21:11:03’,23,1);

INSERT INTO resultats_analyse VALUES (’2020-04-02 21:11:03’,’http://blabla’,1);

INSERT INTO observation_generale (date, description, id_dossier_medical, auteurvet, auteurassist) VALUES (’2020-04-02 21:11:03’,’RAS’,1,1,NULL);


INSERT INTO procedure (date, description, id_dossier_medical) VALUES ('2020-04-02  23:02:24','Le patient doit prendre son traitement tous les jours',1);

INSERT INTO prescriptionVeterinaire_dossierMedical VALUES (1,1);

INSERT INTO medicament VALUES (‘paracetamol’,4,’antipyrétique’);

INSERT INTO Composition_Traitement VALUES (1,’paracetamol’);

INSERT INTO medicament_autorise_espece VALUES (‘paracetamol’,’félin’);
