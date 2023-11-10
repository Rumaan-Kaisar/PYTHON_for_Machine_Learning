
################# 4.3: 10:10
# copy:  
#        
#        
################# (8-nov-23 for 10-nov-23)

# Courses: A-Z PY for Data-Science    4.2, 4.3, 4.4, 4.5


# since we'll work with data-frames in Data-science, we need to understand MATRICES


# --------------    Matrix INDEXATION in python    --------------

# locate a single element in a 2D matrix
# matrix[row, column], and both start from 0
A[2, 3]     # an elemnt from 3rd-row and 4-th column


# locate a ROW      matrix[row, : ]
A[1, :]     # 2nd row


# locate a COLUMN   matrix[ :, col]
A[:, 3]     # 4th column




# --------------------    Our First Matrix    --------------------
# Import numpy
# Create a List-of-Lists
# convert the to 2D-array (matrix) using 'np.array'

import numpy as np

a = [.00, .01, .02]
b = [.10, .11, .12]
c = [.20, .21, .22]

mat_1 = np.array([a, b, c])




# --------------    creating a matrix    --------------

# method 1: np.reshape( data , dim , 'C')
    # matrix will be populated row-by-row 
        # in R column-by-column

    # C: it means C-programming (default)
        # C-like matrix-population (row-by-row)

    # F: it means FORTRAN-programming
        # FORTRAN-like matrix-population (column-by-column)
        # np.reshape( data , dim , 'F')
 


# method 2: np.array()
    # it puts row into matrices
        # it combines data into matrices




# np.reshape(data, (row, column))
import numpy as np
mydata = np.arange(0, 20) # create a list of 20 numbers
print(mydata)
type(mydata)    # numpy.ndarray

np.reshape(mydata, (4, 5))

# applying order-flags 'F', 'C'
mat_1 = np.reshape(mydata, (4, 5), order='C')
mat_2 = np.reshape(mydata, (4, 5), order='F')

# Notice how the matrices populated!!
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])

array([[ 0,  4,  8, 12, 16],
       [ 1,  5,  9, 13, 17],
       [ 2,  6, 10, 14, 18],
       [ 3,  7, 11, 15, 19]])


# getting individual element
print(mat_1[2, 4])  # 14
print(mat_2[2, 4])  # 18


# Note :
""" 
    arange([start,] stop[, step,], dtype=None, *, like=None)
        Return evenly spaced values within a given interval.
        the interval including 'start' but excluding 'stop'
    python pyDS_ch3_2_mtrix_dict.py 
"""




# ------------------    using ordinary-list    ------------------

# creating matrices from a list (no 'numpy.ndarray' TYPE)
import numpy as np
mydata_2 = range(20) # create a list of 20 numbers
print(mydata_2)
type(mydata_2)    # numpy.ndarray

np.reshape(mydata_2, (4, 5))

# applying order-flags 'F', 'C'
mat_1 = np.reshape(mydata_2, (4, 5), order='C')
mat_2 = np.reshape(mydata_2, (4, 5), order='F')

# getting individual element
print(mat_1[2, 4])  # 14
print(mat_2[2, 4])  # 18

# To avoid using 'numpy.ndarray' object we've used ordinary-list




# ------------------    OOP concept    ------------------
import numpy as np
mydata = np.arange(0, 20) # create a list of 20 numbers
# Note:
# since 'np.arange(0, 20)' will create a 'numpy.ndarray' TYPE object
# and this object already has "reshape" method, we can directlt use:
mydata.reshape((5, 4))

