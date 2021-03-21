from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from notifypy import Notify

# headless flag
chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome('./chromedriver', options=chrome_options)

driver.get("https://flixtor.to/")
time.sleep(5)


while True:
    if driver.find_element_by_xpath('/html/body/div[3]/div[1]/span').text == 'Welcome to Flixtor':
        notification = Notify()
        notification.title = "FlixTor"
        notification.message = "You can access FlixTor now"
        notification.send()
        break
    driver.refresh()
    time.sleep(20)

driver.close()
driver.quit()
