#import libraries
import pandas as pd
import numpy as np

#load dataset
dataset=pd.read_csv('breast_cancer.csv')

#drop column A of is
dataset=dataset.drop('A', axis=1)

#check for nan values
dataset.isnull().any(axis=0)

#replace nan values with mode
dataset['G']=dataset['G'].fillna(dataset['G'].mode()[0])

#get features and labels
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

#apply svm classification model
from sklearn.svm import SVC
classifier=SVC(kernel='rbf',random_state=0)
classifier.fit(features_train, labels_train)

#predict labels
labels_pred=classifier.predict(features_test)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)

#predict the type of cancer from given data
lst=np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1)
cls=classifier.predict(lst)
print("Class: ",cls)

if(cls==[4]):
    print("Cancerous")
else:
    print("non cancerous")
    