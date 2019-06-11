#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#get dataset
dataset=pd.read_csv('tshirts.csv')

#drop column of names
dataset=dataset.drop('name', axis=1)

#get features
features=dataset.iloc[:,[0,1]].values

#scatter features
plt.scatter(features[:,0], features[:,1])

#given the number of clusters=3
#import kmeans model
from sklearn.cluster import KMeans
#make model
kmeans=KMeans(n_clusters=3, init='k-means++', random_state=0)
#predict clusters
clusters_pred=kmeans.fit_predict(features)


#plot clusters
plt.scatter(features[clusters_pred==0,0],features[clusters_pred==0,1], c='red', label='Medium')
plt.scatter(features[clusters_pred==1,0],features[clusters_pred==1,1], c='blue', label='Large')
plt.scatter(features[clusters_pred==2,0],features[clusters_pred==2,1], c='green', label='Small')
#plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c='yellow', labels='Centroid')
plt.legend()
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Tshirt Sizes")
