#!/bin/sh 


while true
do
        com="$(ping "$1" -c5 | grep 64 | awk 'FNR == 5 {print $7}' | sed -n 's/^time=//p')"
        echo "${com}" >> QOSlog.txt
        sleep 10s
done    
