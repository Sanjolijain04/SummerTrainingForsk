#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori

from collections import defaultdict


#get dataset
dataset=pd.read_csv("Market_Basket_Optimisation.csv", header=None)

#use file handling for converting data to list of lists
transactions=[]

#initialize default dict
dict1=defaultdict(int)
#open file
with open("Market_Basket_Optimisation.csv","rt") as file:
    for line in file:
        lst=line.split(',')
        transactions.append(lst)
        for item in lst:
            dict1[item]+=1
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)




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

#print top 10 edibles
import operator
print("Top 10 edibles: ")
print(dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)[:11]))







