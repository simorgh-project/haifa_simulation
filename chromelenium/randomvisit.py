import argparse
import random
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scapy.all import *


# Read urls from a txt file
def read_urls(file_path):
    url_list = []
    with open(file_path, "r") as f:
        for line in f:
            url_list.append(line.strip('\n'))
    return url_list


pkts = []
iter = 0
pcapnum = 0


def makecap(x):
    global pkts
    global iter
    global pcapnum
    pkts.append(x)
    iter += 1
    if iter == 500:
        pcapnum += 1
        pname = "./pcaps/" + str(url) + "_pcap_%d.pcap" % timestamp
        wrpcap(pname, pkts)
        pkts = []
        iter = 0


def start_capture():
    global iter
    iter = 0
    while 1:
        sniff(prn=makecap)


def stop_capture():
    global iter
    iter = 500


def random_visit(_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--ssl-key-log-file=./ssl/" + _url + "_ssl_" + str(timestamp))
    driver = webdriver.Chrome(args.driver, options=chrome_options)
    # driver.maximize_window()
    driver.implicitly_wait(5)

    for count in range(10):
        if count == 0:
            driver.get("http://" + _url)
        else:
            print(driver.current_url)
            start_capture()
            driver.get(driver.current_url)
            stop_capture()  # pcap is created and saved

        next_urls = []

        for link in driver.find_elements_by_xpath("//*[@href]"):
            hyperlink = link.get_attribute('href')
            next_urls.append(hyperlink)

        if len(next_urls) == 0:
            continue

        driver.get(random.choice(next_urls))

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
