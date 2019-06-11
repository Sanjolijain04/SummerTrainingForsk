#import libararies

import pandas as pd
import numpy as np


#get dataset
dataset=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delim_whitespace=True)
data=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delim_whitespace=True)

features=dataset.drop('lpsa',axis=1)
labels=dataset['lpsa']

#standard scale features
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
features=ss.fit_transform(features)

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.2, random_state=0)


"""
-----------------------linear regression------------
"""

#make linear model
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features_train, labels_train)

#predict labels
labels_pred=lr.predict(features_test)

# calculate mean squared error
from sklearn import metrics
print("Mean squared error: ",metrics.mean_squared_error(labels_test,labels_pred))


"""
-----------------Using lasso---------------------
"""
#lasso 
from sklearn.linear_model import Lasso
regressor_lasso=Lasso()
regressor_lasso.fit(features_train, labels_train)

#predict labels
labels_pred=regressor_lasso.predict(features_test)
print("Mean squared error(lasso) : ",metrics.mean_squared_error(labels_test,labels_pred))


"""
-----------------Using ridge---------------------
"""
#lasso 
from sklearn.linear_model import Ridge
regressor_ridge=Ridge()
regressor_ridge.fit(features_train, labels_train)

#predict labels
labels_pred=regressor_ridge.predict(features_test)
print("Mean squared error(ridge) : ",metrics.mean_squared_error(labels_test,labels_pred))


"""
-------------------Part 2-----------------------------
"""

#find mean of lpsa
lpsa_mean=labels.mean()

data['lpsa']=list(map(lambda x: 'high' if x> lpsa_mean else 'low', data['lpsa']))


