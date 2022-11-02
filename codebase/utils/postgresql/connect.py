import psycopg2
def connect_to_postgresql(request_data):

	try:
		# Try to connect postgresql database
		conn = psycopg2.connect(
		host="database-postgresql-d1.cfnchajqafaa.ap-south-1.rds.amazonaws.com",
		database="postgres",
		user="postgres",
		password="acc12345",
		port=5418)

		cur = conn.cursor()

		# execute a statement
		
		cur.execute('SELECT version()')

		# display the PostgreSQL database server version
		db_version = cur.fetchone()
		print(db_version)

		# close the communication with the PostgreSQL
		cur.close()
		if not db_version:
			return  f"Not able to fetch tables in", 400

		return 'Conection and validation succeeded !!', 200
				
		
	except Exception as e:
		print(f"Failed to establish a new connection: {e}")
		return str(e), 400

	
		



