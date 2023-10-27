
################# 3.8: 3:42
# copy:  
#        
#        
################# (27-oct-23 for 28-oct-23)

# Courses: A-Z PY for Data-Science    3.8,


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

