#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#get dataset
dataset=pd.read_csv('election.csv')

#Fetch the top parties of each state within each constituency with their vote %.
df1=dataset[['State','Constituency','Party','%']]
df_sort1=df1.sort_values(by ='%', ascending=False)
df_final1=df_sort1.drop_duplicates(subset='Constituency')



#Visualize the top parties vote % in each constituency for Rajasthan.
df2=dataset[dataset['State']=='Rajasthan'][['Constituency','Party','%']]
df_sort2=df2.sort_values(by ='%', ascending=False)
df_final2=df_sort2.drop_duplicates(subset='Constituency')

#Visualize the total seats gained by each party in each states.
df3=dataset[['State','Constituency','Party','%']]
df_sort3=df3.sort_values(by='%', ascending=False)
df_dup=df_sort3.drop_duplicates(subset='Constituency')
df_final3=df_dup.groupby(['Party','State'])['Constituency'].count()


#Visualize the total seats won by the parties in the whole country
df4=dataset[['State','Constituency','Party','%']]
df_sort4=df4.sort_values(by='%', ascending=False)
df_dup4=df_sort4.drop_duplicates(subset='Constituency')
df_final4=df_dup.groupby(['Party'])['Constituency'].count()


