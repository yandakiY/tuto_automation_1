from selenium import webdriver
from selenium.webdriver.chrome.service import Service


website = 'https://www.thesun.co.uk/sport/football/'
path = "./chrome-win64"


# # instance service 
service = Service(executable_path = path)

# # instance driver
driver = webdriver.Chrome()

# get data
driver.get(website)
