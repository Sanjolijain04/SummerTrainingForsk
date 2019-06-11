#simpsons phone book
import re

list1=[]
name=[]
with open("simpsons_phone_book.txt", mode='rt') as from_file:
    content=from_file.readlines()
    for item in content:
#        list1.append(item.split())
#    for value in list1:
#        name.append(" ".join(value[:-1]))
#    
#    for item in name:
#        if re.match(r'^[J].*Neu$', item):
#            name_index=name.index(item)
#            print(content[name_index])
        if re.match(r"J.* Neu",item):
            print(item)