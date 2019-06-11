#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create dataset
dataset=pd.read_csv('bluegills.csv')

#find features and labels
features=dataset.iloc[:,0].values.reshape(-1,1)
labels=dataset.iloc[:,1].values.reshape(-1,1)

#perform linear regression
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features,labels)

#draw linear graph
plt.scatter(features, labels)
plt.plot(features, regressor.predict(features), color='blue')
plt.xlabel("Age")
plt.ylabel("Height")
plt.title("Fish")
plt.show()

print("Score of linear : ", regressor.score(features, labels))

#fitting polunomial regression to database
from sklearn.preprocessing import PolynomialFeatures
poly_obj=PolynomialFeatures(degree=2)
features_poly=poly_obj.fit_transform(features)

#create linear model
regressor_2=LinearRegression()
regressor_2.fit(features_poly,labels)

print("Score of Quadratic: ",regressor_2.score(features_poly,labels))
x=np.array([5]).reshape(-1,1)
print(regressor_2.predict(poly_obj.transform(x)))
