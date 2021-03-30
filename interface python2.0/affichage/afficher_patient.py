def afficher_patient(cur,conn):


	sql = "SELECT * FROM patient ORDER BY nom";
	cur.execute(sql)
	row = cur.fetchone()

	while row:

		print("NUMERO DE DOSSIER :%s  NOM: %s  DATE_NAISS: %s  NUM_PUCE: %s  NUM_PASSEPORT: %s ESPECE: %s \n" % (row [0],row[1], row[2], row[3], row[4], row[5]))
		row = cur.fetchone()

	input("\n\nAppuyez sur entrer pour sortir")
	conn.commit()
