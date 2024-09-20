
################# 8.3: 8.58
# copy:
#        
#        
################# (15-Sep-24 for 17-sep-24)

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
    # OOP way - object oriented way


# --------    Functional way of plotting    --------
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

# MatLab-like syntax is also used, eg: to set color and line style 'r--'
plt.plot(x, y, 'r--')

# X,Y labels and title
plt.plot(x, y)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title("Title: simple plot")

# Note: later we'll learn to control dpi to get a finar font & plot
# we need to set the specific DPI before use plt.plot()
plt.figure(dpi=150)  # Higher DPI value results in a finer plot
plt.plot(x, y)



# ------------    multi-plot: subplot    ------------
# plt.subplot(row, col, ref_to_plot_num)
plt.subplot(1,2, 1)
plt.plot(x,y, 'r')

plt.subplot(1,2, 2)     # notice 3rd arg "ref_to_plot_num" set to 2 for 2nd plot
plt.plot(y,x, 'b--')




# --------    Object-Oriented way of plotting    --------
# Let's break down Matplotlib's Object-Oriented API:
#   This approach involves creating figure objects and then calling methods or attributes from them.
#   The key idea is to create figure objects and use their methods, especially when handling multiple plots on one canvas.

# First, create a figure instance
fig = plt.figure()
# notice matplotlib.figure object is created
# consider it as a blank canvas

# Add set of axes to figure, add_axes() takes an list argument with four element
#   left, bottom, width, height (range 0 to 1, as percentage)
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 

# Plot on that set of axes

