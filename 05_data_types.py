import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

# Creating Arrays With a Defined Data Type

arr2 = np.array([1, 2, 3, 4], dtype='S')

print(arr2)
print(arr2.dtype)

# We can define size as well

# Create an array with data type 4 bytes integer:

arr3 = np.array([1, 2, 3, 4], dtype='i4')

print(arr3)
print(arr3.dtype)