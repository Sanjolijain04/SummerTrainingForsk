#import libraries
import pandas as pd
import numpy as np

#load dataset
from sklearn.datasets import load_iris
dataset=load_iris()

#get features and labels
features=dataset.data
labels=dataset.target

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.305, random_state = 0)

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


