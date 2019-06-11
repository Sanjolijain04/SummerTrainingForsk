# Shopping list mini project

shopping_list=[]
shopping_list2=[]

print("What should we puck up at the store?")
print("Enter 'DONE' to stop adding items.")

#defining function
    
def shopping():
    while(True):
       
        #input item
        item=input("> ").lower()
        if(item=='done'):
            break
        elif(item=='show'):
            for value in shopping_list:
                print(value)
            break
        elif(item=="help"):
            print("Enter 'SHOW' to see your shopping_list")
            print("Enter 'DONE' to stop adding items")
            break
        else:
            shopping_list.append(item)
    return shopping_list

#defining function
def shopping1():
    list1=(input("Enter shpooing list: ").split(","))
    for item in list1:
        if(item.lower()=="done"):
            break
        elif(item.lower()=="show"):
            print(shopping_list2)
            break
        elif(item.lower()=="help"):
            print("Enter 'SHOW' to see your shopping_list")
            print("Enter 'DONE' to stop adding items")
            break
        else:
            shopping_list2.append(item)
    return shopping_list2
            
    
#printing item serially
print(shopping())
print(shopping1())
#printing items in the shopping list

print("Here's your list")
 
for item in shopping_list:
    print(item) 
    
#storing thre liost into the file
with open("shopping_list.txt", mode='w') as file1:
    for item in shopping_list:
        file1.write(item+"\n")
        
