
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


# Example 2: To grab the top right corner: i.e. 10, 15, 25, 30
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

# Getting bottom row
arr_2d[2]
# or
arr_2d[2,:]



# --------    Fancy Indexing    --------
# Fancy indexing allows you to select entire rows or columns out of order,
#   to show this, let's quickly build out a numpy array:


""" 
    ----    Fancy Indexing    ----
    Fancy indexing refers to the ability to access elements of an array using lists or arrays of indices, 
        rather than sequential or scalar indexing. 
    This is useful when you need to select elements based on specific positions, even out of order.

    Instead of selecting rows or columns one by one, 
        "Fancy Indexing" allows you to provide a list (or array) of row/column indices and extract them all at once.
    
    It's a powerful feature for efficiently manipulating and accessing data. 
"""


#Set up matrix
arr2d = np.zeros((10,10))   # Initialize a 2D array with zeros. This creates a 2D NumPy array (arr2d) with 10 rows and 10 columns, all filled with zeros

#Length of array
arr_length = arr2d.shape[1] # arr2d.shape[1] gets the number of columns in arr2d, which is 10. The result is stored in arr_length.

#Set up array: Populate the array with values:
""" This loop fills each row of arr2d with the value of i. After this loop:

        Row 0 will be [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Row 1 will be [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        Row 2 will be [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

        and so on until row 9. 
"""
for i in range(arr_length):
    arr2d[i] = i

# Fancy Indexing:
# Select rows using specific indices:
# This is an example of fancy indexing, where you select rows based on a list of indices. 
#   Here, rows with indices 2, 4, 6, and 8 are selected. Fancy indexing allows non-sequential row selection.
arr2d[[2,4,6,8]]

# Selecting rows in any order:
# In this case, rows 6, 4, 2, and 7 are selected, but the order of selection doesn’t have to follow any pattern. 
#   Fancy indexing allows you to pick rows or columns in any order.
arr2d[[6,4,2,7]]




# --------    conditional selection    --------
# applying condition will retrun a "boolean array"
    # comparison applied to each values of the array
    # generates "Boolean array"

import numpy as np
arr_3 = np.arange(1, 11)

# following generates Boolean-array
arr_3 < 5   # array of boolean values

# we can apply above "Boolean array" to filter elements form an array 
    # (needs to same-size & shape)
bool_arr3 = (arr_3 < 5)
print(bool_arr3)

# use "boolean-array" to conditionally select the elements of an array
# following returns the elements corresponding "True" values of the "bool_arr3"
arr_3[bool_arr3]

filterArr_1 = arr_3[bool_arr3]
print(filterArr_1)

arr_4 = np.arange(31, 41)
print(arr_4)
filterArr_2 = arr_4[bool_arr3]
print(filterArr_2)

# We can do all above in one line of code
    # notice we used the conditional directly, and 
    # it directly applies the "boolean array" to 'arr_3'
arr_3[arr_3 < 5]

# similarly, following returns the array of elements greater than 7
arr_3[arr_3 > 7]

# We'll use this kind of notations more frequently when we wprk with PANDAS



# Example 3: return the sub-array from following 5x10 matrix (2D array)
                # Notice we used reshape() to make it: 5x10
                # grab the sub-array: [31, 32, 33]
                # grab the sub-array: [[13.14], [23,24]]
arr_2D = np.arange(50).reshape(5, 10)
print(arr_2D)

subArr2D_1 = arr_2D[3, 1:4]
print(subArr2D_1)

subArr2D_2 = arr_2D[1:3, 3:5]
print(subArr2D_2)

# getting column:
subArr2D_3 = arr_2D[:, 1]  # 2nd column
print(subArr2D_3)

subArr2D_4 = arr_2D[:, 3]  # 4th column
print(subArr2D_4)

# Note: useing [:, 1] will return a 1D array
# but [:, 1:2]  will return a 2D array, 
    # an array containing arrays of single element
arr_2D[:, 1:2]
arr_2D[:, 3:4]

