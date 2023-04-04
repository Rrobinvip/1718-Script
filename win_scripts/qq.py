import os, time
from Config import Config

import pyautogui

chat_questions = Config.CHAT_QUESTIONS
print(" - (P5) Launching QQ..")
time.sleep(1)
pyautogui.hotkey('win', interval=0.1)
time.sleep(1)
pyautogui.typewrite('qq', interval=0.2)
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)

print(" - (P5) Waiting for QQ to boot..")
pyautogui.click(Config.QQ_INFO['Login'][0], Config.QQ_INFO['Login'][1])
time.sleep(5)

print(" - (P5) Starting conversation.")
pyautogui.hotkey('ctrl', "f", interval=0.1)
pyautogui.typewrite(Config.QQ_INFO['QQ'], interval=0.1)
pyautogui.press('enter')
time.sleep(1)


for i in range(60):
    pyautogui.click(Config.QQ_INFO['Chatbox'][0], Config.QQ_INFO['Chatbox'][1])
    pyautogui.typewrite(chat_questions[i], interval=0.1)
    pyautogui.press('enter')
    time.sleep(12)
    
pyautogui.hotkey('alt', 'f4', interval=0.1)
    