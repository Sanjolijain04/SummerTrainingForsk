#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing regular expression
import re

#get dataset
dataset=pd.read_csv('monster_com-job_sample.csv')

#replace nan values with keyword missing
dataset=dataset.replace(np.nan, 'Missing')


#regular expression for location
#result=re.search(r'[A-Za-z]*(\s?[[A-Za-z]*]?){1,}[\,]{1}?\s?[A-Z]{2}\s?[0-9]*','Madison New City, CM 76534')

#regular expression for organization
#result=re.search(r'(([A-Za-z]*[\.]?\s?){1,}[\-/&,]?([A-Za-z]*[\.]?\s?){1,}){1,}','')


#make a list for organization column to find pattern of location
lst=[]
for item in dataset['organization']:
    result=re.findall(r'[A-Za-z]*\s?[[A-Za-z]*]?\s?[[A-Za-z]*]?[\,]{1}?\s?[A-Z]{2}\s?[0-9]*',item)
    lst.append(result)


#get the list of index with loc in organisation column
    
loc_ind=[]   
for item in lst:
    if(item!=[]):
        loc_ind.append(lst.index(item))

#check for organization in the column location of list of index
lst2=[]
#([A-Za-z]*\s?[\/.,:&]?)
for item in loc_ind:
    result=re.findall(r'^[a-zA-Z&\-\.\/\s]{10,}',dataset['location'][item])
    lst2.append(result)

loc_ind_org=[]
for item in lst2:
    if(item!=[]):
        loc_ind_org.append(lst.index(item))  