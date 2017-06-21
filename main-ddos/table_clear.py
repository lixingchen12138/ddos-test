import MySQLdb

conn = MySQLdb.connect(host="10.0.3.11",user="nova",passwd="nova",db="nova_api")
cursor = conn.cursor()

sql = "delete from ddos_count"
cursor.execute(sql)
conn.commit()


conn.close()
