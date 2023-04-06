import os, time, sys
from Config import Config

import pyautogui


def get_yes_no_input(prompt):
    """
    Asks the user for a Yes/No input, ignoring cases, until a valid input is received.

    Parameters:
    prompt (str): The message displayed to the user asking for input.

    Returns:
    bool: True if the user inputs 'y' or 'yes' (case-insensitive), False if the user inputs 'n' or 'no' (case-insensitive).

    Example:
    user_wants_to_continue = get_yes_no_input("Do you want to continue? ")
    if user_wants_to_continue:
        print("Continuing...")
    else:
        print("Stopping...")
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["y", "yes"]:
            return True
        elif user_input in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'yes' to indicate Yes, or 'n' or 'no' to indicate No.")
            

chat_questions = Config.CHAT_QUESTIONS
print(" - (P5) Launching QQ..")

if get_yes_no_input("Are you inside the chatbox with bot?"):
    pass
else:
    sys.exit(1)
# pyautogui.hotkey('win', interval=0.1)
# time.sleep(1)
# pyautogui.typewrite('qq', interval=0.2)
# time.sleep(1)
# pyautogui.press("enter")
# time.sleep(5)

# print(" - (P5) Waiting for QQ to boot..")
# pyautogui.click(Config.QQ_INFO['Login'][0], Config.QQ_INFO['Login'][1])
# time.sleep(5)

# print(" - (P5) Starting conversation.")
# pyautogui.hotkey('ctrl', "f", interval=0.1)
# pyautogui.typewrite(Config.QQ_INFO['QQ'], interval=0.1)
# pyautogui.press('enter')
# time.sleep(1)

print(" - (P5) A gap for you to focus to the chatbox..")
time.sleep(3)

for i in range(60):
    # pyautogui.click(Config.QQ_INFO['Chatbox'][0], Config.QQ_INFO['Chatbox'][1])
    pyautogui.typewrite(chat_questions[i], interval=0.1)
    pyautogui.press('enter')
    time.sleep(12)
    
pyautogui.hotkey('alt', 'f4', interval=0.1)
    