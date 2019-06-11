# using map reduce and filter
from functools import reduce

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
'''
# fucntion to filter the entries without height given
def check_height(item):
    if 'height' in item:
        return True
    else:
        return False
    
#function to find total height
def reduce_list(ht_one,ht_two):
    return ht_one + ht_two

#filtered list
filtered_list=list(filter(check_height,people))

#height list
height_list=[]
for item in filtered_list:
    height_list.append(item['height'])
print(height_list)

#reduce to find total height
total_height=reduce(reduce_list,height_list)
print(total_height)

'''

#print("Average = ",(reduce(lambda x,y: x+y,list(map(lambda item: item['height'] ,list(filter(lambda item : True if 'height' in item else False,people))))))/len(list(filter(lambda item : True if 'height' in item else False,people))))
print("Average = ",(reduce(lambda x,y: x+y,list(map(lambda item: item['height'] ,list(filter(lambda item : True if 'height' in item else False,people))))))/len([i for i in people if "height" in i]))