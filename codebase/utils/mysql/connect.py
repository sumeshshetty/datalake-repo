import pymysql
def connect_to_mysql(request_data):

	try:
		# Try to connect MySQL database
		conn = pymysql.connect(
			host=request_data['host'],
			user=request_data['user'],
			password = request_data['password'],
			db= request_data['db'],
			connect_timeout = 5
			)
		
		cur = conn.cursor()

		query1=f'''use {request_data['db']};'''
		cur.execute(query1)
		query2='''  SHOW TABLES;'''
		cur.execute(query2)
		output = cur.fetchall()
		conn.close()
		if not output:
			return  f"Not able to fetch tables in {request_data['db']}", 400

		return 'Conection and validation succeeded !!', 200
		
	except Exception as e:
		print(f"Failed to establish a new connection: {e}")
		return str(e), 400

	
		



