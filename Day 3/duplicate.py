# duplicate 

list1=[40,30,23,48,56,24,23,48,40,110,90,35,56]
list2=[]
#removing duplicates
for item in list1:
    if item not in list2:
        list2.append(item)
        
        
#reverse sequence
list2.reverse()
print(list2)

        