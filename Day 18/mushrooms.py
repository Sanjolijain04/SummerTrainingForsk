#import libraries
import pandas as pd
import numpy as np

#create dataset
dataset=pd.read_csv('mushrooms.csv')

#taking habitat, population and odor as predictors
dataset=dataset.iloc[:,[5,21,22,0]]

#find features
features=dataset.iloc[:,:-1].values

#find labels
labels=dataset.iloc[:,-1].values



#label encode features one by one
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features[:,0]=le.fit_transform(features[:,0])
features[:,1]=le.fit_transform(features[:,1])
features[:,2]=le.fit_transform(features[:,2])

#one hot encode features
#for odor
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[0])
features=ohe.fit_transform(features).toarray()
#remove first column
features=features[:,1:]

#for population
ohe=OneHotEncoder(categorical_features=[9])
features=ohe.fit_transform(features).toarray()
#remove first column
features=features[:,1:]

#for habitat
ohe=OneHotEncoder(categorical_features=[14])
features=ohe.fit_transform(features).toarray()
#remove first column
features=features[:,1:]


#perform train test split
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)

#making logistic regression model
from sklearn.linear_model import LogisticRegression
#make model
lr=LogisticRegression()
#train model
lr.fit(features_train, labels_train)

#make predicted labels
labels_pred=lr.predict(features_test)


#make confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test, labels_pred)


#predict values
arr=np.array([1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]).reshape(1,-1)
print("Class: ",lr.predict(arr))



