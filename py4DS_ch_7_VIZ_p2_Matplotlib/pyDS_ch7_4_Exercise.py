
################# 8.6: Full
# copy:  
#        
#        
################# (29-oct-24 for 30-oct-24)

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

# plot (x,y) on both axes. And call your figure object to show it
ax1.plot(x, y)
ax2.plot(x, -x)

ax1.set_xlabel('X')
ax1.set_ylabel('y')
ax2.set_xlabel('X')
ax2.set_ylabel('y')

fig1    # Show figure object




# Problem 3
    # Create a plot by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
fig2 = plt.figure()
ax_a1 = fig2.add_axes([0, 0, 1, 1])
ax_a2 = fig2.add_axes([0.2, 0.5, .4, .4])

# use x,y, and z arrays to plot. 
# modify the xlimits and ylimits on the inserted plot: y : (30, 50), x: (20, 22)
ax_a1.plot(x, z)
ax_a2.plot(x, y)

ax_a1.set_xlabel('X')
ax_a1.set_ylabel('z')
ax_a2.set_xlabel('X')
ax_a2.set_ylabel('y')

ax_a2.set_title("X vs Y")
ax_a2.set_xlim(20, 22)
ax_a2.set_ylim(30, 50)

fig2    # Show figure object



# Problem 4
    # Use plt.subplots(nrows=1, ncols=2) to create a subplot
    # plot (x,y) and (x,z) on the axes
    # change linewidth and style

fig_p4, ax_p4 = plt.subplots(nrows=1, ncols=2)

# use x,y, and z arrays to plot
ax_p4[0].plot(x, y, linewidth=3, linestyle='--', color='blue')
ax_p4[1].plot(x, z, linewidth=3, color='red')

# or
# axes[0].plot(x,y, color="blue", lw=3, ls='--')
# axes[1].plot(x,z, color="red", lw=3, ls='-')


