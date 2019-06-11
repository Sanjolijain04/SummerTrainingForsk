#import libraries
import pandas as pd
import numpy as np

#create dataset
dataset=pd.read_table('Auto_mpg.txt', delim_whitespace=True, names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])

#car with highest mpg
print("Car name with highest mpg: ",dataset[dataset['mpg']==dataset['mpg'].max()]['car name'])

"""
---------Decision Tree of given dataset---------
"""
#replace ? 
dataset['horsepower']=dataset['horsepower'].replace('?','0')
dataset=dataset.drop('car name', axis=1)


#find features
features=dataset.iloc[:,1:].values
#find labels
labels=dataset.iloc[:,0].values

#Label Encoding Features
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features[:,-1]=le.fit_transform(features[:,-1])

#standard scale all the values
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.2, random_state=0)

#make decision tree model
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor()
regressor.fit(features_train, labels_train)

#predict labels
labels_pred=regressor.predict(features_test)

print("Score of decision tree: ", regressor.score(features_test, labels_test))

"""
-------- random forest-----------
"""

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor(n_estimators=20, random_state=0)
rfr.fit(features_train, labels_train)

#predict labels
labels_pred2=rfr.predict(features_test)
print("Score of random forest: ", rfr.score(features_test, labels_test))

#finding mpg for both model with given specs
specs=np.array([6,215,100.0,2630,22.2,80,3]).reshape(1,-1)
#predict for decison tree
print("mpg from decison tree: ", regressor.predict(specs))
print("mpg from random forest: ", rfr.predict(specs))




