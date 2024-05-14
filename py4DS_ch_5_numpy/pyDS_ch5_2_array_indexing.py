
################# 5.4: 7:2
# copy:  
#        
#        
################# (12-may-24 for 14-may-24)

# Courses: 
    # PrTla PY for DS & ML : 5.4, 5.5


# --------    numpy array indexing    --------
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




# indexing of 2D array (matrix)

