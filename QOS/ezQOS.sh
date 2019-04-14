#!/bin/bash 

c=0
one=1
five=5
while true
do
        com="$(ping "$1" -c5 | grep 64 | awk 'FNR == 5 {print $7}' | sed -n 's/^time=//p')"
        c=$(($c + $one))
        echo "${com}" >> QOSlog.txt
        sleep 10s
        if [ $c -eq $five ]; then
                echo "${com}" > QOSlog.txt
                c=0
        fi
done
