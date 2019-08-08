from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
browser.get("https://jqueryui.com/checkboxradio/")
browser.maximize_window()

elm = browser.find_element_by_xpath("//a[contains(text(),'Themes')]")
time.sleep(5)
elm.click()
time.sleep(3)

browser.back()
time.sleep(6)
browser.forward()
