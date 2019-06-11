from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt

#link of web page
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

#get content of web page
source=requests.get(url).text

#parse it
soup=BeautifulSoup(source,'lxml')

#extract all tables
all_tables=soup.find_all('table')

#required table
right_table=soup.find("table", class_="wikitable")

#make dataframe of the table
state=[]
share=[]
#list of columns of table
for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if(len(cells)==7):
        state.append(cells[1].text.strip())
        share.append(cells[4].text.strip())
        
#create dictionary of lists
col_names=['State/Territory','National Share(%)']
d=OrderedDict(zip(col_names,[state, share]))

#make dataframe of table
df=pd.DataFrame(d)
df=df[:6]

#make pie chart of the data frame
explode=(0.5,0,0,0,0,0)
plt.pie(df['National Share(%)'], explode=explode, labels=df['State/Territory'], autopct='%2.2f%%')
plt.axis('equal')
plt.show()



    



