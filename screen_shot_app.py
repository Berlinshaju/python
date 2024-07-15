# open cmd:- pip install virtualenv
# open terminal:- pip install pyautogui
import time
import pyautogui

def screenshot():
    # Get current date and time in a formatted string
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    name = "C:/Users/Administrator/OneDrive/Documents/Screenshots/{}.png".format(current_time)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()

#in different formats to save file:-

'''

current path:

name = "{}.png".format(current_time)

-------------------------------------------------

import time

current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
print(current_time)

--------------------------------------------------

Date Only Format (YYYY-MM-DD):

current_date = time.strftime("%Y-%m-%d")
name = "{}.png".format(current_date)

-----------------------------------------------------
Time Only Format (HH-MM-SS):

current_time = time.strftime("%H-%M-%S")
name = "{}.png".format(current_time)

-----------------------------------------------------
Date and Time Combined (YYYY-MM-DD_HH-MM-SS):

current_datetime = time.strftime("%Y-%m-%d_%H-%M-%S")
name = "{}.png".format(current_datetime)


Day of the Week (Monday, Tuesday, etc.):

current_day = time.strftime("%A")
name = "{}.png".format(current_day)


Month and Day (MM-DD):

current_month_day = time.strftime("%m-%d")
name = "{}.png".format(current_month_day)

'''
