# Pallindromic integer
list1=(input("Enter the list of integrs: ")).split()
list2=[]

def check_pallindrome(item):
    reverse=item[::-1]
    if(reverse==item):
        list2.append(True)
    else:
        list2.append(False)


for item in list1:
    check_pallindrome(item)
    



#check list 2
if True in list2:
    print(True)
else:
    print(False)
    
    
    
