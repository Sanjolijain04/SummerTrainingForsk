#import libraries
import pandas as pd
import numpy as np

#create dataframe
dataset=pd.read_csv('Foodtruck.csv')

#predict labels and features
features=dataset.iloc[:,0].values.reshape(-1,1)
labels=dataset.iloc[:,1].values.reshape(-1,1)

#import libraries
from sklearn.linear_model import LinearRegression

#create object
regressor=LinearRegression()

#fit data to model
regressor.fit(features,labels)

#print intercept and coeff
print(regressor.coef_)
print(regressor.intercept_)

#predict data for pop=3.
x=[3.073]
x=np.array(x).reshape(-1,1)
print(regressor.predict(x))
