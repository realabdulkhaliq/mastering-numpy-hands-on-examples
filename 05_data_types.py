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


# A non integer string like 'a' can not be converted to integer (will raise an error):

arr4 = np.array(['a', '2', '3'], dtype='i') # Error

# Converting Data Type on Existing Arrays
arr5 = np.array([1.1, 2.1, 3.1])

newarr = arr5.astype('i')

print(newarr)
print(newarr.dtype)

newarr1 = arr5.astype(int) # Change data type from float to integer by using int as parameter value
print(newarr1)
print(newarr1.dtype)