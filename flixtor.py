from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pync

chrome_options = Options()
# Chrome v75 and lower:
# chrome_options.add_argument("--headless")
# Chrome v 76 and above (v76 released July 30th 2019):
chrome_options.headless = True

driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

driver.get("https://flixtor.to/")
time.sleep(5)

# print(driver.find_element_by_xpath('/html/body/div[3]/div[1]/span').text)

while True:
    print(driver.find_element_by_xpath('/html/body/div[3]/div[1]/span').text)
    if driver.find_element_by_xpath('/html/body/div[3]/div[1]/span').text == 'Welcome to Flixtor':
        pync.notify("You can access Flixtor now")
        break
    driver.refresh()
    time.sleep(20)

driver.close()
driver.quit()
