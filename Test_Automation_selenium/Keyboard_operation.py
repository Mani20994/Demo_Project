from selenium import webdriver
import time

from selenium .webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("http://www.thetestingWorld.com/testings")

driver.maximize_window()
driver.find_element_by_xpath(".//*[@id='tab-content1']/form/input[2]").send_keys("Hello")

act =ActionChains(driver)
time.sleep(5)

#act.send_keys(Keys.CONTROL).send_keys('a').perform()
#act.send_keys(Keys.TAB).perform()
#time.sleep(5)

act.send_keys(Keys.SPACE).perform()
time.sleep(5)

#act.send_keys(Keys.BACK_SPACE).perform()
#time.sleep(5)

#driver.close()