from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import pandas as pd


website = 'https://www.thesun.co.uk/sport/football/'
path = "/chrome-win64"


# # instance service 
service = Service(executable_path = path)

# # instance driver
driver = webdriver.Chrome()

# print the website
driver.get(website)


# find specify element
containers = driver.find_elements(by=By.XPATH , value="//div[@class = 'teaser__copy-container']/.")

titles = []
sub_titles = []
links = []


for container in containers:

    # print(container.text)
    # container.find_element
    title = container.find_element(by=By.XPATH , value='./a/span').text
    sub_title = container.find_element(by=By.XPATH , value='./a/h3').text
    link = container.find_element(by=By.XPATH , value='./a').get_attribute('href')
    
    
    titles.append(title)
    sub_titles.append(sub_title)
    links.append(link)


my_dict = {'titles': titles , 'sub_titles': sub_titles , 'links': links}

df_news = pd.DataFrame(my_dict)

df_news.to_csv('df_news.csv')

driver.quit()