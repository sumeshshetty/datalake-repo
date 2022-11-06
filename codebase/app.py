from flask import Flask, request
from utils.mysql.connect import connect_to_mysql
from utils.postgresql.connect import connect_to_postgresql
from utils.oracle.connect import connect_to_oracle




app = Flask(__name__)



@app.route('/connect/mysql')
def mysql_connector():
	request_body = request.json 
	
	print ("Connecting to MySQL")
	response = connect_to_mysql(request_body)
	return response

@app.route('/connect/postgresql')
def postgresql_connector():
	request_body = request.json 
	
	print ("Connecting to PostGreSQL")
	response = connect_to_postgresql(request_body)
	return response

@app.route('/connect/oracle')
def oracle_connector():
	request_body = request.json 
	
	print ("Connecting to Oracle")
	response = connect_to_oracle(request_body)
	return response
	

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug = True)


