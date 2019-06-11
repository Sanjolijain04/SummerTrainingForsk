#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#get dataset
df=pd.read_csv("Dating_Data.csv", encoding="Windows 1252")

#replace nan values with missing
df=df.replace(np.nan,0)

#visualize what male and female see most in their date
df.groupby(['gender'])['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1'].sum().plot.bar()

#visualize what partner look into date
df.groupby(['gender'])['attr2_1','sinc2_1','intel2_1','fun2_1','amb2_1','shar2_1'].sum().plot.bar()

#visualize how often they go out males and females
df.groupby(['gender'])['go_out'].value_counts()[0].plot.bar()
df.groupby(['gender'])['go_out'].value_counts()[1].plot.bar()

#activities liked by them
df.groupby(['gender'])['sports','tvsports','exercise','dining','museums','art','hiking','gaming','clubbing','reading','tv','theater','movies','concerts','music','shopping','yoga'].mean().plot.bar()


#willingness to date with respect to race of partner
df.groupby(['gender'])['imprace'].value_counts()[0].plot.bar()
df.groupby(['gender'])['imprace'].value_counts()[1].plot.bar()

#attractive before date v/s after date
df.groupby(['gender'])['attr1_1','attr1_2'].sum().plot.bar()
plt.legend(['Before Date','After Date'])

