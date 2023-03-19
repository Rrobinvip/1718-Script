from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from Config import Config

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

print(" - (P2) Launching the browser..")
# Navigate to YouTube
driver.get(Config.YOUTUBE_VID)

# Wait for the video to load
time.sleep(5)

print(" - (P2) Playing the video and adjusting the quality..")
# Play the video  (To skip ads)
driver.find_element(By.CSS_SELECTOR, ".ytp-play-button").click()
time.sleep(2)

# Open the setting and adjust resolution to 4K
driver.find_element(By.CSS_SELECTOR, value='button.ytp-button.ytp-settings-button').click()
time.sleep(2)

driver.find_element(By.XPATH, value='(//div[@class="ytp-menuitem"])[3]').click()
time.sleep(1)

driver.find_element(By.XPATH, value='(//div[@class="ytp-menuitem"])[1]').click()

# Play the video for 12 minutes.
time.sleep(710)

print(" - (P2) Play finished! Quiting..")
# Close the browser
driver.quit()