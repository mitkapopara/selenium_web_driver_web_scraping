from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Users/meet/Desktop/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.python.org/")
event_times = driver.find_elements(by="css selector", value=".event-widget time")
event_names = driver.find_elements(by="css selector", value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
#print(events)
driver.quit()