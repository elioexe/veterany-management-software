CREATE TABLE espece (
nom VARCHAR CHECK (nom='félin' OR nom='canide' OR nom='reptile' OR nom='rongueurs' OR nom='oiseaux' OR nom='autres') PRIMARY KEY
);


CREATE TABLE patient (
id SERIAL PRIMARY KEY,
nom VARCHAR NOT NULL,
date_naissance TIMESTAMP,
nb_puce INTEGER ,
num_passeport INTEGER,
espece VARCHAR REFERENCES espece(nom)
);


CREATE TABLE client (
  id SERIAL PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  date_naissance DATE NOT NULL,
  adresse VARCHAR NOT NULL,
  telephone NUMERIC(10) UNIQUE NOT NULL
);

CREATE TABLE est_proprietaire_de (
proprietaire SERIAL REFERENCES client(id),
patient SERIAL REFERENCES patient(id),
debut_adoption DATE NOT NULL,
fin_adoption DATE NOT NULL,
PRIMARY KEY(proprietaire, patient)
);


CREATE TABLE assistant (
id SERIAL PRIMARY KEY,
nom VARCHAR NOT NULL,
prenom VARCHAR NOT NULL,
date_naissance DATE NOT NULL,
adresse VARCHAR NOT NULL,
telephone NUMERIC(10) UNIQUE NOT NULL
);


CREATE TABLE veterinaire (
id SERIAL PRIMARY KEY,
nom VARCHAR NOT NULL,
prenom VARCHAR NOT NULL,
date_naissance DATE NOT NULL,
adresse VARCHAR NOT NULL,
telephone NUMERIC(10) UNIQUE NOT NULL
);

CREATE TABLE veterinaire_suivi_patient (
veterinaire SERIAL REFERENCES veterinaire(id),
patient SERIAL REFERENCES patient(id),
debut_suivi DATE NOT NULL,
fin_suivi DATE NOT NULL,
PRIMARY KEY(veterinaire, patient)
);

CREATE TABLE specialite_veterinaire (
espece VARCHAR REFERENCES espece(nom),
veterinaire INTEGER REFERENCES veterinaire(id),
PRIMARY KEY(espece, veterinaire)
);

CREATE TABLE specialite_assistant (
espece VARCHAR REFERENCES espece(nom),
assistant INTEGER REFERENCES assistant(id),
PRIMARY KEY(espece, assistant)
);

CREATE TABLE dossier_medical (
id SERIAL PRIMARY KEY,
patient INTEGER REFERENCES patient(id)
);

CREATE TABLE traitement (
id SERIAL PRIMARY KEY,
date TIMESTAMP,
nom VARCHAR NOT NULL,
debut_traitement DATE NOT NULL,
fin_traitement DATE NOT NULL,
id_dossier_medical INTEGER REFERENCES dossier_medical(id)
);


CREATE TABLE poids (
id SERIAL PRIMARY KEY,
date TIMESTAMP,
valeur INTEGER,
id_dossier_medical INTEGER REFERENCES dossier_medical(id)
);

CREATE TABLE taille (
id SERIAL PRIMARY KEY,
date TIMESTAMP,
valeur INTEGER,
id_dossier_medical INTEGER REFERENCES dossier_medical(id)
);

CREATE TABLE resultats_analyse (
id SERIAL PRIMARY KEY,
date TIMESTAMP,
lien VARCHAR UNIQUE NOT NULL,
id_dossier_medical INTEGER REFERENCES dossier_medical(id)
);

CREATE TABLE observation_generale (
id SERIAL PRIMARY KEY,
date TIMESTAMP,
description VARCHAR UNIQUE NOT NULL,
id_dossier_medical INTEGER REFERENCES dossier_medical(id),
auteurvet INTEGER REFERENCES veterinaire(id),
auteurassist INTEGER REFERENCES assistant(id) CHECK (((auteurvet = 0) AND( auteurassist  > 0)) OR ((auteurassist = 0) AND( auteurvet > 0)))
);


CREATE TABLE procedure (
id SERIAL PRIMARY KEY,
 date TIMESTAMP,
description VARCHAR NOT NULL,
id_dossier_medical INTEGER REFERENCES dossier_medical(id)
);

CREATE TABLE prescriptionVeterinaire_dossierMedical (
traitement INTEGER REFERENCES traitement(id),
id INTEGER REFERENCES veterinaire(id),
PRIMARY KEY(traitement, id)
);

CREATE TABLE medicament (
molecule VARCHAR PRIMARY KEY,
qte_jour INTEGER NOT NULL,
effet VARCHAR NOT NULL
);

CREATE TABLE Composition_Traitement (
traitement INTEGER REFERENCES traitement(id),
 molecule VARCHAR REFERENCES medicament(molecule),
PRIMARY KEY(traitement, molecule)
);

CREATE TABLE medicament_autorise_espece(
medicament VARCHAR REFERENCES medicament(molecule),
espece VARCHAR REFERENCES espece(nom),
PRIMARY KEY(medicament, espece)
);
