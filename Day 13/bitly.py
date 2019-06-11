#import pandas to create dataframe
import pandas as pd

#import matplotlib for visuals
import matplotlib.pyplot as plt

#import numpy to find missing values oe null values\
import numpy as np

#import counter class to find frequency
from collections import Counter 

#using exception handling
#try block
try:
    #create dataframe
    #pandas convert json string into json object
    #lines reads each line of file as json object
    json_df=pd.read_json('usagov_bitly_data.json', lines=True)
    
    #replace the nan values with Missing and "" with none
    json_df=json_df.replace([np.nan,""],["Missing","Unknown"])
    
    #top 10 time zones frequency using pandas
    json_df_tz=json_df['tz'].value_counts().head(10)
    
    #time zones frequency without using pandas
    tz_fre=Counter(json_df['tz'])
    
    #plot graph of top 10 time zones in series series.plot().type()
    json_df_tz.plot().bar()
    
    #seperate browser capability
    token_df=json_df['a'].str.split(n=1, expand=True).add_prefix('Token_')
    
    #token counnts
    token_counts=token_df['Token_0'].value_counts()
    
    #plot graph of top 5 token
    token_counts.plot().bar()
    
    # add new column named os in dataframe
    #initialize column with not windows
    token_df['OS']="Not Windows"
    
    #now chnage rows according to compatability\
    token_df['OS'][token_df['Token_1'].str.find("Windows") != -1]='Windows"
    
    
    
    
    


except ValueError as e:
    print(e)

except AttributeError as e:
    print(e)

except TypeError as e:
    print(e)    