import os, time

import pyautogui

# Define the file path
word_file_path = os.path.relpath("win_scripts/assets/Doc_win.docx")

for i in range(14):
    print(" - (P3) Launching word.., for {} time".format(i+1))
    # Open the file in Word
    os.system("start winword {}".format(word_file_path))

    # Wait for Word to open
    pyautogui.sleep(5)

    print(" - (P3) Start typing..")
    # Type some text using the keyboard (The following runs for 50 seconds)
    for i in range(5):
        pyautogui.typewrite('11111, 11111 12345678', interval=0.5)
        pyautogui.press("enter")
        
    pyautogui.hotkey("ctrl", "a", interval=0.1)

    for i in range(5):
        pyautogui.hotkey("ctrl", "b", interval=0.1)
        time.sleep(1)
        
    pyautogui.hotkey("ctrl", "a", interval=0.1)
    pyautogui.press("delete")
    pyautogui.hotkey("ctrl", "s", interval=0.1)
    pyautogui.hotkey("alt", "f4", interval=0.1)

print(" - (P3) Typing finished! Quiting..")