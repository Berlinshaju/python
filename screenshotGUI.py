import time  # Import time module to format the current time for filenames
import pyautogui  # Import pyautogui module to take screenshots
import os  # Import os module to handle directory creation
import tkinter as tk  # Import tkinter module to create the GUI

def screenshot(fmt="%Y-%m-%d_%H-%M-%S"):
    # Minimize the Tkinter window
    root.withdraw()
    time.sleep(1)  # Wait for the window to be minimized
    # Define the directory where screenshots will be saved
    path = "C:/Users/Administrator/OneDrive/Documents/Screenshots"
    # Create the directory if it doesn't exist
    os.makedirs(path, exist_ok=True)
    # Create the full file name for the screenshot
    name = f"{path}/{time.strftime(fmt)}.png"
    # Take a screenshot and save it to the specified path
    pyautogui.screenshot(name).show()
    # Restore the Tkinter window
    root.deiconify()

# Create the main window of the application
root = tk.Tk()
# Set the title of the main window
root.title("Screenshot Tool")

# Create a button to take a screenshot
tk.Button(root, text="Take Screenshot", command=screenshot).pack(pady=5)
# Create a button to exit the application
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

# Run the Tkinter main loop to keep the application running
root.mainloop()
