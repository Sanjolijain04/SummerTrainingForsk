#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import apriori functionn
from apyori import apriori

#read dataset
dataset=pd.read_csv('BreadBasket_DMS.csv')

#drop column of date and column
dataset=dataset.drop(['Date', 'Time'], axis=1)

#plot pie chart of top 15 selling items 
dataset['Item'].value_counts()[:16].plot.pie()

#initialize transactions
transactions=[]

#apply loop
#for i in range(1,9685):
#    transaction.append([str(dataset['Item'][j]) if dataset['Transaction'][j]==str(i) for j in range(0,21293)])

#convert series to list
def convert_tolist(arg):
#    lst=arg.values
    transactions.append(list(set(arg)))
    
    

#convert dataset to lists of lists
dataset.groupby(['Transaction'])['Item'].apply(convert_tolist)

#apply apriori on the dataset
rules=apriori(transactions, min_support=0.0025, min_confidence=0.2, min_lift=3)

#convert rules to list
results=list(rules)


#print item in sophisticated way
for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    
    

