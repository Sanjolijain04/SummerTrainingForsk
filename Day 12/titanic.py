# titanic problem

import pandas as pd

#read csv file
df=pd.read_csv("training_titanic.csv")

#count the number of enties in survived column
survived_count=df['Survived'].value_counts()

#print the count of survived people and died people
print("Number of prople survived: ",survived_count[1])
print("Number of people died: ",survived_count[0])

#find % survived by setting normalize=True
survived_pct=df['Survived'].value_counts(normalize=True)

#print the % of people died and survived
print("% of people survived: ",survived_pct[1]*100)
print("% of people died: ",survived_pct[0]*100)

#calculate number of mens died and number of mens survived

#select the Survived column for only mens
mens_count=df.loc[df['Sex']=='male']['Survived'].value_counts()

print("Number of mens survived: ",mens_count[1])
print("Number of mens died: ",mens_count[0])

# add new column child to data frame
#fill 0 if age > 18 else fill 1
df['Child']=df['Age'].map(lambda x: 1 if(x<18) else 0 )

#count of child which survived
child_survival=df['Child'][df['Survived']==1].value_counts(normalize=True)
print("% of child survived: ",child_survival[1]*100)
print("% of people with age>18 survived: ",child_survival[0]*100)


