import psycopg2, json, sys



def grab_connection():
	with open('../cred/connections.json') as fn:
		connection_dict = json.load(fn)


def connect_db(connection_name):
	conn = psycopg2.connect(database=connection_dict[connection_name]['database'], 
						host=connection_dict[connection_name]['host'], 
						user=connection_dict[connection_name]['user'], 
						password=connection_dict[connection_name]['password'], 
						port=connection_dict[connection_name]['port'])
	cur = conn.cursor()

def close_connection():
	cur.close()
	conn.close()

#cur.execute("SELECT * FROM loans LIMIT 1;")
#b = cur.fetchone()
#print(b)
