#import libraries

import pandas as pd

#create dataset
dataset=pd.read_csv('Female_Stats.csv')


#labels and features
features=dataset.iloc[:,1:3].values
labels=dataset.iloc[:,0].values


#view statistics of our features
import statsmodels.api as sm

#add contsant to features
features=sm.add_constant(features)

#make a copy of features
features_opt = features[:,:]
#make a model using OLS class
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
#view summary
print(regressor_OLS.summary())
#coeff for moms height
print('Coeff for mom: ',regressor_OLS.params[1])
#coeff for dads height
print('Coeff for dad: ',regressor_OLS.params[2])
