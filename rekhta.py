import pyautogui
import time

# Function to check if the screen content contains the trigger
def check_trigger():rekhta.org/ebooks/
    screenshot = pyautogui.screenshot()
    if pyautogui.locateOnScreen('trigger_screenshot.png', screenshot, confidence=0.9) is not None:
        return True
    return False

# Main loop
while True:
    if check_trigger():
        # Click on the specified UI element
        pyautogui.click(341, 1464)
        time.sleep(2)  # Wait for the page to load
        
        # Take a screenshot
        pyautogui.screenshot('screenshot.png')
        
    time.sleep(1)  # Wait before checking again