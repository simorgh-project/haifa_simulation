# haifa_simulation


for Orange project ( web browser agents collecting pcaps and ssl) 
```
sudo python3 ./randomvisit.py --driver "./chrome_version_73/linux/chromedriver" --file "urls.txt"
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
