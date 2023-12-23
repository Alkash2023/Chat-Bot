import pyautogui
import time
time.sleep(1)
pyautogui.moveTo(330,760)
pyautogui.click(button = "left")
pyautogui.moveTo(330,400)
pyautogui.doubleClick(button = "left") 
print(pyautogui.position())
print(pyautogui.size())
