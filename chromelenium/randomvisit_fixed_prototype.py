import argparse
import random
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scapy.all import *
#import threading
from multiprocessing import Process

pkts = []


# Read urls from a txt file
def read_urls(file_path):
    url_list = []
    with open(file_path, "r") as f:
        for line in f:
            url_list.append(line.strip('\n'))
    return url_list




def makecap(x):
   # print ("MAKEE")
    global pkts
    pkts.append(x)
    #print (str(x))

def start_capture(u):
    print ("START")
    sniff(prn=makecap, timeout=20)
    print ("done with sniff")
    stop_capture(u)


def stop_capture(u):
    print ("STOP")
    iter = 500
    if iter == 500:
        print (u)
        re.sub('[^A-Za-z0-9]+','',u)
        print (u)
        pname = "./fml/" + str(url) + "url=" + u[10:19] + "_pcap_%d.pcap" % timestamp
        wrpcap(pname, pkts)
        print ("done = " + str(pname))

def rst_pkts():
    global pkts
    print ("reset packets")
    pkts=[]

def random_visit(_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--ssl-key-log-file=./fml/" + _url + "_ssl_" + str(timestamp))
    driver = webdriver.Chrome(args.driver, options=chrome_options)
    # driver.maximize_window()
    driver.implicitly_wait(5)
    for count in range(10):
        if count == 0:
                t1= Process(target=start_capture, args=(str(driver.current_url),))
                t1.start() 
                time.sleep(2)
                driver.get("http://" + _url)
                time.sleep(5)
                t1.join()
        else:
            print(driver.current_url)

            t1 = Process(target=start_capture, args=(str(driver.current_url),))
            t1.start() 
            time.sleep(10)
            t2 = Process(target=driver.get,args=(driver.current_url,))
#            t1.start() 
            t2.start()

            #start_capture()
            #driver.get(driver.current_url)
            print ("back")
            time.sleep(2)
            t1.join()
            t2.join()
            print ("thats a wrap")
            break 

        next_urls = []

        for link in driver.find_elements_by_xpath("//*[@href]"):
            hyperlink = link.get_attribute('href')
            next_urls.append(hyperlink)

#        if len(next_urls) == 0:
            #break #continue

#        driver.get(random.choice(next_urls))

    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver", required=True, type=str, help="the path of the web driver")
    parser.add_argument("--file", required=True, type=str,
                        help="the path of the file where urls to be visited are stored")

    # Parse the args
    args = parser.parse_args()

    # Create the ssl dir if not exists
    if not os.path.isdir("./ssl"):
        os.mkdir("./ssl")
    if not os.path.isdir("./pcaps"):
        os.mkdir("./pcaps")

    global url
    global timestamp

    # Visit urls from the input file
    urls = read_urls(args.file)
    for url in urls:
        timestamp = int(time.time())
        print(url)
        random_visit(url)
        rst_pkts()
