import pandas as pd
import os

#get path of current working directory
path=os.getcwd()
#list files present in current working directory
files=os.listdir(path)

#create a list of file names
files_list=[]
for item in range(0, len(files)):
    #append the files in list that ends with .txt format
    if files[item].endswith('txt'):
        files_list.append(files[item])
 
#make dataframe using that list
data=pd.DataFrame(columns=['Name', 'Sex','Frequency','Year'])
#add data of each year as column
for year in range(1880,2011):
    #compare each file
    for file in files_list:
        if(file=='yob'+str(year)+'.txt'):
            #open file
            file_data=open(file)
            lst=file_data.splitlines()
            print(lst)

#take column of year 2010
#make a list of list of data in 2010

    
        
        