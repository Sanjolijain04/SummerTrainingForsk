#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#get dataset
dataset=pd.read_csv('deliveryfleet.csv')

#drop driver is as it is not a features
dataset=dataset.drop('Driver_ID', axis=1)

#divide dataset into two features accoridng to the distance features

#get features
features=dataset.iloc[:,[0,1]].values

#visualize the data
plt.scatter(features[:,0], features[:,1])

#import kmeans class
from sklearn.cluster import KMeans

#make kmeans model
kmeans=KMeans(n_clusters=2, init='k-means++', random_state=0)
#predict clusters
clusters_pred=kmeans.fit_predict(features)


#plot  clusters
plt.scatter(features[clusters_pred==0,0], features[clusters_pred==0,1], c='red', label='Rural')
plt.scatter(features[clusters_pred==1,0], features[clusters_pred==1,1], c='blue', label='Urban')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c='Yellow', label='Centroid')
plt.xlabel("Distance Travelled")
plt.ylabel("Speed")
plt.title("Urban v/s Rural")
plt.legend()


