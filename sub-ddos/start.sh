#!/bin/bash
dest_ip=$1
for ((i=1; i<=5; i ++))  
do  
    python /home/lxc/attack.py $dest_ip &
done  
