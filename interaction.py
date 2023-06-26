from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("C:/Users/meet/Desktop/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by="name", value="fName")
last_name = driver.find_element(by="name", value="lName")
email = driver.find_element(by="name", value="email")
first_name.send_keys("met")
last_name.send_keys("Kapora")
email.send_keys("ujfhsfhfshfvsuifhy0472847@gail.com")
sing_up = driver.find_element(by="css selector", value="form button")
sing_up.send_keys(Keys.ENTER)





