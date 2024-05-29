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
    name = result.find_element("xpath", ".//div[contains(@class,'NrDZNb')]").text
    #reviews = result.find_element("xpath", "//span[contains(@class,'MW4etd')]").text
    results_span = result.find_elements(By.XPATH, ".//div[contains(@class,'AJB7ye')]")
    results_phone = result.find_elements(By.XPATH, ". //div[contains(@class,'W4Efsd')][2]/div[2]/span[2]")
    for child in results_span:
        rating_element = child.find_element(By.XPATH, ".//span[contains(@class,'fontBodyMedium')]")
        rating = rating_element.text.strip() if rating_element else "N/A"
    for child_p in results_phone:
        phone =  child_p.find_element(By.XPATH, ".//span[contains(@class,'UsdlK')]").text
    industry = result.find_element("xpath", ".//div[contains(@class,'W4Efsd')]/span/span").text
    address = result.find_element("xpath", ".//div[contains(@class,'W4Efsd')]/span[2]/span[2]").text
    items.append({"name": name, "rating": rating, "phone": phone, "industry": industry, "address": address, })
for result in items:
    print(result)

