from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
import sys
from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome("chromedriver.exe")

args = sys.argv
loopCount = int(args[1])
url = args[2]

driver.get(url)
xpath = '//*[@id="app"]/main/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/button'
iine_button = driver.find_elements(by=By.XPATH, value=xpath)
driver.execute_script('arguments[0].click();', iine_button)
time.sleep(5)