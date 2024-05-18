
################# 5.4: ok, 5.5: 13.00
# copy:  lecture notebooks (3)
#        
#        
################# (17-may-24 for 18-may-24)

# Courses: 
    # PrTla PY for DS & ML : 5.4, 5.5


# --------    numpy array indexing and selection    --------
# we'll see how to index and slice numpy arrays
    # it works exactly like a normal Python list

# Objective: How to select elements or group certain elements from a Numpy array

import numpy as np

arr_1 = np.arrange(11) # numpy array of 11 elements
arr_1

# we'll use [], and slice using ':' just like python normal list
arr_1[10]   # gets the value at index 10

# use slice notation [start(inclusive) : stop(exclusive)]
arr_1[1:5]
arr_1[0:6]

# everything UPTO 
arr_1[:6]   # same as arr_1[0:6]

# start and UPTO END [start(inclusive) : ]
arr_1[6:]



""" 
    Just like a "normal Python list", indexing starts at zero in Numpy arrays. 
        Therefore, the arr[5:] notation actually grabs everything starting with the index 5.
"""




# --------    BROADCAST ability    --------
# numpy Array differ from python list because of BROADCAST ability 

# Example 1: if we try to assign elements from 0 to 4 as below:
arr_1[0:5] = 100
# It'll broadcast the value 100 to all the 5 elements from index 0 to 4
print(arr_1)
# [100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10]

# ----  slice and BROADCAST  ----
# altering slice of an array will affect the main array
arr_2 = np.arange(0, 11)
slice_of_arr_2 = arr_2[0:6]

# apply broadcast on slice_of_arr_2 for all of its element
slice_of_arr_2[:] = 99
print(slice_of_arr_2)
# notice the main array "arr_2" is also changed
print(arr_2)

# Reason: The reason is numpy array tahes up memeory, 
    # for saving memory it's slice refer to the original array

# ----  copy()  ----
# if we want a COPY (not refering original array) we have to use copy() method
arr_2_copy = arr_2.copy()
arr_2_copy[0:6] = 0
print(arr_2_copy)
# notice now "arr_2" is not changed
print(arr_2)




# --------    indexing of 2D array (matrix)    --------
import numpy as np

# to crearte a 2D numpy array we use a list of list (nested list)
arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)

# There are "two general formats" to access the element of a 2D array
    # [row][column]-format
    # [row, column]-format (recommend to use)

# ----  [row][column]-format  ----
arr_2d[0][0]    # 5
arr_2d[0]       # gives entire row
arr_2d[1][1]    # 25
arr_2d[2][1]    # 40
arr_2d[1][2]    # 30


# ----  [row, column]-format  ----
    # recommened to use
arr_2d[2, 1]    # 40
arr_2d[1, 2]    # 30

# ----  sub-matrix: chunks of an array  ----
# getting "part of an array" instead of single element
# use slice: to retun a sub-matrix from a matrix we use ":"
"""
        [ 5,10,15],
        [20,25,30],
        [35,40,45]
"""
# Example: To grab the top right corner: i.e. 10, 15, 25, 30
arr_2d[:2]          # gets the first 2 row
# arr_2d[:2][1:]      # won't gets the first 2 row and then last two columns

# If you want to use the arr_2d[row][column] format instead of slicing directly, 
#   you can use list-comprehension

# Note that this approach is different from slicing and may not produce the desired result directly.
# Grab the top right corner using arr_2d[row][column] format
top_right_corner = arr_2d[:2]
top_right_corner = [row[1:] for row in top_right_corner]

# Convert the list of lists to a NumPy array
# array = np.array(list_of_lists)
top_right_corner = np.array(top_right_corner)
print(top_right_corner)

# or we can use other format
arr_2d[:2, 1:]  
# ':2' = grabs all rows upto index-2 (excluding 2)
# '1:' = grab all columns from index 1 (including 1)


# --------    conditional selection    --------


