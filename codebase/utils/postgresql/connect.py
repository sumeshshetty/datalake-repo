import psycopg2


def connect_to_postgresql(request_data):

	try:
		# Try to connect postgresql database
		conn = psycopg2.connect(
		host=request_data['host'],
		database=request_data['db'],
		user=request_data['user'],
		password=request_data['password'],
		port = request_data['port'],
		connect_timeout = 5)

		cur = conn.cursor()

		# execute a statement
		
		cur.execute(f'''SELECT * FROM pg_catalog.pg_tables where schemaname = '{request_data['schema']}' ;''')

		
		result = cur.fetchone()
		
		print(result)
		# close the communication with the PostgreSQL
		cur.close()
		if not result:
			return  f"Not able to fetch tables in {request_data['schema']}", 400

		return 'Conection and validation succeeded !!', 200
				
		
	except Exception as e:
		print(f"Failed to establish a new connection: {e}")
		return str(e), 400



	
		



