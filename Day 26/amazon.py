#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#get dataset
dataset=pd.read_csv("amazon_cells_labelled.txt", delimiter="\t", header=None)
#give name to columns
dataset.columns=["Review","Category"]

#import regular expressions
import re
#import library for nlp
import nltk

#download stopwords from nltk
nltk.download('stopwords')

#import stopwords
from nltk.corpus import stopwords

#import stemmer
from nltk.stem.porter import PorterStemmer
#mqke object of stemmer
ps=PorterStemmer()

#make a empty list 
corpus=[]
#loop for all rows
for i in range(0,1000):
    #replace all non character with spaces
    review=re.sub('[^a-zA-Z]',' ', dataset["Review"][i])
    #convert review to lower case
    review=review.lower()
    #split the review
    review=review.split()
    #get the words which are not present in stopwords
    review=[word for word in review if not word in set(stopwords.words('english'))]
    #stem each word in review
    review=[ps.stem(word) for word in review]
    
    #join review
    review=" ".join(review)
    corpus.append(review)

#create bag of words model
from sklearn.feature_extraction.text import CountVectorizer
#make object and limit the number of features
cv=CountVectorizer(max_features=900)
#get features
features=cv.fit_transform(corpus).toarray()
#get labels
labels=dataset.iloc[:,-1].values

#perform train test split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

#apply gaussian naive bayes algorithm
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)

#apply knn
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
