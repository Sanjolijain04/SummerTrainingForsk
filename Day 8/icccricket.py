#import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict


#provide url of html page
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

#content of full html page 
source=requests.get(url).text
#converting to beautiful soup
soup=BeautifulSoup(source,"lxml")

#find all tables
all_tables=soup.find_all('table')

#find correct table
right_table=soup.find("table" ,class_="table")

#generate lists
A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if(len(cells)==5):
        A.append(cells[1].text.strip())
        B.append(cells[2].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[4].text.strip())
        
col_name=['Team', 'Weighted matches', 'Points', 'Rating']
col_data=OrderedDict(zip(col_name,[A,B,C,D]))

df=pd.DataFrame(col_data)

    



