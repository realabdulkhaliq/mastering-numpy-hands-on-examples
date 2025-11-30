import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0]) # 1

print(arr[1]) # 2

# Array indexing is the same as accessing an array element.

print(arr[2] + arr[3]) # 3 + 4 = 7

arr_2d = np.array([[1,2,3,4,5], 
                   [6,7,8,9,10]])

print('2nd element on 1st row: ', arr_2d[0, 1]) # R C -> 2
print('5th element on 2nd row: ', arr_2d[1, 4]) # R C -> 10

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr_3d[0, 1, 2]) # 6