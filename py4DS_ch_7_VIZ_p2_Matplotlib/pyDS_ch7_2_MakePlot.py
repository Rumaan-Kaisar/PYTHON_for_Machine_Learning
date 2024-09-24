
# Courses: PrTla PY for DS & ML >   8.3, 8.4 (6.22)

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

import numpy as np
import matplotlib.pyplot as plt
# shows plots directly in Jupyter notebooks.
%matplotlib inline

# First, create a figure instance
fig = plt.figure()
# notice matplotlib.figure object is created
# consider it as a blank canvas


# Add set of axes to figure, add_axes() takes an list argument with four element
#   left, bottom, width, height (range 0 to 1, as percentage)
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 

# The data we want to plot:
# linearly spaced 11 points between (0, 5)
x = np.linspace(0, 5, 11)
y = x**2    # output, function of x

# Plot on that set of axes
axes.plot(x, y, 'r')

# X,Y labels and title, notice the use of set_ to begin methods
axes.set_xlabel('X Label')
axes.set_ylabel('y Label')
axes.set_title('Title')


# Let's try multiple plot in one canvas. 
#   It'll clear the purpose of using the list [0.1, 0.1, 0.8, 0.8], to what it referances
#       basically first two are the coordinate of origin
#       last tw are define the size of the plot
#       all 4 numbers ranges between (0, 1) as relative-percetage

fig2 = plt.figure()

ax1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])   # origin at (0.1, 0.1), size of (0.8, 0.8)
ax2 = fig2.add_axes([0.2, 0.5, 0.4, 0.5])   # origin at (0.2, 0.5), size of (0.4, 0.5), smaller moved upper-left
# Note: each ax1, ax2 is an 'matplotlib.axes' object
#       we've manually created it, in subplot() we'll work with array of 'matplotlib.axes'

# Plot on ax1
ax1.plot(x, y, 'r')
ax1.set_title('Big plot')

# Plot on ax2
ax2.plot(y, x)
ax2.set_title('Small Plot')




# ------------    SUBPLOTs using OO    ------------
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots()

# as before we can use 'axes' to plot 
x = np.linspace(0, 5, 11)
y = x**2    # output, function of x

# Plot on that set of axes
axes.plot(x, y, 'r')
axes.set_xlabel('X Label')
axes.set_ylabel('y Label')
axes.set_title('Title')

# subplot allows number of rows and columns
#   it's actually an axes manager on top of plt.figure
fig_2, axes_2 = plt.subplots(nrows=1, ncols=2)
fig_3, axes_3 = plt.subplots(nrows=3, ncols=3)

# ----  issues of overlapping  ----
#   we'll deal with it later. But a quickfix is using: tight_layout()
#   fig.tight_layout() or plt.tight_layout() automatically adjusts the positions of the axes on the figure canvas
plt.tight_layout()


# Here 'axes' is an array of axes to plot on (i.e. an array of 'matplotlib.axes' objects).
#   that's the reason of this "tuple-unpacking":  "fig, axes"   
#   of  "fig, axes= plt.subplots()"
axes
axes_3

# we can manually access each 'axes' by indexing and plot
axes_3[1][1].plot(x, y)
axes_3[1][1].set_title('First Plot')
axes_3[2][0].plot(y, x)
axes_3[2][0].set_title('Second Plot')
fig_3

# we can LOOP through that "array of axes"
for currnt_ax in axes_2:
    currnt_ax.plot(x, y)
fig_2

# notice nested loop to access "array of axes"
for row in axes_3:
    for currnt_ax in row:
        currnt_ax.plot(x, y)
fig_3

# put "tight_layout" at the of the plot-statements
plt.tight_layout()


