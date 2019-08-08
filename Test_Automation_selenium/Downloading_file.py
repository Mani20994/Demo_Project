from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
time.sleep(5)

#Downloading Textfile
driver.find_element_by_xpath("//textarea[@id='textbox']").send_keys("testing download text file")
time.sleep(5)

#Generator file button
driver.find_element_by_xpath("//button[@id='createTxt']").click()
time.sleep(2)

#Download file button
driver.find_element_by_xpath("//a[@id='link-to-download']").click()
time.sleep(2)

#Dowmloading PDF file
driver.find_element_by_xpath("//textarea[@id='pdfbox']").send_keys("download text file")
time.sleep(3)

driver.find_element_by_xpath("//button[@id='createPdf']").click()
time.sleep(5)

#Download file button
driver.find_element_by_xpath("//a[@id='pdf-link-to-download']").click()
time.sleep(2)