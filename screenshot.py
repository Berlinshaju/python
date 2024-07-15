import time
import pyautogui

def screenshot(format="%Y-%m-%d_%H-%M-%S"):
    current_time = time.strftime(format)
    save_path = "C:/Users/Administrator/OneDrive/Documents/Screenshots"
    name = "{}/{}.png".format(save_path, current_time)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

# Example usage:

# Save with default date-time format (YYYY-MM-DD_HH-MM-SS)
screenshot()

# # Save with date only format (YYYY-MM-DD)
# screenshot("%Y-%m-%d")

# # Save with time only format (HH-MM-SS)
# screenshot("%H-%M-%S")

# # Save with day of the week format (Monday, Tuesday, etc.)
# screenshot("%A")

# # Save with month and day format (MM-DD)
# screenshot("%m-%d")
