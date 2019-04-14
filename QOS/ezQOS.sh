#!/bin/sh 


while true
do
        com="$(ping "$1" -c1 | grep 64 | awk 'FNR == 1 {print $7}' | sed -n 's/^time=//p')"
        echo "${com}" >> QOSlog.txt
        sleep 10s
done    
