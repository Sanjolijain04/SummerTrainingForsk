#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

#get train dataframe
train=pd.read_json("train.json", lines=True, orient='columns')
#get test dataframe
test=pd.read_json("test.json",lines=True, orient='columns')

#applying nlp on the heading column in train data\
#download stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#stem data
from nltk.stem.porter import PorterStemmer
corpus = []
ps = PorterStemmer()
for i in range(0,20217):
    review = re.sub('[^a-zA-Z]', ' ',train['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1000)
features_train= cv.fit_transform(corpus).toarray()

#append column city and section to np array
features_train=np.append(features_train,train.loc[:,['city','section']].values,axis=1)

#label encode features
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features_train[:,-1]=le.fit_transform(features_train[:,-1])
features_train[:,-2]=le.fit_transform(features_train[:,-2])

#one hot encode features
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[-1])
features_train=ohe.fit_transform(features_train).toarray()
features_train=features_train[:,1:]

ohe=OneHotEncoder(categorical_features=[-1])
features_train=ohe.fit_transform(features_train).toarray()
features_train=features_train[:,1:]

#applying nlp on the heading column in test data\
#download stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#stem data
from nltk.stem.porter import PorterStemmer
corpus = []
ps = PorterStemmer()
for i in range(0,15370):
    review = re.sub('[^a-zA-Z]', ' ',test['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1000)
features_test= cv.fit_transform(corpus).toarray()

#append column city and section to np array
features_test=np.append(features_test,test.loc[:,['city','section']].values,axis=1)

#label encode features
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features_test[:,-1]=le.fit_transform(features_test[:,-1])
features_test[:,-2]=le.fit_transform(features_test[:,-2])

#one hot encode features
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[-1])
features_test=ohe.fit_transform(features_test).toarray()
features_test=features_test[:,1:]

ohe=OneHotEncoder(categorical_features=[-1])
features_test=ohe.fit_transform(features_test).toarray()
features_test=features_test[:,1:]

#get labels train
labels_train=train.loc[:,['category']].values

#train test split train features and labels
from sklearn.model_selection import train_test_split
ftr,ftst,ltr,ltst=train_test_split(features_train, labels_train, test_size=0.25,random_state=0)

"""
Apply machine learning-knn model
"""
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(ftr,ltr)
# Predicting the Test set results
lp1 = knn.predict(ftst)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm1=confusion_matrix(ltst,lp1)

#score
score_knn=knn.score(ftst,ltst)

"""
applying logistic regression
"""
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(ftr,ltr)
# Predicting the Test set results
lp2 = lr.predict(ftst)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm2=confusion_matrix(ltst,lp2)

#score
score_lr=lr.score(ftst,ltst)

"""
Applying decision tree
"""

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(ftr,ltr)
# Predicting the Test set results
lp3 = dtc.predict(ftst)
#make confusion matrix
from sklearn.metrics import confusion_matrix
cm3=confusion_matrix(ltst,lp3)
#score
score_dtc=dtc.score(ftst,ltst)



#predict labels using logistic regression

labels_predicted=lr.predict(features_test)
