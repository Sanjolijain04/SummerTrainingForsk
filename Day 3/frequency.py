#frequency occurence

my_string=input("Enter the string: ")

#string to list
list1=[]
for item in my_string:
    if item not in list1:
        list1.append(item)
        
#initialize dictionary
dict1={}

#frequency occurence
for item in list1:
    counter=0
    for value in my_string:
        if(item==value):
            counter+=1
    dict1[item]=counter

print(dict1)