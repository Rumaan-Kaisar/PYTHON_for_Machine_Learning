
################# 5.4: 3:40
# copy:  
#        
#        
################# (8-may-24 for 10-may-24)

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



# numpy Array differ from python list:
""" 
    Just like a "normal Python list", indexing starts at zero in Numpy arrays. 
        Therefore, the arr[5:] notation actually grabs everything starting with the index 5.
"""


