#import libraries
import pandas as pd
import numpy as np

#create dataset
dataset=pd.read_csv('PastHires.csv')

#create features and labels
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values

#label encode features
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features[:,1]=le.fit_transform(features[:,1])
features[:,3]=le.fit_transform(features[:,3])
features[:,4]=le.fit_transform(features[:,4])
features[:,5]=le.fit_transform(features[:,5])

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features, labels, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(features_train, labels_train)

#predict labels
labels_pred=dtc.predict(features_test)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test, labels_pred)


#find score
print("Score: ",dtc.score(features_test, labels_test))


"""
--------------------------- Random Forest----------
"""
#make random forest model
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=10, random_state=0)
rfc.fit(features_train, labels_train)
#predict labels
labels_pred2=rfc.predict(features_test)

#make confusion matrix
cm2=confusion_matrix(labels_test, labels_pred2)

#calculate score
print("Score 2 : ", rfc.score(features_test, labels_test))

#predict employment of first person
specs=np.array([10,1,4,0,1,0]).reshape(1,-1)
print("Hired: ",rfc.predict(specs))

#predict employment of second person
specs=np.array([10,0,4,1,0,1]).reshape(1,-1)
print("Hired2: ",rfc.predict(specs))


