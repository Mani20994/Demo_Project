from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver= webdriver.Firefox(capabilities=cap, executable_path="C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\geckodriver.exe" )

driver.get("http://google.com/")

