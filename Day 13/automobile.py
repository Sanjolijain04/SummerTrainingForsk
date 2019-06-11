import pandas as pd
import matplotlib.pyplot as plt

#create data frame from diven csv file
df=pd.read_csv("Automobile.csv")

#make a series of make column
series=df['make'].value_counts()

#explode
explode=(0.3,0,0,0,0,0,0,0,0,0)

#make pie chart
plt.pie(series.values[:10], explode=explode, labels=series.index[:10], autopct='%2.2f%%')
plt.axis('equal')
plt.show()


