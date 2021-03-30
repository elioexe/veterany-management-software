def stat_med(cur,conn):

	total = 0

	sql = "SELECT * FROM medicament ORDER BY molecule";
	cur.execute(sql)
	row = cur.fetchone()

	while row:

		total += 1

		row = cur.fetchone()


	print("\n\nLe nombre total de médicaments vendus: % i \n " % (total ))
	input("\nAppuyer sur entrer pour sortir")
	conn.commit()
