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

# run QoS code in screen
# python3 ./randomvisit.py --driver "./chromedriver" --file "urls.txt"

echo "Running QoS script in screen"
screen -d -m sh QOS/main.sh

