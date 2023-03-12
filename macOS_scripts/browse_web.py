from selenium import webdriver
import time
from Config import Config

# set the number of repetitions
num_repetitions = 12

# set the URL of the webpage you want to scroll
url = Config.WEB_PAGE

# set the duration of the scrolling in seconds
scroll_duration = 5

# create a new instance of the Chrome driver
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions() 
    
# Keeps the browser open
chrome_options.add_experimental_option("detach", True)

print(" - (P1) Launching the browser..")


# loop through the specified number of repetitions
for i in range(num_repetitions):

    print(" - (P1) Browsing webpages.. (Setup webpages in Config.py)")
    # navigate to the specified URL
    driver.get(url[i])

    # wait for the page to load
    time.sleep(5)
    
    # scroll the page for the specified duration
    end_time = time.time() + scroll_duration
    while time.time() < end_time:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

print(" - (P1) All pages browsed! Quiting..")    
driver.quit()