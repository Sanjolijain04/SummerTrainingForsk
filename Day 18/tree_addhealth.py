#import libraries
import pandas as pd
import numpy as np

#create dataset
dataset=pd.read_csv('tree_addhealth.csv')

#replace null values with mode
for i in dataset:
    dataset[i]=dataset[i].fillna(dataset[i].mode()[0])


#find features
features=dataset[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
#find labels
labels=dataset['TREG1'].values

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.2, random_state=0)


#make decision tree classifier model
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(features_train, labels_train)

#predict labels
labels_pred=dtc.predict(features_test)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm1=confusion_matrix(labels_test, labels_pred)
#score

print("Chances of smoking: ",dtc.score(features_test, labels_test))

"""
-------------------------Part-2-----------------------------------
"""

#find features and labels
features=dataset[['BIO_SEX','VIOL1']].values
labels=dataset[['EXPEL1']].values

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.2, random_state=0)


#make decision tree classifier model
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(features_train, labels_train)


#predict labels
labels_pred=dtc.predict(features_test)




#make confusion matrix
from sklearn.metrics import confusion_matrix
cm2=confusion_matrix(labels_test, labels_pred)
#score

print("Chances of expel: ",dtc.score(features_test, labels_test))


"""
-------------------------Part-3---------------------------------
"""

#find features and labels
features=dataset[['WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN']].values
labels = dataset["TREG1"].values

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.2, random_state=0)

#make random forest classifier model 
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
rfc.fit(features_train, labels_train)

labels_pred=rfc.predict(features_test)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm2=confusion_matrix(labels_test, labels_pred)
#score

print("Chances of being a smoker: ",rfc.score(features_test, labels_test))



 