#to covert a space seperated numbers in to 3X3 matrix

import numpy as np
numbers=list(map(int,input("Enter the numbers: ").split()))
nd_arr=np.array(numbers)
print(nd_arr.reshape(3,3))