from importlib.resources import path
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
path=r"C:\Users\Simon\Documents\GitHub\real-estate-price-predictions\chromedriver.exe"
driver=webdriver.Chrome(path)


#property listing has different sub urls than the actual property page sub url!!
root_url="https://www.immoweb.be/en"
property_url="/classified/apartment/for-sale/gavere/9890/10146915?searchId=633d38c4ccc41"
listing_url="/search/apartment/for-sale?countries=BE"
test_url=""
driver.get({root_url, })
print(driver.title)




# property=requests.get(f"{root_url}{property_url}")

# first_content=BeautifulSoup(property.text,'html.parser')
# print(first_content.prettify())