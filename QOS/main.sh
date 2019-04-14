#!/bin/sh
sh ezQOS.sh 8.8.8.8 &
touch QOSlog.txt
touch insight.txt
sleep 2s
sh ezInsights.sh &

mkdir -p web
test -f web/insight.txt || ln -s insight.txt web/insight.txt
cd web
cat /etc/hostname > hostname.txt
echo $(ifconfig br0-int | grep -oE 'HWaddr .*' | grep -oE ' .*' | sed 's/ //g') > mac.txt

python -m SimpleHTTPServer 8000 &

