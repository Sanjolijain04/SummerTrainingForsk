#import libraries
import pandas as pd
import numpy as np

#create dataset
dataset=pd.read_csv('pulsar_stars.csv')

#check for null values
dataset.isnull().any(axis=0)

#get labels and featutes
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values


#now we will standard scale our data
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
features=ss.fit_transform(features)


#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.25, random_state=0)


#make classification model
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(features_train, labels_train)

#predict labls
labels_pred=lr.predict(features_test)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test, labels_pred)


print("Score: ", lr.score(features_test, labels_test))
