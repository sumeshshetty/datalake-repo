import os
import cx_Oracle

def connect_to_oracle(request_data):


	try:
		try:
			libs_dir = os.path.join(os.path.dirname(__file__),'libs/instantclient_19_8')
			cx_Oracle.init_oracle_client(lib_dir=libs_dir)
		except cx_Oracle.ProgrammingError as exception:
			pass
		except Exception as exception2:
			pass
			
		connection = cx_Oracle.connect(
		    user=request_data['user'],
		    password=request_data['password'],
		    dsn=f"{request_data['host']}/{request_data['sid']}")
		
	
		print("Successfully connected to Oracle Database")

		cursor = connection.cursor()

		# Create a table

		query = f"""select * from {request_data['table_name']} where rownum=1"""
		try:
			rows = cursor.execute(query)
		except Exception as e:
			return  f"Not able to fetch tables in {request_data['table_name']}", 400
		for row in rows:
			if row:
				cursor.close()
				connection.close()
				print(row)
				return "Successfully done !!", 200
			else:
				cursor.close()
				connection.close()
				return  f"Not able to fetch tables in {request_data['table_name']}", 400
	except Exception as e:
		print(f"Failed to establish a new connection: {e}")
		return str(e), 400
	
