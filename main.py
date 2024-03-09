from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com/maps/")

elem = driver.find_element(By.ID, "searchboxinput")
elem.clear()
elem.send_keys("companies in rivers state")
elem.send_keys(Keys.RETURN)

driver.close()
