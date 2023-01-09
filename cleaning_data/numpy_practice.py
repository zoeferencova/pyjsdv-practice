# standard way to import numpy
import numpy as np

# everything in numpy is built around its homogenous, multidimensional ndarray object

# adding contents of an array to itself
a = np.array([1, 2, 3])
print(a + a)


# the key properties of the numpy ndarray are its number of dimensions (ndim)
# shape (shape), and numeric type (dtype)

def print_array_details(arr):
    print(
        f'Dimensions: {arr.ndim}, shape: {arr.shape}, dtype: {arr.dtype}')


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

# takes memory block without fill, leaving initialization up to you
empty_array = np.empty((2, 3))
print(empty_array)

# creates a shaped random array with numbers 0 <= x < 1
random_array = np.random.random((2, 3))
print(random_array)

# creates specified number of evenly spaced samples over set interval
# arange is similar but uses step-size argument
linspace_array = np.linspace(2, 10, 5)
# inclusive of upper value (float64 datatype)
print(linspace_array)

arange_array = np.arange(2, 10, 2)
# 2 <= x < 10 with 2 interval
print(arange_array)


# slicing: one-dimensional arrays are indexed and sliced like python lists
a = np.array([1, 2, 3, 4, 5, 6])

print(a[2])  # out: 3
print(a[3:5])  # out: [4, 5]
# every second item from 0-4 set to 0
a[:4:2] = 0  # out: [0, 2, 0, 4, 5, 6]
print(a[::-1])  # out: [6, 5, 4, 0, 2, 0], reversed

# example multi-dimensional array
a = np.arange(16, dtype='int32')
a = a.reshape(2, 2, 4)

# array([[[0, 1, 2, 3],
#        [4, 5, 6, 7]],
#       [[8, 9, 10, 11],
#        [12, 13, 14, 15]]])

print(a[0])  # out: [[ 0 , 1, 2, 3 ], [ 4, 5, 6, 7 ]]
# access first array within second array
print(a[1, 0])  # out: [8, 9, 10, 11]
# from both arrays within the first array, access index 1 to 2
print(a[0, :, 1:3])  # out: [[1, 2], [5, 6]]
# from second array within second array, access all numbers before last
print(a[1, 1, :-1])  # out: [12, 13, 14]


# equivalence
a = np.arange(8)
a.shape = (2, 2, 2)

# array([[[0, 1],
#         [2, 3]],
#        [[4, 5],
#         [6, 7]]])

# compares arrays by shape and elements
a1 = a[1]  # array([[4, 5], [6, 7]])
# : selects all elements in second array
np.array_equal(a1, a[1, :])  # out: True
# selects all elements of all arrays in second array
np.array_equal(a1, a[1, :, :])  # out: True
# taking the first element of the subarrays array([[0, 2], [4, 6]])
# ... selects all arrays, as does :, :
np.array_equal(a[..., 0], a[:, :, 0])  # out: True


# being able to manipulate arrays as easily as single numbers is a
# huge strength of numpy and a large part of its power
a = np.arange(6)
a = a.reshape([2, 3])
# adds 2 to every element in array
a = a + 2
# divides every element by 2 and converts to float
a = a / 2.0
# outputs an array with bool values based on condition
a = a > 2  # out: [ False, False, False, False, True, True ]


# other useful numpy array methods
a = np.arange(8).reshape((2, 4))

# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])

# gets mins from each nested array
a.min(axis=1)  # array([0, 4])
# sums index values at corresponding indexes
a.sum(axis=0)  # array([4, 6, 8, 10])
# gets average along second axis
a.mean(axis=1)  # array([ 1.5, 5.5 ])
# gets standard deviation along second axis
a.std(axis=1)  # array([ 1.11803399,  1.11803399])


# math functions

# trigonometric functions
pi = np.pi
a = np.array([pi, pi/2, pi/4, pi/6])

np.degrees(a)  # radians to degrees
# out: array([ 180., 90., 45., 30.,])

sin_a = np.sin(a)
# out: array([  1.22464680e-16,   1.00000000e+00,
#               7.07106781e-01,   5.00000000e-01])

# rounding
np.round(sin_a, 7)  # round to 7 decimal places
# out: array([ 0.,  1.,  0.7071068,  0.5 ])

# sums, products, differences
a = np.arange(8).reshape((2, 4))
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])

np.cumsum(a, axis=1)  # cumulative sum along second axis
# array([[ 0,  1,  3,  6],
#        [ 4,  9, 15, 22]])

np.cumsum(a)  # without axis argument, array is flattened
# array([ 0,  1,  3,  6, 10, 15, 21, 28])


# custom array function exercise: moving average
# moving average is a series of averages based on a moving window of the last n values where n is a variable

a = np.arange(6)
# array([0, 1, 2, 3, 4, 5])


# function receives array a and number n specifying size of moving window
def moving_average(arr, n=3):
    # use built in cumsum function to calculate cumulative sum of array
    # ret = array([0, 1, 3, 6, 10, 15])
    ret = np.cumsum(arr, dtype=float)
    # starting at nth index of cumsum array, subtract i-nth value for all i
    # i now has the sum of the last n values of a, inclusive
    # ret = array([0, 1, 3, 6, 9, 12])
    # index 5 is now the sum of the window [3, 4, 5]
    ret[n:] = ret[n:] - ret[:-n]
    # return arr([1, 2, 3, 4])
    return ret[n - 1:] / n


test = np.arange(10)
print(f'moving average: {moving_average(test, 4)}')
# out: array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
