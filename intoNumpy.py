import numpy as np

# 1d numpy array
arr = np.array([1,2,3,4,5])

# 2d array
arr = np.array([(1,2),(3,4),(5,6)])

print(arr)



# numpy array uses less memory, faster and convinient compared to list

import time 
import sys

a1 = range(10000)

print(sys.getsizeof(5)*len(a1)) # memory occupied buy list

a2 = np.arange(10000)

print(a2.size*a2.itemsize) # memory occupied by numpy (less)

