#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dataframe for train
df=pd.read_csv("train.csv")
#get features train
features_train=df.iloc[:,:-1].values
#get labels train
labels_train=df.iloc[:,-1].values
#dataframe of test 
df2=pd.read_csv("test.csv")
#get features test
features_test=df2.iloc[:,:-1].values
#get labels test
labels_test=df2.iloc[:,-1].values

"""
Applyting decision tree classifer
"""

#apply decision tree classifier to predict data
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
#train model
dtc.fit(features_train, labels_train)

#predict labels
labels_pred=dtc.predict(features_test)

#make confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test, labels_pred)

#find score
score1=dtc.score(features_test, labels_test)

"""
Applying random forest classifier
"""
#import decision tree classifier
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=10, random_state=0)
#train model
rfc.fit(features_train, labels_train)

#predict labels
labels_pred=rfc.predict(features_test)

#make confusion matrix
cm2=confusion_matrix(labels_test, labels_pred)
score2=rfc.score(features_test, labels_test)

"""
Applying logistic regression
"""
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
#train model
lr.fit(features_train, labels_train)
#predict labels
labels_pred=lr.predict(features_test)

#make confusion matrix
cm3=confusion_matrix(labels_test, labels_pred)
score3=lr.score(features_test, labels_test)


"""
Applying kNN 
"""
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5, p=2)
#train model
knn.fit(features_train, labels_train)

#predict labels
labels_pred=knn.predict(features_test)

#make confusion matrix
cm4=confusion_matrix(labels_test, labels_pred)

#find score
score4=knn.score(features_test, labels_test)

"""
----------------------------------------------Models with feature reduction--------------------------------
"""
#label encode labels
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
labels=le.fit_transform(labels_train)


#applying backward elimination on features train
#add constant to feaures
import statsmodels.api as sm
features=sm.add_constant(features_train)

features_opt=features[:,:]
regressor_OLS=sm.OLS(endog=labels, exog=features_opt).fit()
regressor_OLS.summary()
#get a list of p values
p_values=list(regressor_OLS.pvalues)

#loop for all p values and eliminate thode p values which have p value>0.5
lst=[]
for i in range(0,len(p_values)):
    lst.append(i)
p_val=p_values
while(True):
    maximum=max(p_values)
    if(maximum>0.5):
        lst.remove(lst[p_values.index(maximum)])
        features=features[:,lst]
        regressor_OLS=sm.OLS(endog=labels, exog=features).fit()
        p_values=list(regressor_OLS.pvalues)
    else:
        break
    