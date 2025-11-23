# How to create an Array in NumPy from a list and a tuple

import numpy as np

arr_list = np.array([1, 2, 3, 4, 5])

print(arr_list)


arr_tup = np.array((1, 2, 3, 4, 5))

print(arr_tup)

print(type(arr_list))
print(type(arr_tup))