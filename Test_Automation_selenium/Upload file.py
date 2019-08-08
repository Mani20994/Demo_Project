import time
import os
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(15)

driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("‪E:\\Requirements\\pswd req.docx‪")
time.sleep(5)

driver.find_element_by_id("file-submit").click()
time.sleep(3)