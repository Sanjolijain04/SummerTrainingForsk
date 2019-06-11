# digit letter counter

my_string=input("Enter the string: ")
dict1={}

digit=0
alphabet=0
for item in my_string:
    if(item.isdigit()==True):
        digit+=1
    elif(item.isalpha()==True):
        alphabet+=1

dict1["Alphabet"]=alphabet
dict1["Digit"]=digit

print(dict1)