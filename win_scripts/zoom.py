from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
import time
from Config import Config
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from pyautogui import ImageNotFoundException
import os

assets_file_path ={
    "ChromeCheckBox":os.path.relpath("assets/zoom/ChromeCheckBox.png"),
    "ChromeButton":os.path.relpath("assets/zoom/ChromeButton.png"),
    "ZoomPassWordSection":os.path.relpath("assets/zoom/ZoomPasswordSection.png"),
    "ZoomJoinButton":os.path.relpath("assets/zoom/zoom_join_meeting.png")
}

# options = webdriver.ChromeOptions() 
# options.add_argument("user-data-dir={}".format(Config.CHROME_DEFAULT_PATH))
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

print(" - (P4) Opening zoom meeting link..")
driver.get(Config.ZOOM_INFO['ZoomLink'])
 
# meeting id and passcode
meet_code = Config.ZOOM_INFO['MeetingCode']
passcode = Config.ZOOM_INFO['PassCode']

time.sleep(5)

# Close cookies policy, if any.
try:
    cookies_btn = driver.find_element(By.CLASS_NAME, "onetrust-close-btn-ui")
    cookies_btn.click()
except (NoSuchElementException, ElementClickInterceptedException) as e:
    pass


time.sleep(2)
# finding id text box and sending it our meeting code.
element_box = driver.find_element(By.XPATH, "//input[@id='join-confno']")
time.sleep(1)

element_box.send_keys(meet_code)
 
#waiting for 2 seconds to send the code
time.sleep(2)   
 
#finding the join button and clicking on it
join_btn = driver.find_element(By.XPATH, "//a[@id='btnSubmit']")
join_btn.click()

time.sleep(10)

# print(" - (P4) Looking for Chrome checkbox..")
# try:
#     checkbox = pyautogui.locateCenterOnScreen(assets_file_path['ChromeCheckBox'])
#     print(checkbox)
#     pyautogui.click(checkbox)
#     time.sleep(1)
#     try:
#         print(" - (P4) Checkbox selected, looking for Button")
#         pyautogui.locateCenterOnScreen(assets_file_path['ChromeButton'])
#         pyautogui.click()
#         time.sleep(1)
#     except ImageNotFoundException as e:
#         pass
# except ImageNotFoundException as e:
#     pass


print(" - (P4) Looking for Password Section..")
time.sleep(10)
pyautogui.click(x = Config.ZOOM_INFO['Password'][0], y = Config.ZOOM_INFO['Password'][1], clicks=5, interval=1)
pyautogui.typewrite(passcode, interval=0.1)
time.sleep(2)

print(" - (P4) Looking for join button..")
pyautogui.click(Config.ZOOM_INFO['Join'][0], Config.ZOOM_INFO['Join'][1])

time.sleep(2)

pyautogui.click(Config.ZOOM_INFO['FinalJoin'][0], Config.ZOOM_INFO['FinalJoin'][1])

print(" - (P4) Meeting is live.")
time.sleep(695)

pyautogui.hotkey('command', 'q', interval=0.1)
time.sleep(1)
pyautogui.hotkey('enter')