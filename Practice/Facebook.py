#import libraries
import pandas as pd
import numpy as np

#load dataset
dataset=pd.read_csv('dataset_Facebook.csv',delimiter=';')

dataset['Paid']=dataset['Paid'].fillna(dataset['Paid'].mode()[0])

