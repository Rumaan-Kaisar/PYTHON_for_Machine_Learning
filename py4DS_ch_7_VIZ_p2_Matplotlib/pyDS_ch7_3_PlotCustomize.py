
################# 8.4: full, 8.5:3.50
# copy:
#        
#        
################# (27-Sep-24 for 28-sep-24)

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


# ----  linestyle  ----
# Line and marker styles



