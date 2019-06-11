import pandas as pd
from selenium import webdriver
from collections import OrderedDict

url="https://bidplus.gem.gov.in/bidlists"

driver=webdriver.Chrome("D:\Padhai\Softwares\chromedriver.exe")

driver.get(url)

bid_no=[]
items=[]
quantity=[]
dept=[]
start=[]
end=[]


for i in range(1,11): # find by using x path
   bid_no.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
   items.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
   quantity.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
   dept.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
   start.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
   end.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)
  
start_date=[]
start_time=[]
end_date=[]
end_time=[]

for item in start:
    start_date.append(item.split()[0])
    start_time.append(item.split()[1] + item.split()[2])
for item in end:
    end_date.append(item.split()[0])
    end_time.append(item.split()[1] + item.split()[2])   

col_name=["Bid No","Items","Quantity Required","Dept., Name, Address","Start Date","Start Time","End Date", "End Time"]
col_data=OrderedDict(zip(col_name,[bid_no,items,quantity,dept,start_date,start_time,end_date,end_time]))

df = pd.DataFrame(col_data) 
df.to_csv("bid_plus.csv")