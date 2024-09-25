
################# 8.4: 11.34
# copy:  2 figs
#        
#        
################# (10-Sep-24 for 11-sep-24)

# Courses: PrTla PY for DS & ML >   8.4 (6.22+), 8.5


# --------    Figure size, aspect ratio and DPI    --------
# By calling the 'fig' object we can customize the figure

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


