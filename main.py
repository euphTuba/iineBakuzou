import sys
from selenium import webdriver
import time
import pyautogui

args = sys.argv
loopCount = int(args[1])
url = args[2]

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get(url)
time.sleep(1)
pyautogui.moveTo(1557,420)
for i in range(loopCount):
    pyautogui.click()
    time.sleep(1)
    driver.delete_all_cookies()
    driver.refresh()
    time.sleep(5)

