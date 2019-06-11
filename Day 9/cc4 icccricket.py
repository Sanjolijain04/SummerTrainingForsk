#import libraries
from bs4 import BeautifulSoup
import requests



#provide url of html page
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

#content of full html page 
source=requests.get(url).text
#converting to beautiful soup
soup=BeautifulSoup(source,"lxml")

import sqlite3

conn=sqlite3.connect('my_cricket.db')

c=conn.cursor()



c.execute(""" CREATE TABLE cricket(
            Team TEXT,
            Weighted_Matches INTEGER,
            Points INTEGER,
            Rating INTEGER)
        """)

#find all tables
all_tables=soup.find_all('table')

#find correct table
right_table=soup.find('table' ,class_='table')

#generate lists
team=[]
wtmatches=[]
pts=[]
rating=[]

for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if(len(cells)==5):
        team.append(cells[1].text.strip())
        wtmatches.append(cells[2].text.strip())
        pts.append(cells[3].text.strip())
        rating.append(cells[4].text.strip())
        
for i in range(0,len(team)):
    c.execute("INSERT INTO cricket VALUES ('"+team[i]+"',"+wtmatches[i]+","+pts[i]+","+rating[i]+")")

c.execute("SELECT * FROM cricket")

print(c.fetchall())


        
