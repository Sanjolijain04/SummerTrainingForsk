# without using lambda, map and reduce
'''
items=[]
print("Enter the details : Order Number, Book Title, Author Quantity,  Price per Item ")
while(True):
    new_item=(input(">").split())
    if not new_item:
        break
    else:
        items.append(new_item)
        
print("Order Summary : ")
for element in items:
    if(int(element[4])*int(element[3])<100):
        element[4]=int(element[4])+10
        print((element[0],int(element[4])))
        
    else:
        print((element[0],int(element[4])))
'''
     
#using lambda map reduce
items=[]
print("Enter the details : Order Number, Book Title, Author Quantity,  Price per Item ")
while(True):
    new_item=input(">").split(",")
    
    if new_item == ['']:
        break
    else:
        items.append(new_item)

print(list(map(lambda element: (element[0],int(element[-1])) if((int(element[-1])*int(element[-2]))>=100) else (element[0],int(element[-1])+10), items)))        



