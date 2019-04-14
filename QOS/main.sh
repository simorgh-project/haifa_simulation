#!/bin/sh
sh ezQOS.sh 8.8.8.8 &
touch QOSlog.txt
touch insight.txt
sleep 2s
sh ezInsights.sh &

mkdir web
ln -s insight.txt web/insight.txt
cd web
python -m SimpleHTTPServer 8000 &

