from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("http://demo.guru99.com./test/delete_customer.php")
driver.maximize_window()

driver.find_element_by_name("cusid").send_keys("123")
driver.find_element_by_name("submit").click()
time.sleep(5)

#To accept the alert
alert =driver.switch_to.alert
#alert.accept()
#time.sleep(5)

#alert = driver.switch_to.alert
#alert.accept()
#time.sleep(4)

#Dismiss
alert.dismiss()
time.sleep(4)

driver.close()


