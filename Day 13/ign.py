import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df=pd.read_csv('ign.csv')

#filter xbox one with score gt 7
xbox_one_filter=((df['platform']=='Xbox 360') & (df['score']>7))
filtered_reviews=df[xbox_one_filter]

#draw histogram for Xbox 360
df[df['platform']=='Xbox 360']['score'].plot(kind='hist')

#draw historgram of playstation 4
df[df['platform']=='PlayStation 4']['score'].plot(kind='hist')


#draw histogram of xbox one filter
filtered_reviews['score'].plot(kind='hist')

