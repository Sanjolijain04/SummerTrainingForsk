#teen calculator
items={}
while(True):
    new_value=(input("Enter the key with some integer value: ").split())
    
    if not new_value:
        break
    else:
        items[new_value[0]]=int(new_value[1])

value_list=list(items.values())

def teen_fix(value_list):
    teen_lst=[13,14,17,18,19]
    sum=0
    for items in value_list:
        if items in teen_lst:
            sum+=0
        else:
            sum+=items
    return sum

print(teen_fix(value_list))           
            