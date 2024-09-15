
################# 8.3: 3.56
# copy:
#        
#        
################# (14-Sep-24 for 15-sep-24)

# Courses: PrTla PY for DS & ML >   8.3, 8.4 (6.25)

# ------------    Matplotlib concepts    ------------

""" 

Matplotlib is the main Python library for data visualization, created by "John Hunter" 
    to replicate MatLab's plotting features in Python.

If you're familiar with MatLab, Matplotlib will feel natural.

It's a powerful 2D and 3D graphics library for scientific figures.


Pros of Matplotlib:
    - Easy to start with for simple plots
    - Supports custom labels and text
    - Full control over every element in a figure
    - High-quality output in many formats
    - Highly customizable

Matplotlib lets you create reproducible figures programmatically. 
You can explore more on the official Matplotlib website: http://matplotlib.org/.

"""

import matplotlib.pyplot as plt

# shows plots directly in Jupyter notebooks.
%matplotlib inline
# If you're using another editor, add plt.show() at the end of your plotting commands 
#   to display the figure in a separate window
#   plt.show()    # other than Jupyter NB
#   notice 'out' cell is gone when we use plt.show() in ipynb
#   its similar to typing 'string' vs print('string')
#       similarly plt.show() is printing the plot instead of showing the plot



# 2 way to plot in Matplotlib:
    # Functional way
    # OOP way


# --------    Functional way of plotting    --------
# MatLab syntax is also used, eg: to set color r
import numpy as np

# Let's define two numpy arrays. 
# You can plot with lists, but you'll usually use numpy arrays or pandas columns, which act like arrays.

# The data we want to plot:
# linearly spaced 11 points between (0, 5)
x = np.linspace(0, 5, 11)
y = x**2    # output, function of x
print(x)
print(y)
plt.plot(x, y)
# plt.show()    # other than Jupyter NB

