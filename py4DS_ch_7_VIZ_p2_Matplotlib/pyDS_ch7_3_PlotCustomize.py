
################# Advanced & special
# copy:
#        
#        
################# (02-Oct-24 for 04-Oct-24)

# Courses: PrTla PY for DS & ML >   8.4 (6.22+), 8.5


# --------    Figure size, aspect ratio and DPI    --------
# By calling the 'fig' object we can customize the figure

from turtle import color
import numpy as np
import matplotlib.pyplot as plt

# customize a single "figure"
# "dpi" is the dots-per-inch (pixel per inch)
#      'dpi' for resolution. more dpi is more crisp image
#       most of the time default dpi is used
# "figsize" is a tuple of (width, height) in inches
#       figsize=(3, 2) means 3 inches by 2 inches
fig1 = plt.figure(figsize=(3, 2), dpi=100)
# add the axis
ax = fig1.add_axes([0, 0, 1, 1])

# The data we want to plot:
# linearly spaced 11 points between (0, 5)
x = np.linspace(0, 5, 11)
y = x**2    # output, function of x

ax.plot(x, y)

ax.set_title('Title')
ax.set_ylabel('Y')
ax.set_xlabel('X')



# customizing subplots
# 'figsize' and 'dpi' can also be passed to layout managers, such as the 'subplots'
fig2, axes2 = plt.subplots(nrows=2, ncols=1, figsize=(3,5))

axes2[0].plot(x, y)
axes2[1].plot(y, x)



# --------    saving a figure    --------
# matplotlib can save a figure in HD formats like: JPG, PNG, EPS, SVG, PGF and PDF
# To save a figure to a file we can use "savefig" method from "Figure" class
# we can specify the DPI and choose between different output formats
fig1.savefig("fig1.png")
fig2.savefig("fig2_subplot.jpg", dpi=200)



# --------    Legends, labels and titles    --------
# 'set_title' sets the TITLE of the axes instance
# 'set_xlabel' and 'set_ylabel' sets the labels of the X and Y axes:

# LEGEND: with legend we can have labled text for more info about a plot
#   used to specify multiple lines in one plot
import numpy as np
import matplotlib.pyplot as plt

fig3 = plt.figure(figsize=(3, 2))
ax3 = fig3.add_axes([0, 0, 1, 1])

# The data we want to plot:
x = np.linspace(0, 5, 11)
y = x**2 

# adding a legend is 2 step process
# 1.    label the objects in ax.plot(): label="label text"
# 2.    call legend() at the end

# multiple lines in one plot
ax3.plot(x, y, label='X vs Y')
ax3.plot(y, x, label='Y vs X')
ax3.plot(x, x**2, label='X Squared')
ax3.plot(x, x**3, label='X Cubed')

ax3.set_title('Title')
ax3.set_ylabel('Y')
ax3.set_xlabel('X')

ax3.legend(loc=0)    # check each of the plot and looks for a label
# to avoid the overlapping we can use 'loc', there is location codes and location strings
(location_strings, location_codes) = {
    ('best', 0),
    ('upper right', 1),
    ('upper left', 2),
    ('lower left', 3),
    ('lower right', 4),
    ('right', 5),
    ('center left', 6),
    ('center right', 7),
    ('lower center', 8),
    ('upper center', 9),
    ('center', 10)
}
# 'best' is recomended, i.e. loc=0

# alternative 2 tuple position: set the position of (x, y) of the "lower-left corner" of the legend
ax3.legend(loc=(0.1, 0.1))



# ------------    Setting colors, linewidths, linetypes    ------------
# MATLAB like sntax can be used (but avoid these for more clarity)

import numpy as np
import matplotlib.pyplot as plt

fig4 = plt.figure()
ax4 = fig4.add_axes([0, 0, 1, 1])

# The data we want to plot:
x = np.linspace(0, 5, 11)
y = x**2 


# ----  setting colors  ----
# colorcan take strings ('red', 'blue', 'orange') or RGB-HEX-color like "#FF9C00"
ax4.plot(x, y, color='#FF9C00')


# ----  linewidth  ----
# can also use shorthand: linewidth 'lw'
ax4.plot(x, y, linewidth=3)
# use "alpha-style" for tranparency
ax4.plot(x, y, linewidth=3, alpha=0.5)


# ----  using MATLAB-like syntax  ----
# we can define the colors of lines and other graphical elements 
    # color: 'b' means blue, 'g' means green, etc. 
    # line styles: 'b.-' means a blue line with dots
fig5, ax5 = plt.subplots()
ax.plot(x, x+1, color="blue", alpha=0.5) # half-transparant
ax.plot(x, x+2, 'g--')         # MATLAB-like syntax
ax.plot(x, x+3, color="#FF8C00")         # RGB hex code 



# ----  linestyle and marker styles  ----
# linestyle 
    # we can use different styles. Use 'linestyle' or 'ls' attribute
    # '-' solid line (default)
    # '--' dashed line
    # '-.' dot-dashed line
    # ':' smaller dashes
    # 'steps' stair-case like for 'fixes-increment of x axis'

# markers
# markers can be used if we have discrete "fiewer data-points"
# for example x is a set of 11 data points
# we want to mark those 11 points on the plot

# we'll use "marker" and "markersize" attribute
# styles: 
    # 'o' dots, '*' asteric, '1' star, '2' star, '+' points
    # 'markeredgewidth', 'markeredgcolor' and 'markerfacecolor' for more styling

import numpy as np
import matplotlib.pyplot as plt

fig6 = plt.figure(figsize=(12,6))
ax6 = fig6.add_axes([0, 0, 1, 1])

x = np.linspace(0, 5, 11)
print(x)

# ax6.plot(x, (1*x)+1, color="red", linewidth=0.25, linestyle='steps')
# ls ='steps' doesn't work anymore, use 'drawstyle' or 'ds': drawstyle='steps-pre'
ax6.plot(x, (1*x)+1, color="red", linewidth=0.25, linestyle='-', drawstyle='steps-pre')
ax6.plot(x, (2*x)+2, color="green", linewidth=0.50, linestyle='-')
ax6.plot(x, (3*x)+3, color="blue", linewidth=1.00, ls='-.')
ax6.plot(x, (4*x)+4, color="purple", linewidth=2.00, ls=':')

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax6.plot(x, (x**1), color="#FF9C00", lw=2, ls='-', marker='+', markersize=2)
ax6.plot(x, (x**2), color="#FF9C00", lw=2, ls='--', marker='o', markersize=2)
# marker with more styles
ax6.plot(x, (x**0.5), color="#FF9C00", lw=2, ls='-', marker='s', markersize=8, markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="#008811")
ax6.plot(x, (x**-2), color="#FF9C00", lw=2, ls='--', marker='1', markersize=8, markerfacecolor="#008811", markeredgewidth=3, markeredgecolor="red")


# ----  custom dash  ----
# format: line length, space length, ...
fig7, ax7 = plt.subplots(figsize=(12,6))

line, = ax7.plot(x, -x, color="black", lw=1.50)     # notice "tuple unpacking"
line.set_dashes([5, 10, 15, 10])  # format: line length, space length, ...


fig8 = plt.figure(figsize=(6,6))
ax8 = fig8.add_axes([0, 0, 1, 1])
line2, = ax8.plot(x, -x, color="black", lw=1.50)     # no tuple sepearion needed for single object
line2.set_dashes([5, 10, 15, 10])  # format: line length, space length, ...

""" 
    ----  why "tuple unpacking"  ----
    line, = ax7.plot(x, -x, ...) 
    assigns the "Line2D object" created by the plot() function to the variable 'line'

    The tuple unpacking (line, =) is necessary because ax7.plot() returns a "list of line objects", even if only one line is plotted. 
    The trailing comma ensures that 'line' is assigned the "single Line2D object", rather than a list containing it.

    If you don't use tuple unpacking (i.e., if you just do line = ax7.plot(...)), 
        then line becomes a 'list', and lists don't have a "set_dashes()" method. 
    That's why you would get the error: 'list' object has no attribute 'set_dashes'.

    So, to avoid this error, the "line, =" syntax ensures that you are dealing with the actual Line2D object, which has the set_dashes method.
"""


# ------------    axis appearance control    ------------
import numpy as np
import matplotlib.pyplot as plt

fig9 = plt.figure(figsize=(12,6))
ax9 = fig9.add_axes([0, 0, 1, 1])

x = np.linspace(0, 5, 11)
print(x)

ax9.plot(x, x*x, color='red', lw=2, ls='--')

# plot range
# y-limit and x-limit: for eaxample we want to set x= [0, 1]
ax9.set_xlim([0, 1])
ax9.set_ylim([0, 2])



# ------------    special plot  types    ------------
# Most of these special methods we'll use in the "seaborn" library, but they primarily originate from Matplotlib.
    # barplot
    # histogram
    # scatterplot
    # boxplot

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 16)    # 0 to 15, 16 points

# scatter plot
plt.scatter(x, (x**2)*(-1)**2)


# Histogram
from random import sample
dta = sample(range(1, 1000), 100)
print(dta)
plt.hist(dta) # plots how many data points falls in (0, 100), (101, 200), ..., (901, 1000)

"""  
    sample() is an built-in function of "random" module in Python that returns a particular length "list of items" chosen from the sequence 
    The "sequence" can be a list, tuple, string, or set, and the sampling is done without replacement.

            Syntax : 
                        random.sample(sequence, k)  
            Parameters:
                        sequence: Can be a list, tuple, string, or set. 
                        k: An Integer value, it specify the length of a sample

            Returns: k length new list of elements chosen from the sequence.
"""
# demo of random.sample()
from random import sample

# Prints list of random items of given length
list1 = [1, 2, 3, 4, 5] 

print(sample(list1,3))



# ------------    Advanced plots and Refererance links    ------------
# Essentially, we'll rely on Seaborn to manage most of the following staff



