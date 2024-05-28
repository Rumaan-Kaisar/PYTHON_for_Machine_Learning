
################# 5.6: full, 5.7: full
# copy:  
#        
#        
################# (26-May-24 for 28-May-24)

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
np.arange(10, 50)

# Create an array of all the even integers from 10 to 50
# TRICK: use increment
np.arange(10, 50, 2)

# ----  rev[26-may-24]  ----
#### Create a 3x3 matrix with values ranging from 0 to 8
