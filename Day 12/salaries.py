#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#make dataframe of given csv file
data=pd.read_csv("Salaries.csv")

#maximum salary
max_salary=data.groupby('sex')['salary'].max()
#minimum salary
min_salary=data.groupby('sex')['salary'].min()

#making dataframe of professer
prof_df=data[data['rank']=='Prof']

#prof with max salary
prof_max_salary=prof_df.groupby('sex')['salary'].max()
#prof with minimun salary
prof_min_salary=prof_df.groupby('sex')['salary'].min()

#managing missing salaries with the mean of salaries with same service

#mean of salaries with service A
a=data[data['discipline']=='A']['salary'].mean()
#mean of salaries with service B
b=data[data['discipline']=='B']['salary'].mean()

#filling null salaries with mean
data['salary'][data['discipline']=='A']=data['salary'].fillna(a)
data['salary'][data['discipline']=='B']=data['salary'].fillna(b)

#calculating mean of phd for respective discipline
a1=data[data['discipline']=='A']['phd'].mean()
b1=data[data['discipline']=='B']['phd'].mean()

#filling the mean at null places
data['phd'][data['discipline']=='A']=data['phd'].fillna(a1)
data['phd'][data['discipline']=='B']=data['phd'].fillna(b1)

#pie chart with % of sex ratio
gender_df=pd.DataFrame(data['sex'].value_counts())
visual1=plt.pie([gender_df['sex']['Male'],gender_df['sex']['Female']], explode=[0,0],colors=['blue','yellow'], labels=['Male','Female'],autopct='%1.1f%%')
visual1.show()

#pie chart of rank of persons
rank_df=pd.DataFrame(data['rank'].value_counts())
visual2=plt.pie([rank_df['rank']['Prof'],rank_df['rank']['AsstProf'],rank_df['rank']['AssocProf']],explode=[0,0,0], colors=['red','green','blue'],labels=['Prof','AsstProf','AssocProf'],autopct='%1.1f%%')
visual2.show()


#senior most employee
print("Senior most employee: ")
print(data[data['service']==data['service'].max()])

#junior most employee
print("Junior most employee: ")
print(data[data['service']==data['service'].min()])

#histogram for salaries
plt.hist(data['salary'],bins=range(50000,190000,15000))
plt.title("Salary Representation")
plt.xlabel("Number of employee")
plt.ylabel("Salaries")
plt.grid(True)



