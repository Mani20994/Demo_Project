from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("http://wikipedia.org")

driver.maximize_window()
driver.implicitly_wait(10)

element = driver.find_element_by_xpath("//strong[contains(text(),'English')]")
hover = ActionChains(driver).move_to_element(element)
hover.perform()