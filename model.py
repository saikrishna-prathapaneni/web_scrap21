from selenium import webdriver
import pandas as pd
import time
import datetime
#import all the necessary libraries


#url for the weather data 
url="https://weather.com/en-IN/weather/tenday/l/Khammam+Telangana?canonicalCityId=d9c48593696ea68859c748a8acf914dc031c166665e258c1d8afa0a685b8ee65"
#use of webdriver to activate communicate with the site
driver = webdriver.Chrome('c:/chromedriver')# change the location of the driver with repective the system used 
driver.get(url)

#variables for the data
location=[]
temperature=[]
precipitation=[]
humid=[]
timeframe=[]

#main program implements the collection of data every four hours untill keyboard interrupts
while True:
     
          try:
                time.sleep(14400)#change the time here for faster data collection 
                driver.refresh()
                #div elements on the website to collect the data
                loc=driver.find_element_by_class_name("LocationPageTitle--PresentationName--Injxu")
                temp=driver.find_element_by_class_name("DailyContent--temp--_8DL5")
                prec=driver.find_element_by_class_name("DailyContent--value--3Xvjn")
                humidity=driver.find_element_by_class_name("DetailsTable--value--1F3Ze")
                timeframe.append(datetime.datetime.now())
                location.append(loc.text)
                temperature.append(temp.text)
                humid.append(humidity.text)
                precipitation.append(prec.text)
                
          except KeyboardInterrupt: 
             print("data collected") #data collection untill keyboard interrupts
             break
                                   # If you actually want the program to exit


#pandas is used to convert the data into csv file  
df = pd.DataFrame({'location':location,'timeframe':timeframe,'temperature':temperature,'humid':humid,'precipitate':precipitation}) 
df.to_csv('weatherdata.csv', index=False, encoding='utf-8')




