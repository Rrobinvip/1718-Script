from selenium import webdriver
import time
from Config import Config

# set the number of repetitions
num_repetitions = 12

# set the URL of the webpage you want to scroll
url = Config.WEB_PAGE

# set the duration of the scrolling in seconds
scroll_duration = 60

# create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir={}".format(Config.CHROME_DEFAULT_PATH))
options.add_argument('--disable-gpu')  # disable hardware acceleration
options.add_argument('--disable-accelerated-video-decode')
options.add_argument('--disable-accelerated-mjpeg-decode')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
    
# Keeps the browser open

print(" - (P1) Launching the browser..")


# loop through the specified number of repetitions
for i in range(num_repetitions):

    print(" - (P1) Browsing webpages.. (Setup webpages in Config.py)")
    # navigate to the specified URL
    driver.get(url[i])

    # wait for the page to load
    time.sleep(5)
    
    for j in range(10):
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.refresh()
        time.sleep(5.5)

print(" - (P1) All pages browsed! Quiting..")    
driver.quit()