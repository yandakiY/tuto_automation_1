from selenium import webdriver
from selenium.webdriver.chrome.service import Service


website = 'https://www.thesun.co.uk/sport/football/'
path = "./chrome-win64"


# # instance service 
service = Service(executable_path = path)

# # instance driver
driver = webdriver.Chrome()

# print the website
driver.get(website)


# find specify element
containers = driver.find_elements(by='xpath' , value="//div[@class = 'teaser__copy-container']")

list_title = []


for container in containers:

    title = driver.find_element(by='xpath' , value="./a/span[contains(@class , 'teaser__headline')]").text
    sub_title = driver.find_element(by='xpath' , value="./a/h3").text
    link = driver.find_element(by='xpath' , value='./a').get_attribute('href')
    #  list_title.append(title)

print(containers.count())