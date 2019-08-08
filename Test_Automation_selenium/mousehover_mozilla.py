from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("http://www.thetestingworld.com/")

driver.maximize_window()
time.sleep(1)

driver.find_element_by_xpath(".//*[@id='menu576']").click()
time.sleep(1)

driver.find_element_by_xpath(".//*[@id='menu628']/span").click()
time.sleep(2)

