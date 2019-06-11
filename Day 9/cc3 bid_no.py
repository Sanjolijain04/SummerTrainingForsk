import mysql.connector
from selenium import webdriver

conn=mysql.connector.connect(user='sanjoli04', password='sanjoli@1166', host='db4free.net', database='ssdatabase')

c=conn.cursor()

c.execute("DROP TABLE bid_plus;")

url="https://bidplus.gem.gov.in/bidlists"

driver=webdriver.Chrome("D:\Padhai\Softwares\chromedriver.exe")

driver.get(url)

c.execute(""" CREATE TABLE bid_plus(
            Bid_no TEXT,
            Items TEXT,
            Quantity INTEGER,
            Dept TEXT,
            Start_date TEXT,
            Start_time TEXT,
            End_date TEXT,
            End_time TEXT)
        """)


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
    

for i in range(0,len(bid_no)):
    c.execute("INSERT INTO bid_plus VALUES ('"+bid_no[i]+"','"+items[i]+"',"+quantity[i]+",'"+dept[i]+"','"+start_date[i]+"','"+start_time[i]+"','"+end_date[i]+"','"+end_time[i]+"')")


c.execute("SELECT * FROM bid_plus")

print(c.fetchall())