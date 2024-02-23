from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

serchbox = driver.find_element("id",'twotabsearchtextbox')
serchbox.send_keys("iphone 15 pro max")
time.sleep(1)
Find = driver.find_element("xpath",'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
Find.click()
time.sleep(1)