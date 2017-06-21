ps -ef|grep attack.py|grep -v grep|cut -c 9-15|xargs kill -9
ps -ef|grep phantomjs|grep -v grep|cut -c 9-15|xargs kill -9
