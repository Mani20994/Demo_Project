from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

driver.maximize_window()
time.sleep(4)

#Register
driver.find_element_by_xpath("//a[contains(text(),'REGISTER')]").click()
time.sleep(2)

#First name
driver.find_element_by_xpath("//input[@name='firstName']").send_keys("Tina")
time.sleep(1)

#Last name
driver.find_element_by_xpath("//input[@name='lastName']").send_keys("Reema")
time.sleep(1)

#Phone number
driver.find_element_by_xpath("//input[@name='phone']").send_keys("4567891234")
time.sleep(1)

#Email id
driver.find_element_by_xpath("//input[@id='userName']").send_keys("tina123@gmail.com")
time.sleep(1)

#Address
driver.find_element_by_xpath("//input[@name='address1']").send_keys("Opp High Court")
time.sleep(1)

#city
driver.find_element_by_xpath("//input[@name='city']").send_keys("Kalaburgi")
time.sleep(1)

#State
driver.find_element_by_xpath("//input[@name='state']").send_keys("Karnataka")
time.sleep(1)

#Code
driver.find_element_by_xpath("//input[@name='postalCode']").send_keys("456789")
time.sleep(1)

#Dropdown by visible method /country
obj=Select(driver.find_element_by_name("country"))
obj.select_by_visible_text("INDIA")
time.sleep(1)

#username
driver.find_element_by_xpath("//input[@id='email']").send_keys("sita")
time.sleep(1)

#password
driver.find_element_by_xpath("//input[@name='password']").send_keys("12345asdf")
time.sleep(1)

#confirm password
driver.find_element_by_xpath("//input[@name='confirmPassword']").send_keys("12345asdf")
time.sleep(3)

#Scrolling_page
elm=driver.find_element_by_tag_name('html')
elm.send_keys(Keys.UP)
time.sleep(3)

elm.send_keys(Keys.DOWN)
time.sleep(4)

elm.send_keys(Keys.END)
time.sleep(3)

elm.send_keys(Keys.HOME)
time.sleep(6)

#Submit
driver.find_element_by_xpath("//input[@name='register']").click()
time.sleep(4)

#Flights
driver.find_element_by_xpath("//a[contains(text(),'Flights')]").click()
time.sleep(3)

#Type
driver.find_element_by_xpath("//body//b//input[1]").click()
time.sleep(1)

#Passengers by index method
obj=Select(driver.find_element_by_name("passCount"))
obj.select_by_index(2)
time.sleep(1)

#Departement from index method
obj=Select(driver.find_element_by_name("fromPort"))
obj.select_by_index(4)
time.sleep(1)

#On by visible method
obj=Select(driver.find_element_by_name("fromMonth"))
obj.select_by_visible_text("May")
time.sleep(1)

obj=Select(driver.find_element_by_name("fromDay"))
obj.select_by_visible_text("31")
time.sleep(1)

#Arriving Date by visible method
obj=Select(driver.find_element_by_name("toPort"))
obj.select_by_index(3)
time.sleep(1)

#Returning month by visible method
obj=Select(driver.find_element_by_xpath("//select[@name='toMonth']"))
obj.select_by_visible_text("August")
time.sleep(1)

#returing date by index method
obj=Select(driver.find_element_by_xpath("//select[@name='toDay']"))
obj.select_by_index(10)
time.sleep(1)

#Service class
driver.find_element_by_name("servClass").click()
time.sleep(1)

#Airline
obj=Select(driver.find_element_by_name("airline"))
obj.select_by_index(3)
time.sleep(2)

#Continue
driver.find_element_by_xpath("//input[@name='findFlights']").click()
time.sleep(4)

#Fetching title of page
print("Title of page is : " + driver.title)
time.sleep(1)

#feting URL of page
print("Page URL is : " +  driver.current_url)
time.sleep(3)

driver.quit()
