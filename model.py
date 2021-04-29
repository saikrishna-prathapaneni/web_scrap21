from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime


url="https://weather.com/en-IN/weather/tenday/l/Khammam+Telangana?canonicalCityId=d9c48593696ea68859c748a8acf914dc031c166665e258c1d8afa0a685b8ee65"
driver = webdriver.Chrome('c:/chromedriver')
driver.get(url)

location=[]
temperature=[]
precipitation=[]
humid=[]

timeframe=[]
i=0
while True:
     
          try:
                time.sleep(2)
                driver.refresh()
                loc=driver.find_element_by_class_name("LocationPageTitle--PresentationName--Injxu")
                temp=driver.find_element_by_class_name("DailyContent--temp--_8DL5")
                prec=driver.find_element_by_class_name("DailyContent--value--3Xvjn")
                humidity=driver.find_element_by_class_name("DetailsTable--value--1F3Ze")
                timeframe.append(datetime.datetime.now())
                location.append(loc.text)
                temperature.append(temp.text)
                humid.append(humidity.text)
                precipitation.append(prec.text)
                i=i+1
          except KeyboardInterrupt:
             
             print("data collected")
             break
        # If you actually want the program to exit
        
df = pd.DataFrame({'location':location,'timeframe':timeframe,'temperature':temperature,'humid':humid,'precipitate':precipitation}) 
df.to_csv('weatherdata.csv', index=False, encoding='utf-8')




