
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pandas as pd

def map_details():
    name: str = []
    phone: str =  []
    address: str = []
    longitude: float = []
    latitude: float = []
    website: str = []
    open_time: str = []
    close_time: str =  []
    reviews: str =  []

    df = pd.DataFrame({"name" : name,
        "phone": phone,
        "address": address,
        "longitude": longitude,
        "latitude": latitude,
        "website": website,
        "open_time" : open_time,
        "close_time" : close_time,
        "reviews": reviews})

    return df

driver = webdriver.Firefox()
driver.get("https://www.google.com/maps/")

elem = driver.find_element(By.ID, "searchboxinput")
elem.clear()
search_info = input("Enter your search: ")

elem.send_keys(search_info)
elem.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 40)
wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'m6QErb')]")))

items = []

# Wait for links and extract
results = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class,'Nv2PK')]")))
for result in results:
    element = result.find_element("XPath","//div[contains(@class,'NrDZNb')]")
    link = element.text
    items.append(link)
    print(items)

driver.close()
