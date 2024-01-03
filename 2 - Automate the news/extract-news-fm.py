from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


site_url = 'https://www.footmercato.net/'
path = '/chromewin64'

# create options headless
options = Options()
options.add_argument('--headless=new')

# Create service
service = Service(executable_path = path)

# create river of webdriver
driver = webdriver.Chrome(options=options)

# get url site
driver.get(site_url) 

# Find infos

containers_articles = driver.find_elements(by=By.XPATH , value = "//div[contains(@class , 'group__main--desktopOnly')]/article[contains(@class , 'articleInline--center')]/div/.")

print('article trouve :' , len(containers_articles))
# variables
categories = []
titles = []
links = []


for article in containers_articles:
    
    title = article.find_element(by=By.XPATH , value = "./a[@class = 'articleInline__titleMetas']/div/h3/.").text
    link = article.find_element(by = By.XPATH , value="./a[@class = 'articleInline__imageLink']/.").get_attribute('href')
    
        
    
    titles.append(title)
    links.append(link)


# list to dict
dict_news = {
    'titles': titles , 'links':links
}

df_dict_news = pd.DataFrame(dict_news)

df_dict_news.to_csv('fm_news.csv')

driver.quit()