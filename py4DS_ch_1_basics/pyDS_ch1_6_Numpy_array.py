
################# 3.9: full
# copy:  
#        
#        
################# (28-oct-23 for 29-oct-23)

# Courses: A-Z PY for Data-Science    3.8, 3.9


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


