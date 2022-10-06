from distutils.log import info
from importlib.resources import path
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
path=r"C:\Users\Simon\Documents\GitHub\real-estate-price-predictions\chromedriver.exe"
# driver=webdriver.Chrome(path)


# property listing has different sub urls than the actual property page sub url!!
root_url="https://www.immoweb.be/en"
property_url="/classified/apartment/for-sale/gavere/9890/10146915?searchId=633d38c4ccc41"
listing_url="/search/apartment/for-sale?countries=BE"
# test_url=""
driver=webdriver.Chrome(path)
driver.get(property_url)
# print(driver.title)
# driver.implicitly_wait(10)
# cookie_button=driver.find_element(By.XPATH,"""//*[@id="uc-btn-accept-banner"]""")
# cookie_button.click()

def get_property_char(property_url):
    property_char=requests.get(property_url)
    soup=BeautifulSoup(property_char.text,"html.parser")
    info=[]
    for info in soup.find_all("script"):
        info.append(info.text)
    data=info[1]
    return(data)

pages = driver.find_elements(By.XPATH, """/html/body/div[1]/div[1]/div/main/div/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/div/div[1]/div/nav/ul/li[4]/a/span[2]""")

for page in pages:
    total_pages=page.text
print(total_pages)




# print(soup.prettify())
