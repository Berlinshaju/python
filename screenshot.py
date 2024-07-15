import time
import pyautogui

def screenshot(format="%Y-%m-%d_%H-%M-%S"):
    # Get current time based on the specified format
    current_time = time.strftime(format)
    
    # Define the save path for screenshots
    save_path = "C:/Users/Administrator/OneDrive/Documents/Screenshots"
    
    # Construct the full file path with the current time
    name = "{}/{}.png".format(save_path, current_time)
    
    # Wait for 5 seconds before taking the screenshot
    time.sleep(5)
    
    # Take the screenshot and save it with the constructed name
    img = pyautogui.screenshot(name)
    
    # Show the screenshot (optional)
    img.show()

# Example usage:

# Save with default date-time format (YYYY-MM-DD_HH-MM-SS)
screenshot()

# Save with date only format (YYYY-MM-DD)
# screenshot("%Y-%m-%d")

# # Save with time only format (HH-MM-SS)
# screenshot("%H-%M-%S")

# # Save with day of the week format (Monday, Tuesday, etc.)
# screenshot("%A")

# # Save with month and day format (MM-DD)
# screenshot("%m-%d")
