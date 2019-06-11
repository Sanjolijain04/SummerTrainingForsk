#import libraries

import pandas as pd



#create dataset of given data
dataset=pd.read_csv('Bahubali2_vs_Dangal.csv')

#calculate labels and features
features=dataset.iloc[:,0].values.reshape(-1,1)
labels=dataset.iloc[:,[1,2]].values


#import ml library
from sklearn.linear_model import LinearRegression
#create madel
regressor=LinearRegression()
#fit data to model
regressor.fit(features,labels)

#find coeff and intercept of model
print(regressor.intercept_)
print(regressor.coef_)

#predict values
import numpy as np

x=[10]
x=np.array(x).reshape(-1,1)
regressor.predict(x)

