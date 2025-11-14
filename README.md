# Mastering Numpy with Hand on Examples in Python

Learn NumPy

NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".

It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

The source code for NumPy is located at this github repository https://github.com/numpy/numpy

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called `ndarray`, it provides a lot of supporting functions that make working with ndarray very easy.

NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

`pip install numpy`

Create an alias with the as keyword while importing:

`import numpy as np`

`print(np.__version__)`

To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray

`arr = np.array([1, 2, 3, 4, 5])`

### 0-D Arrays

0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

### 1-D Arrays

An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

### 2-D Arrays

An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.

### 3-D Arrays

An array that has 2-D arrays (matrices) as its elements is called a 3-D array.
