from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)

driver.get("http://amazon.in")
driver.maximize_window()
driver.implicitly_wait(30)

driver.get_screenshot_as_file("‪‪‪‪C:\\Users\\JC\\Desktop\\image\\amazon.PNG")