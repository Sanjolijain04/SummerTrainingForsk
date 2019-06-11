#import libraries
import pandas as pd


#create dataset
dataset=pd.read_csv('kc_house_data.csv')

#replace nan values with mean
dataset=dataset.fillna(dataset.mean())


#find labels and features
features=dataset.drop(['price','id','date'], axis=1)
labels=dataset['price']

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.2, random_state=0)


#make linear regression model
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features_train, labels_train)

#predict labels
labels_pred=lr.predict(features_test)

print("Score of linear regression: ",lr.score(features_test, labels_test))


"""
-----------------Using lasso---------------------
"""
#lasso 
from sklearn.linear_model import Lasso
regressor_lasso=Lasso()
regressor_lasso.fit(features_train, labels_train)

#predict labels
labels_pred=regressor_lasso.predict(features_test)

print("SCore from lasso: ",regressor_lasso.score(features_test, labels_test))


"""
-----------------Using ridge---------------------
"""
#lasso 
from sklearn.linear_model import Ridge
regressor_ridge=Ridge()
regressor_ridge.fit(features_train, labels_train)

#predict labels
labels_pred=regressor_ridge.predict(features_test)

print("Score from ridge: ",regressor_ridge.score(features_test, labels_test))


