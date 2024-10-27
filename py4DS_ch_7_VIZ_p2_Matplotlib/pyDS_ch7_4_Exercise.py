
################# 8.6: Full
# copy:  
#        
#        
################# (27-oct-24 for 29-oct-24)

# Courses: PrTla PY for DS & ML >   8.6, 8.7

# ------------    matplotlib exercise    ------------
# Following are reletively simple plots
# Don't focus too much on the Matplotlib syntax; we'll be using Seaborn in the next chapter.
# Since Seaborn is built on top of Matplotlib, it's important to understand Matplotlib first.

# note: all the commands for plotting a figure should all go in the same cell. separating them out into multiple cells may cause nothing to show up

# use following data
import numpy as np
x = np.arange(0, 100)   # array of [0, 1, ..., 99]
y = 2*x
z = x**2


# Import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt
# set %matplotlib inline if you are using the jupyter notebook. 
%matplotlib inline
# What command do you use if you aren't using the jupyter notebook?
# plt.show()




# Problem 1:
    # Create a figure object called fig using plt.figure() 
    # Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. 
    # Plot (x,y) on that axes and set the labels and titles to match the plot below:

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('title')




# Problem 2
    # Create a figure object and put two axes on it, ax1 and ax2. 
    # Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively
fig1 = plt.figure()
ax1 = fig1.add_axes([0, 0, 1, 1])
ax2 = fig1.add_axes([0.2, 0.5, .2, .2])


