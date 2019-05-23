# haifa_simulation


for Orange project ( web browser agents collecting pcaps and ssl) 
```
sudo python3 ./randomvisit.py --driver "./chrome_version_73/linux/chromedriver" --file "urls.txt"
```
if chrome 74 
```
sudo python3 ./randomvisit.py --driver "./chromedriver" --file "urls.txt"
```
and for parts rather than urls 
```
sudo bash start_benign.sh 1 2 3
```



for RBC project 
Benign host ( collects QOS data - visits 8.8.8.8) 
```
sudo sh QOS/main.sh & 
```

Malicious Host ( collects attack stats - attacks 9.9.9.9) 
```
sh run.sh 9.9.9.9 &
```


for ssh behind gateway 
```
ssh -i '~/.ssh/gw' 10.142.15.239
```


install chrome 
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable
```
new machine runs web agent 
```
apt install git 
apt install python3-pip 
pip3 install selenium 
pip3 install scapy 
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable
```
