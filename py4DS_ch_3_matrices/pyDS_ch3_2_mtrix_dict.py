
################# 4.2: FULL
# copy:  
#        
#        
################# (7-nov-23 for 8-nov-23)

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
# convert the to 2D-array (matrix) using np.array

import numpy as np

a = [.00, .01, .02]
b = [.10, .11, .12]
c = [.20, .21, .22]

mat_1 = np.array([a, b, c])


# python pyDS_ch3_2_mtrix_dict.py
