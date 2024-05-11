
# Courses: 
    # A-Z PY for Data-Science    3.8, 3.9
    # PrTla PY for DS & ML : 5.1, 5.2, 5.3



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-      A-Z py4ds      -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ---------    Numpy and Arrays    ---------

# arrays are similar to list

# there are 2 ways to use arrays in Python
    # python built-in arrays: array.array
    # use NumPy packae's array

# Python built-in arrays
from array import array

# the built-in array.array is good but a 'Numpy array' has more flexibility

# NumPy array
import numpy as np

# np.array() will convert a list into an "numpy-array"
ls = [12, 45, 78, 98]
type(ls)    # <class 'list'>

np_arr = np.array(ls)
type(np_arr)    # <class 'numpy.ndarray'>


# -------------    array vs list    -------------
# an array "Cannot support different data-types"
    # if we use a lsit of mixed data-types, 
        # all element will converted to a single data-type
        
b = np.array([12, 56.0, 67])    # mixed int and float
b   # all element will converted to "float": array([12., 56., 67.])

d = np.array([12, 56.0, 67, True, "Hello!"])    # mixed int and float
d   # all element will converted to "string"
# array(['12', '56.0', '67', 'True', 'Hello!'], dtype='<U32')

# similar to "list-object" an 'array-object' contains many useful functions
# we use 'array' insted of 'lists' because in data-science we'll work with multi-dimentional arrays




# ---------    Slicing the ARRAY    ---------
# The operation is similar to lists
import numpy as np
a = np.array([23245, 27, 546, 215, -1234]) 
a[2:]   # array([  546,   215, -1234])
a[2:4]  # array([546, 215])

# what's the diffeence ?
# in list-slicing new list is created during slice (i.e new instance is craeted)
# in array-slicing no-new list is crated
    # it's just a viewing window
    # if we assigne the array to new variable, it's still connected to the old instance
    # to copy an array we use 'array.copy()' method

b = a

# updating b
b[1] = 11235
b   # array([23245, 11235,   546,   215, -1234])

# notice a is changed too
a   # array([23245, 11235,   546,   215, -1234])

# this is because array is stored in memory as one copy, to save some space
    # that's why 'array' is more faster than 'list'
    # 'array' will take less memroy than 'list'

c = b[2:4]
c[:] = 111
# a & b both changed
b   # array([23245, 11235,   111,   111, -1234])
a   # array([23245, 11235,   111,   111, -1234])
c   # array([111, 111])

# creating a copy
copy = a.copy()
copy[1] = 0000
copy    # array([23245,     0,   111,   111, -1234])
# notice a is unchanged
a   # array([23245, 11235,   111,   111, -1234])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-






# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-      PrTla PY for DS & ML      -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# We'll focus on NumPy array

# Numpy arrays essentially come in two flavors: 
#         vectors
#         matrices

# Vectors are strictly 1D arrays and 
# matrices are 2D (but a matrix can still have only one row or one column).

""" 
    NumPy (or Numpy) is a Linear Algebra Library for Python.
    Almost all of the libraries in the PyData Ecosystem created based on NumPy
    Numpy is also incredibly fast, as it has bindings to C libraries.

    install numpy:
        conda install numpy
        pip install numpy 
"""

# numpy array from a python object (such as: list)
# convert a list to a numpy array
my_list = [1, 2, 3]
my_list

import numpy as np
np.array(my_list)

arr = np.array(my_list)
arr


# 2D - array: cast a list of lists to the np.array()
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat)




# --------    numpy methods to gnertae arrays    --------
# use numpy's built-in array generator methods (faster)
# following are some common ways to do that:
        # from a list 
        # arange()
        # zeros()
        # ones()
        # linspace()
        # eye()
        # random.rand()
        # random.randn()
        # random.randint()

# --------    arrange()    --------
# np.arrange(start, stop, step) - most common & quick
    # its similar to range() method
np.arange(0, 10)

np.arange(0, 11, 2)

# for more specific type of array we can use following

# array of all 0
np.zeros(3)     # 1D
# use tuple to generate higher dimensional array
np.zeros((2,3)) # 2D by (row, column)

# array of all 1
np.ones(3)     # 1D
np.ones((3,4)) # 2D by (row, column)


# easy way to understand multi-dimensional array:
    # notic e the number of square-brackets []
    # [] - 1D
    # [[]] - 2D
    # [[[]]] - 3D


# --------    linspace()    --------
# it returns evenly spaced numbers between intervals
# difference between "arange() vs linspace()"
    # arange(): 3rd argument is the step-size
        # arange(start, end, stepSize)
    # linspace(): 3rd argument is number of "equally spaced points between start and end"
        # linspace(start, end, noumberOfPoints)

# 10 evenly spaced points between 0 and 5
np.linspace(0, 5, 10)
np.linspace(0, 5, 100)  # 100 points

# "Identity matrix" using numpy
np.eye(4)   # gives 4x4 identity matrix




# ------------    random numbers    ------------
# there are lots of ways to create an array of random numbers
# ----  np.random.rand()  ----
    # array of given-shape of matrix with 
    # random nubers from uniform distribution over "0 to 1"

# 1D array of 5 random numbers
np.random.rand(5)
# unlike oprevious functions, in this case we don't need to pass the tuples
    # we directly pass the size (dimensions) in seperate arguments
np.random.rand(5,5)     # 5x5 matrix of random numbers


# 'sample' or "many samples" from GAUSSIAN or standared NORMAL distributions
    # instead of rand() we use randn()
    # this will retun numbers from "standared NORMAL distribution" centered around 0
    # instead of UNIFORM distribution over "0 to 1"
np.random.randn(2)
# we'll visualize GAUSSIAN or standared NORMAL distributions curves later
np.random.randn(2,4)    # 2x4 matrix of random numbers from std normal distribution
# notice agin we didn't use tuples here

# ----  randint()  ----
# returns random integers for a LOW (inclusive) to HIGH (exclusive) 
    # for a given size (how many numbers)
    # i.e. it returns n random numbers for a given "range" and "size=n"
np.random.randint(1,100)    # returns a random number between 1 and 100
np.random.randint(1,100, 10)    # returns 10 random numbers between 1 and 100

# we can also import a specific function from the "random" as below
from numpy.random import randint
randint(2,10)


# --------    "attributes" and "methods" of an array    --------
        # reshape()
        # max / min value 
        # index-location of max/min
        # shape info
        # data-type
        
arr_1 = np.arrange(25)
rand_arr_1 = np.random.randint(0, 50, 10)

# ----  reshape()  ----
# returns a new array of same data with new shape
# reshapes the 1D arry "arr_1" to a 2D 5x5 array using reshape(row, column)
arr_1.reshape(5,5)  
# notice, reshape() is a method of object "arr_1"
# youll get ERR if you won't fill out the matrix completely
    # i.e. the 1D matrix must fit into the 2D matrix
    # following gives an Value-ERR, 
        # becausewe're trying to fit a 25 size 1D matrix into 50 size 2D
arr_1.reshape(5,10) 
# ValueError: total size of new array

# to check: row*column = total size


# ----  max / min values & their index location  ----
# find the max / min value of "rand_arr_1"
rand_arr_1.max()
rand_arr_1.min()

# to return the index-location of max/min, use: argmax() and argmin()
rand_arr_1.argmax()
rand_arr_1.argmin()

# ----  shape info  ----
# we use "shape" attribute, (it's not a method)
arr_1.shape 
# the comma in (25,) indicating it's a 1D vector

# following, we converted it to a 5x5 2D matrix
arr_2 = arr_1.reshape(5,5)  
arr_2.shape
# returns (5,5) i.e. it's 2D now


# ----  data-type info  ----
# to get the datatype of an array use "dtype" attribute
arr_2.dtype

