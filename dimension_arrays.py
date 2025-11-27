# Program to create and display arrays of different dimensions using NumPy
import numpy as np

arr_0d = np.array(42)

print(arr_0d)

arr_1d = np.array([1, 2, 3, 4, 5])

print(arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d)

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr_3d)

# Check the number of dimensions
print("Number of dimensions:")
print("0D array:", arr_0d.ndim)
print("1D array:", arr_1d.ndim)
print("2D array:", arr_2d.ndim)
print("3D array:", arr_3d.ndim)