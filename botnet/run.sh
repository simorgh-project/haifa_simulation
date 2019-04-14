#!/usr/bin/env bash

die() {
    echo "Already running"
    exit 1
}

test -f /tmp/flooder.pid && die

python flooder_icmp.py "$@" &

mkdir -p web
test -L web/stats || ln -s $(pwd)/attack_stats.txt web/stats
cd web
cat /etc/hostname > hostname.txt
echo $(ifconfig br0-int | grep -oE 'HWaddr .*' | grep -oE ' .*' | sed 's/ //g') > mac.txt

echo sleep...
sleep 5

echo PID=$(cat /tmp/flooder.pid) || exit 1

python -m SimpleHTTPServer 8001

