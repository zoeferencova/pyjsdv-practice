# standard way to import numpy
import numpy as np

# everything in numpy is built around its homogenous, multidimensional ndarray object

# adding contents of an array to itself
a = np.array([1, 2, 3])
print(a + a)


# the key properties of the numpy ndarray are its number of dimensions (ndim)
# shape (shape), and numeric type (dtype)

def print_array_details(arr):
    print(f'Dimensions: {arr.ndim}, shape: {arr.shape}, dtype: {a.dtype}')


a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a)
print_array_details(a)
# returns Dimensions: 1, shape: (8,), dtype: int64


# using the reshape method, we can change the shape and number of dimensions
# reshaping into two dimensional array (two arrays of four)
a = a.reshape([2, 4])
print(a)
print_array_details(a)

# an eight member array can also be reshaped into a three dimensional array
a = a.reshape([2, 2, 2])
print(a)
print_array_details(a)

# the shape and numeric type can be specified on creation of the array or later
# you can change an array's numberic type using the astype method to make a resized
# copy of the original with the new type
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(x.shape)
x.shape = (6,)
print(x)
x = x.astype('int64')
print(x.dtype)

# numpy provides utility functions ot create arrays with a specific shape
a = np.zeros([2, 3])
print(a)
# returns: [[0., 0., 0.], [0., 0., 0.]]
a = np.ones([2, 3])
print(a)
# returns: [[1., 1., 1.], [1., 1., 1.]]
