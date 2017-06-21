#!/bin/bash
ip_array=("192.168.0.12" "192.168.0.15" "192.168.0.16")
user="root"

for ip in ${ip_array[*]}
do
     echo $ip
     ssh $user@$ip "/home/lxc/stop.sh"
done
