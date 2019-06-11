import numpy as np
import matplotlib.pyplot as plt
#generate random incomes 
incomes=np.random.normal(100.0,20.0,10000)
#draw histogram
plt.hist(incomes,50)
#show histogram
plt.show()
#calculate mean and median
prev_mean=np.mean(incomes)
prev_med=np.median(incomes)

#adding outliers in the data
incomes=np.append(incomes,100000000)
#calculate men and median after adding outliers
after_mean=np.mean(incomes)
after_med=np.median(incomes)


print("Previos mean: ",prev_mean)
print("Previous median: ",prev_med)
print("---")
print("After mean: ",after_mean)
print("After median: ",after_med)


