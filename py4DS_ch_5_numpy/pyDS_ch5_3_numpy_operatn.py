
################# 5.6: full, 5.7: full, 5.8: 00.55
# copy:  
#        
#        
################# (01-jun-24 for 02-jun-24)

# Courses: 
    # PrTla PY for DS & ML : 5.6, 5.7(ex), 5.8(ex-soln) 


# ------------    numpy OPERATIONS    ------------
# Basic operations we perform on numpy array
    # Array with Array 
    # Array with Scalars 
    # Universal Array Functions

import numpy as np
arr = np.arange(0,11)
print(arr)


# ------    Array with Array    ------
# we can do simple arithmetic operation with two array
# following adds "element-by-element" basis
arr + arr

# similarly we can do subtraction and multiplication
arr - arr
arr * arr
arr**2      # exponents

# ------    scaler operation    ------
# numpy basically broadcast the scaler to every element 
# the operation occured in also "element by element"

arr + 100
arr / 100
arr * 100


# --------    numpy warning    --------
# dividing elements by 0 cause ERROR in "python"
# but "numpy" gives a warning instead of ERROR
# so be careful about having 0 in your dataset
1/0     # gives ERROR in python: ZeroDivisionError

# numpy gives an "warning" but no ERROR
    # notice the first element of the "arr" is 0 and 
    # 0/0 will give a ERROR in python
    # but in "numpy" we'll get an warning instead
        # it will return "nan" for 0/0 in numpy

arr / arr       # Runtimewarning: invalid value encountered in true_divide

# following returns 'inf' (infinity) for the first element when performing '1/0'
1 / arr


# --------    universal array function    --------
# universal array functions are just mathematical operations
# perform-operation & broadcast over array
np.sqrt(arr)    # square root
np.exp(arr)     # e^n : calculates exponent e**n for each array element

np.max(arr)     # maximum using numpy method
# alternatively
arr.max()       # maximum using builtin array method/property

# ----  trigonometric functions  ----
np.sin(arr)     # gets the sin value element-wise

# ----  logarithmic value  ----
# NOTE: for 0, we'll get "-ve inf" and a RuntimeWarning for "divide by 0"
np.log(arr)     # gets the "e"-based-log, i.e. ln() value element-wise

# more universal array functions:
# befor implementing your own function it's good to check if it's already built-in numpy function

# visit numpy documentation: Universal Functions (ufunc)
    # https://numpy.org/doc/stable/reference/ufuncs.html
    # math operations
    # triginimetric functions
    # advance functions: max, min, comparison etc




# ------------    NumPy Exercises    ------------
# FOR MORE EXERCISE: https://www.w3resource.com/python-exercises/numpy/

# create zeros, ones, scalar multiplication
# array of integers
# 2D matrix
# identity matrix
# random numbers matrix
# evenly spaced numbers

# ----    Numpy indexing and selections    ----
# reshape
# select parts of matrix 
# array functions


# Import NumPy as np
import numpy as np

# Create an array of 10 zeros 
np.zeros(10)
np.zeros((2, 5), dtype=int)
np.zeros((5, 2), dtype=float)


# Create an array of 10 ones
np.ones(10)
np.ones((2, 5), dtype=int)
np.ones((5, 2), dtype=int)


# Create an array of 10 fives
5*np.ones(10)


# Create an array of the integers from 10 to 50
np.arange(10, 51)


# Create an array of all the even integers from 10 to 50
# TRICK: use increment or stepSize
np.arange(10, 51, 2)
# notice, we use 51, because the endpoint is excluded


# Create a 3x3 matrix with values ranging from 0 to 8
arr1 = np.arange(0, 9)
arr1.reshape(3, 3)
# we can do that in single line
np.arange(0, 9).reshape(3, 3)


# Create a 3x3 identity matrix
# note that we don't need to specify 3x3 by (3, 3)
# since identity matices are always square, we just use: np.eye(3)
# np.eye(3, 3)
np.eye(3)


# ----  random numbers  ----
# Use NumPy to generate a random number between 0 and 1
np.random.rand()    # rand() uses uniform distribution
np.random.rand(1)    # gives an array containing one random number


# Use NumPy to generate an array of 25 random numbers sampled from a "Standard Normal Distribution"
np.random.randn(25)


# Create the following matrix:
""" 
array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])

"""
# 100 evenly spaced points between 0 and 1
np.arange(0.01, 1.01, 0.01).reshape(10, 10)
# alternatively
np.linspace(0.01, 1, 100).reshape(10, 10)
# we can also do:
np.arange(1,101).reshape(10,10) / 100   # similar to firsat approach


# Create an array of 20 linearly spaced points between 0 and 1:
np.linspace(0, 1, 20)



# ----  Numpy Indexing and Selection  ----
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
""" 
    array( [[ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]] )

"""
mat = np.arange(1,26).reshape(5,5)
mat


# write code that reproduces the output as:
""" 
    array(  [[12, 13, 14, 15],
             [17, 18, 19, 20],
             [22, 23, 24, 25]]  )
"""
subArr2D_1 = mat[1:, 1:]
print(subArr2D_1)


# select "20" from the above matrix
mat[3, -1]
mat[3, 4]   # ALTERNATIVE


# get following
""" 
    array( [[ 2],
            [ 7],
            [12]]) 
"""
mat[:3, 1]  # gets as 1D array 
mat[:3, 1:2]  # returns the column as 2D array 


# get: array([21, 22, 23, 24, 25])
mat[4, :]


# get:
""" 
    array( [[16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]])
"""
mat[3:, :]
mat[3:5, :]  # alternative. Notice we exceed the last-index of "mat"


# ----  numpy: universal array functions  ----
# Get the sum of all the values in mat
mat.sum()

# Get the standard deviation of the values in mat
    # numpy.std()
    # std = sqrt(mean(x)) , where x = abs(a - a.mean())**2
mat.std()

# Get the sum of all the columns in mat
    # axis=1 for row-wise sum
    # axis=0 for column-wise sumn
mat.sum(axis=1)     # sum the rows
mat.sum(axis=0)     # sum the columns

