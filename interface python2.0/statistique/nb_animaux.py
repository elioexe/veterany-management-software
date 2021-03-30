def statistiques_animaux(cur,conn):

	tot_feline = 0
	tot_canide = 0
	tot_reptile = 0
	tot_rongeur = 0
	tot_oiseau = 0
	tot_autre = 0
	total = 0

	sql = "SELECT * FROM patient ORDER BY nom";
	cur.execute(sql)
	row = cur.fetchone()

	while row:

		total += 1

		if (row[5] == 'félin'):
			tot_feline += 1
		elif(row[5] == 'canidé'):
			tot_canide += 1
		elif(row[5] == 'reptile'):
			tot_reptile += 1
		elif(row[5] == 'rongeurs'):
			tot_rongeur += 1
		elif(row[5] == 'oiseaux'):
			tot_oiseau += 1
		elif(row[5] == 'autres'):
			tot_autre += 1

		row = cur.fetchone()


	print("\n\nLe nombre total des animaux traités: % i \n - Félins : %i \n - Canidés: %i \n - Reptile: %i \n - Rongeurs: %i \n - Oiseaux: %i \n - Autres: %i \n\n" % (total, int(tot_feline),int(tot_canide), int(tot_reptile), int(tot_rongeur), int(tot_oiseau), int(tot_autre)))
	input("\nAppuyer sur entrer pour sortir")
	conn.commit()
