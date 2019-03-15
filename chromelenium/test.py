from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome('./chrome_version_73/mac/chromedriver', chrome_options=chrome_options)  # Optional argument, if not specified will search path.
    driver.get('https://www.google.com')

    # Let the user actually see something!
    # time.sleep(5)

    search_box = driver.find_element_by_name('q')
    search_box.send_keys('Chrome')
    search_box.submit()

    driver.save_screenshot('screenshot.png')

    # Let the user actually see something!
    # time.sleep(5)

    driver.close()
    driver.quit()
