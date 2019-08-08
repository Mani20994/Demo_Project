from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")#chromepathname
driver.get("http://www.theTestingWorld.com/testings")#URL

driver.maximize_window()#Max_window
time.sleep(1)

driver.find_element_by_xpath("//input[@placeholder='myusername']").send_keys("Ravi")#username
time.sleep(2)

driver.find_element_by_xpath("//input[@placeholder='myusername@gmail.com']").send_keys("ravi1234@gmail.com")#user_id
time.sleep(2)

driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("abcd$1234")#password
time.sleep(2)

driver.find_element_by_xpath("//input[@placeholder='Confirm password']").send_keys("abcd$1234")#confirm_password
time.sleep(2)

driver.find_element_by_xpath("//input[@id='datepicker']").send_keys("07/29/2019")#date
time.sleep(2)

driver.find_element_by_xpath("//input[@placeholder='Phone']").send_keys("9966453200")#mobile_number
time.sleep(2)

driver.find_element_by_xpath("//input[@placeholder='Address']").send_keys("Opposite high court")#address
time.sleep(2)

driver.find_element_by_xpath("//body//input[9]").click()#Address_type
time.sleep(2)

#Dropdown_by_index_method
obj=Select(driver.find_element_by_xpath("//select[@name='sex']"))#Gender
obj.select_by_index(1)
time.sleep(9)

#Dropdown_by_visible_method
obj=Select(driver.find_element_by_xpath("//select[@id='countryId']"))#Country
obj.select_by_visible_text("India")
time.sleep(9)

#State
obj=Select(driver.find_element_by_xpath("//select[@id='stateId']"))
obj.select_by_visible_text("Karnataka")
time.sleep(9)

#City
obj=Select(driver.find_element_by_xpath("//select[@id='cityId']"))
obj.select_by_index(15)
time.sleep(3)

#Zipcode
driver.find_element_by_xpath("//input[@placeholder='Zip code']").send_keys("456789")
time.sleep(2)

#Check
driver.find_element_by_xpath("//div[@id='tab-content1']//form[1]").click()
time.sleep(2)

#Scrolling_page
elm=driver.find_element_by_tag_name('html')
elm.send_keys(Keys.UP)
time.sleep(2)

elm.send_keys(Keys.DOWN)
time.sleep(4)

elm.send_keys(Keys.END)
time.sleep(4)

elm.send_keys(Keys.HOME)
time.sleep(7)

driver.find_element_by_xpath("//li[1]//div[1]//form[1]//div[1]//input[2]").click()#signup
time.sleep(5)

#fetchind title
print("Title of page is : " + driver.title)
time.sleep(5)

#Fetching URL of page
print("Page URL is : " + driver.current_url)
time.sleep(5)

driver.quit()