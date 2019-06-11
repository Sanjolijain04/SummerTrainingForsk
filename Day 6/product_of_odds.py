# product of odd numbers in a list

from functools import reduce
input_list=list(map(int, input("Enter the list elements: ").split()))

print(reduce( lambda one, next: one*next,list(filter(lambda x: True if(x%2!=0) else False, input_list))))