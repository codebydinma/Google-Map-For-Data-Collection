
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
        "phone" : phone,
        "address" : address,
        "longitude" : longitude,
        "latitude" : latitude,
        "website" : website,
        "open_time" : open_time,
        "close_time" : close_time,
        "reviews" : reviews})

    return df

driver = webdriver.Firefox()
driver.get("https://www.google.com/maps/")

elem = driver.find_element(By.ID, "searchboxinput")
elem.clear()
search_info = input("Enter your search: ")

elem.send_keys(search_info)
elem.send_keys(Keys.RETURN)

driver.close()
