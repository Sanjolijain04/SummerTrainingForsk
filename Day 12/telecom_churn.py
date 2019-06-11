import pandas as pd


#read csv file
data=pd.read_csv("Telecom_churn.csv")

#churned customer availing both plans
churn_count=data.loc[(data['voice mail plan']=='yes') & (data['international plan']=='yes')]['churn'].value_counts()

print("Number of customers availing both voice mail plan and international plan: ",churn_count[1])

#total charge for international call by churned customer and non churned customer
call_charge=data.groupby('churn')['total intl charge'].sum()
visual1=call_charge.plot.pie(autopct='%2.2f%%')

#state having largest intl night calls for churned customers
#make data frame of churn customers
churn_df=data[data['churn']==True]
#max of night intl minutes
night_mins=churn_df['total night minutes'].max()
print(night_mins)

# visualizing types of international calls done by churned users

intl_calls=churn_df.iloc[:,7:19].sum().sort_index()
visual2=intl_calls.plot.bar()

#predict the category of customers having largest account length

nonchurn_al=data['account length'][data['churn']==False].max()
churn_al=data['account length'][data['churn']==True].max()
if(churn_al>nonchurn_al):
    print("Account length of churned customer is max")
else:
    print("Account length if non churned customer is max")
    
#number of calls to customer care by churned customers
customer_care=churn_df['customer service calls'].value_counts()
print(customer_care)

#number of international calls area wisw
area_ppl=data.groupby('area code')['international plan'].value_counts().unstack()
print(area_ppl)




