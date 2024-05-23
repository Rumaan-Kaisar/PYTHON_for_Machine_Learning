
################# 5.6: 3.41
# copy:  
#        
#        
################# (22-May-24 for 24-May-24)

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

# ------    scaler operation    ------
# numpy basically broadcast the scaler to every element 
# the operation occured in also "element by element"

arr + 100
arr / 100
arr * 100


# --------    numpy warning    --------
# dividing elements by 0 cause ERROR in "python"
# but "numpy" gives a warning instead of ERROR
1/0     # gives ERROR in python: ZeroDivisionError

# numpy gives an "warning" but no ERROR
    # notice the first element of the "arr" is 0 and 
    # 0/0 will give a ERROR in python
    # but in "numpy" we'll get an warning instead
        # it will return "nan" for 0/0 in numpy

arr / arr       # Runtimewarning: invalid value encountered in true_divide

# following returns 'inf' (infinity) for the first element when performing '1/0'
1 / arr

