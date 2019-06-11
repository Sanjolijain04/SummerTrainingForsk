# most frequent without using numpy

import numpy as np
from scipy import stats
#start, end,no_of_elements
random_num=np.random.randint(5,15,40)

# most frequent using numpy
most_freq=stats.mode(random_num)
print(most_freq)

#most frequent without using numpy
from collections import Counter
#using counter class
frequency=Counter(random_num)
#most common will give the key value pair with max occurence
most_comm=frequency.most_common(1)
print(most_comm)
#it will give output in form of list containg a tuple of key value pair
print(most_comm[0][0])