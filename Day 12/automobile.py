# automobiles

#import libraries
import pandas as pd
import numpy as np

#open csv file
df=pd.read_csv('Automobile.csv')

#Handling missing values for price column

#check the columns in which data is null
df[df['price'].isnull()]

#fill the null value to the mean
df['price']=df['price'].fillna(df['price'].mean())

#create an nd array of price column
price_array=np.array(df['price'])
print(price_array)

#minimun price
print("Minimun price: ",df['price'].min())
#maximun price
print("Maximun price: ",df['price'].max())
#mean price
print("Mean Price: ",df['price'].mean())
#standard deviation of price
print("Standard Deviation: ",df['price'].std())