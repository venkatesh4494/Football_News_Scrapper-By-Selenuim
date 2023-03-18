import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import sys
from datetime import datetime


app_path=os.path.dirname(sys.executable)
now=datetime.now()
month_day_year=now.strftime("%m%d%Y")

website="https://www.thesun.co.uk/sport/football/"
path="/usr/local/bin/chromedriver_mac64/chromedriver"


options=Options()
options.headless=True
driver=webdriver.Chrome(service=Service(executable_path=path),options=options)
driver.get(website)

containers=driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')

titles=[]
subtitles=[]
links=[]


for container in containers:
    title=container.find_element(by="xpath",value='./a/h3').text
    subtitle=container.find_element(by="xpath",value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

mydict={'title':titles,'subtitle':subtitles,'link':links}

df_headlines=pd.DataFrame(mydict)

filename=f'football_headlines_{month_day_year}.csv'
final_path=os.path.join(app_path,filename)
df_headlines.to_csv(final_path)

driver.quit()





