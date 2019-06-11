# vowel founder

#list intake
state_names=["Alabama", "California","Oklahoma", "Florida"]

output_list=[]
for state in state_names:
    str1=''
    for alphabet in state:
        if alphabet not in 'aeiouAEIOU':
            str1=str1+alphabet

    output_list.append(str1)
         
print(output_list)
         

'''
name = "Sanjoli"
str1 = ""

for item in name:
    if item not in "aieou":
        str1 = str1+item
'''