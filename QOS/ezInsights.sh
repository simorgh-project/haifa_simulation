#!/bin/sh

while true
do
        com="$(awk '{ total += $1 } END { print total/NR }' QOSlog.txt)"
        echo "${com}" > insight.txt
        sleep 50s
done
