#!/bin/bash
python table_clear.py
ip_array=("192.168.0.12" "192.168.0.15" "192.168.0.16")
user="root"
dest_ip=("173.26.140.3")
dest_count=${#dest_ip[*]}
i=0

for ip in ${ip_array[*]}
do
     echo $ip
     if [ $i -ge $dest_count ]
     then
	i=$(($i % $dest_count))
     fi
     ssh $user@$ip "/home/lxc/start.sh ${dest_ip[$i]}" &
     i=$(($i + 1))
done
