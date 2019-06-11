#operations of list
import numpy
from functools import reduce
my_array=list(map(int,(input("Enter array: ")).split()))


#addition
print("Addition: ",sum(my_array))


#multiply
print("Multiplication: ",numpy.prod(my_array))

#print("Multiplication: ",reduce((lambda x,y: x*y),my_array)
#largest
print("Largest: ",max(my_array))

#smallest
print("Smallest: ",min(my_array))

#sorted
print("Sorted: ",sorted(my_array))

#without duplicates
print("Without Duplicates: ",list(set(my_array)))