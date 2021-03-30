def afficher_assistant(cur,conn):


	sql = "SELECT * FROM assistant ORDER BY id;"
	cur.execute(sql)
	row = cur.fetchone()

	while row:

		print("NUMERO DE DOSSIER :%s  NOM: %s  PRENOM: %s  DATE DE NAISSANCE: %s  ADRESSE: %s TELEPHONE: %s \n" % (row [0],row[1], row[2], row[3], row[4], row[5]))
		row = cur.fetchone()

	input("\n\nAppuyez sur entrer pour sortir")
	conn.commit()
