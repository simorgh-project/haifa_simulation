#!/usr/bin/env bash

cd ~

# add chrome repo
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list

# install dependencies
sudo apt-get update
sudo apt-get install -y google-chrome-stable git python3-pip virtualenv

# make virtualenv
virtualenv -p /usr/bin/python3 env
. env/bin/activate

# install python dependencies
# TODO change with requirements.txt file
pip3 install --upgrade pip
pip3 install selenium
pip3 install scapy
pip3 install --upgrade --ignore-installed urllib3

# clone haifa
mkdir -p NEW_HAIFA
cd NEW_HAIFA
rm -rf haifa_simulation/
git clone https://github.com/haifa-foundation/haifa_simulation.git
cd haifa_simulation/

# python3 ./randomvisit.py --driver "./chromedriver" --file "urls.txt"

# ========================================================

# run ezQOS script
screen -d -m sh QOS/ezQOS.sh 8.8.8.8

# make insight files
touch QOSlog.txt
touch insight.txt

# sleep for some reason Ezz knows
sleep 2s

# run ezInsights
screen -d -m sh QOS/ezInsights.sh 8.8.8.8

# run QoS code in screen
echo "Running QoS script in screen"
screen -d -m sh QOS/main.sh

# run web-server directory
mkdir -p web

# link insight file
test -f web/insight.txt || test -L web/insight.txt || ln -s insight.txt web/insight.txt
cd web

# add hostname and mac
cat /etc/hostname > hostname.txt
echo $(ifconfig br0-int | grep -oE 'HWaddr .*' | grep -oE ' .*' | sed 's/ //g') > mac.txt

# run HTTP server
screen -d -m sh QOS/imServer.sh 8.8.8.8

