import pandas as pd
import numpy as np

data=pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv')

grouped_data=data.groupby(['JobTitle','AnnualSalary'])
total= grouped_data.sum()
agg=grouped_data.mean()

#maximum salary
highest_salary=data['AnnualSalary'].max()


#group data with Job title
grouped_data=data.groupby('JobTitle')
sorted(grouped_data.keys())

#plot value of top 10 job titles
(data['JobTitle'].value_counts())[0:10].plot('bar')



