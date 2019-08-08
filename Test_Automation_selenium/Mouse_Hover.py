from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("https://www.amazon.in")

driver.maximize_window()
driver.implicitly_wait(20)

element = driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
time.sleep(9)

hover = ActionChains(driver).move_to_element(element)
time.sleep(9)
hover.perform()