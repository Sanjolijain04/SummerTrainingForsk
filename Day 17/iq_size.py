#import libraries
import pandas as pd
import numpy as np

#get dataset
dataset=pd.read_csv('iq_size.csv')

#get features and labels
features=dataset.iloc[:,1:].values
labels=dataset.iloc[:,0].values

#using multiple regression
from sklearn.linear_model import LinearRegression
#make model
lr=LinearRegression()
#fit data into model
lr.fit(features, labels)

#check score of model
lr.score(features, labels)

#make quadratic model
from sklearn.preprocessing import PolynomialFeatures
#make object
pf=PolynomialFeatures(degree=2)
#change polynomial
features_poly=pf.fit_transform(features)

#fit data to linear model
lr2=LinearRegression()
lr2.fit(features_poly, labels)