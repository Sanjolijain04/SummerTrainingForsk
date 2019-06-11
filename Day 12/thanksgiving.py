#import libraries
import pandas as pd
import numpy as np
#read csv file
dataset=pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

#changing columns name
#making list of actual column name
col_names=list(dataset.columns)

#making list of codes equal to number of columns
col_code= [x for x in range(0,65)]

#making dictionary to use columns name with their code for furthur reference
col_ref=dict(zip(col_code,col_names))

#changing the column names of dataset
dataset.columns=col_code

#sorting data of people who celebrate thanksgiving
dataset=dataset[dataset[1]=='Yes']

#replcing nan values to missing keyword
dataset=dataset.replace(np.nan,"Missing")

