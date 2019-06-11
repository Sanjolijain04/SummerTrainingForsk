import numpy as np
import matplotlib.pyplot as plt
#generate random data
random_data=np.random.normal(150.0,20.0,1000)
#draw histogram with bucket size 100
plt.hist(random_data,100)
plt.show()

#calculate standard deviation
print("Standard Deviation: ",np.std(random_data) )
#calculate variance
print("Variance: ",np.var(random_data))
