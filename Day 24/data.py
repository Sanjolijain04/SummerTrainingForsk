#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#get dataset
dataset=pd.read_csv('data.csv')

#drop column with all value null
for col_name in dataset.columns:
    if(dataset[col_name].isnull().all(axis=0)):
        dataset=dataset.drop(col_name, axis=1)
        


#visualize the countries with top artworks
lst=dataset['Country'].value_counts().head(10)
values=list(lst.values)
labels=list(lst.index)
pie=plt.pie(values, autopct='%2.2f%%')
plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
           bbox_transform=plt.gcf().transFigure)

#top 2 classification of artwork
dataset['Classification'].value_counts().head(2).plot.bar()

#artists interested in artwork
dataset['Artist Display Name'].value_counts().plot.bar()

#top 2 culture of artworks
dataset['Culture'].value_counts().head(2).plot.bar()