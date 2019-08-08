import time
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("https://jqueryui.com/checkboxradio/")

driver.maximize_window()
driver.implicitly_wait(10)

#Iframe
driver.switch_to.frame(driver.find_element_by_css_selector("body.jquery-ui.page.page-id-692.page-template-default.page-slug-checkboxradio.single-author.singular:nth-child(2) div:nth-child(2) div.clearfix.row:nth-child(3) div.content-right.twelve.columns div:nth-child(1) > iframe.demo-frame:nth-child(5)"))

#Radio button
driver.find_element_by_xpath("//label[contains(text(),'New York')]").click()
time.sleep(1)

#Checkbox
driver.find_element_by_xpath("//label[contains(text(),'2 Star')]").click()
time.sleep(1)
driver.find_element_by_xpath("//label[contains(text(),'3 Star')]").click()
time.sleep(1)

