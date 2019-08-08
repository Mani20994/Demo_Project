from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(3)
driver.get("http://only-testing-blog.blogspot.in/2014/09/selectable.html")
driver.implicitly_wait(1)

element = driver.find_element_by_xpath(".//*[@id='post-body-7297556448793668582']/div[1]/button").click()
driver.implicitly_wait(10)

act = ActionChains(driver)
act.double_click(element).perform()