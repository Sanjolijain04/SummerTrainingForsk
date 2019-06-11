#import libraries
import pandas as pd
import numpy as np

#read dataset
dataset=pd.read_csv('affairs.csv')

#check for null values
dataset.isnull().any(axis=0)

#find features
features=dataset.iloc[:,:-1].values
#find labels
labels=dataset.iloc[:,-1].values

#one hot encoding for occupation
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[6])
features=ohe.fit_transform(features).toarray()
features=features[:,1:]

#one hot encoding for husband occupation
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[11])
features=ohe.fit_transform(features).toarray()
features=features[:,1:]

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test,labels_train, labels_test=train_test_split(features, labels, test_size=0.25, random_state=0)

#convert all features to standard scale
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)

#perform logistic regression
from sklearn.linear_model import LogisticRegression
#make model
classifier=LogisticRegression()
#train model
classifier.fit(features_train, labels_train)


#predict labels for featutres test
labels_pred=classifier.predict(features_test)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test, labels_pred)

#check score
s=classifier.score(features_test,labels_test)

#percentage of women having affair
affair_yes=pd.value_counts(labels)[1]
affair_no=pd.value_counts(labels)[0]
affair_pct=(affair_yes/(affair_yes+ affair_no))*100


#predict the affair of women 
ft=np.array([1,0,0,0,0,0,0,0,1,0,3,25,3,1,4,17]).reshape(1,-1)
pred_label=classifier.predict(ft)

