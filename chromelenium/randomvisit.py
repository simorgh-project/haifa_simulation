import argparse
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Read urls from a txt file
def read_urls(file_path):
    url_list = []
    with open(file_path, "r") as f:
        for line in f:
            url_list.append(line.strip('\n'))
    return url_list


def random_visit(url):
    for count in range(10):
        driver.get("http://"+url)
        next_urls = []

        for link in driver.find_elements_by_xpath("//*[@href]"):
            next_urls.append(link.get_attribute('href'))

        driver.get(random.choice(next_urls))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver", required=True, type=str, help="the path of the web driver")
    parser.add_argument("--file", required=True, type=str, help="the path of the file where urls to be visited are stored")

    # Parse the args
    args = parser.parse_args()

    urls = read_urls(args.file)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(args.driver, options=chrome_options)
    # driver.maximize_window()
    driver.implicitly_wait(5)

    for url in urls:
        random_visit(url)

    driver.quit()
