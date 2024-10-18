
################# Advanced & special
# copy: update: 
#        
#        
################# (16-Oct-24 for 18-Oct-24)

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


# Boxplot
dta2 = [np.random.normal(0, std, 100) for std in range(1, 4)]
# rectangular box plot
plt.boxplot(dta2, vert=True, patch_artist=True); 

""" 
    numpy.random.normal(loc, scale, size):

        Distribution: Normal (Gaussian) distribution.
        Parameters:
            loc: Mean of the distribution (default is 0).
            scale: Standard deviation of the distribution (default is 1).
            size: Dimensions of the output array.

        Returns: Random numbers from a normal distribution with a specified mean (loc) and standard deviation (scale).

"""





# ----------------    Advanced plots and Refererance links    ----------------
# Essentially, we'll rely on Seaborn to manage most of the following staff
# Following are more advanced topics which we won't usually use as often
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# The data we want to plot:
# linearly spaced 11 points between (0, 5)
x = np.linspace(0, 5, 11)



# --------    AXIS modification    --------
# Set "Logarithmic scale" to axis (one or both axes)
# scales are set seperately using "set_xscale" and "set_yscale" using "log" as parameter

figAdv1, axsAdv1 = plt.subplots(1, 2, figsize=(8,4))
      
axsAdv1[0].plot(x, x**2, x, np.exp(x))
axsAdv1[0].set_title("Normal scale")

axsAdv1[1].plot(x, x**2, x, np.exp(x))
axsAdv1[1].set_yscale("log")
axsAdv1[1].set_title("Logarithmic scale (y)");

"""  
    Note:
        Notice the transformation of the lines after using "Logarithmic scale" : set_yscale("log")
        You can plot multiple lines on the same set of axes using a single plot() function in Matplotlib 
            by providing multiple sets of x and y data. 
            General form:
                            plt.plot(x1, y1, x2, y2, x3, y3, ...)
"""



# --------    Placement of ticks and custom tick labels    --------
# use "set_xticks" and "set_yticks"
    # both take a 'list of values' for where on the axis the ticks are to be placed. 
# custom tick labels
    # use "set_xticklabels" and "set_yticklabels" and provide a list of custom text labels for each tick location
# For  more deatil visit: https://matplotlib.org/stable/api/ticker_api.html

figAdv2, axsAdv2 = plt.subplots(figsize=(8, 4))
axsAdv2.plot(x, x**2, x, x**3, lw=2)

axsAdv2.set_xticks([1, 2, 3, 4, 5])
axsAdv2.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)

yticks = [0, 50, 100, 150]
axsAdv2.set_yticks(yticks)
axsAdv2.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18); # use LaTeX formatted labels


"""  
    $: The dollar signs are used to denote LaTeX math formatting in Matplotlib. 
        Anything between the dollar signs is interpreted as LaTeX code.
        Used for special symbols, Greek letters, superscripts, subscripts, and other mathematical notations

            r'$\alpha$' displays the Greek letter α

            "$%.1f$" % y formats numbers with one decimal place and then wraps them in LaTeX math-like format.

    r (raw string prefix): 
        The r before the string makes it a "raw string". 
        In raw strings, escape characters (like \) are treated as literal characters. 
        Used when writing LaTeX expressions that often include backslashes (\). For example:

            r'$\alpha$' means that \alpha is treated as part of the LaTeX code rather than an "escape sequence".
"""



# --------    Scientific notation    --------
# if we work with very large numbers like million or trillion, "Scientific notation" is best option
from matplotlib import ticker

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 

figAdv3, axAdv3 = plt.subplots(1, 1)
axAdv3.plot(x, x**2, x, np.exp(x))
axAdv3.set_title("scientific notation")
axAdv3.set_yticks([0, 50, 100, 150])
# set "Scientific notation" 
axAdv3.yaxis.set_major_formatter(formatter) 




# --------    Axis number and axis label spacing    --------
# "matplotlib.rcParams" is a dictionary for Matplotlib's default plot settings.
# By modifying rcParams, you can change how Matplotlib renders plots without having to specify options for each individual plot.
    # It controls properties like figure size, color, font size, and line width.
    # "rc" stands for run commands.
    # Customizes plot appearance globally in a Matplotlib session.

# View current default settings
print(plt.rcParams)

# Change the default figure size and font size
plt.rcParams['figure.figsize'] = (8, 6)  # Sets default figure size to 8x6 inches
plt.rcParams['font.size'] = 14           # Sets default font size to 14

# DISTANCE between x and y axis and the numbers on the axes
# Folowing refers to the configuration setting that controls the padding (i.e., the space) between the 
    # major x-axis, y-axis  ticks and the labels in a plot. 
    # The "value" set for this parameter adjusts the distance 
    # between the tick marks and their corresponding "labels" on the axis.

plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5

figAdv4, axAdv4 = plt.subplots(1, 1)
axAdv4.plot(x, x**2, x, np.exp(x))
axAdv4.set_yticks([0, 50, 100, 150])
axAdv4.set_title("label and axis spacing")

# padding between "axis label" and "axis values"
axAdv4.xaxis.labelpad = 5
axAdv4.yaxis.labelpad = 5

axAdv4.set_xlabel("x")
axAdv4.set_ylabel("y");

# restore DEFAULTS
plt.rcParams['xtick.major.pad'] = 3
plt.rcParams['ytick.major.pad'] = 3



# --------    Axis position adjustments    --------
""" 
    Sometimes figure may be cropped.
        subplots_adjust() can adjust the spacing between subplots within a figure. 
        allowing control the padding between subplots, including margins, spacing between rows and columns, 
        and the position of the subplots in relation to the figure edges.  
"""

# You can adjust parameters like left, right, top, bottom, wspace (width space), and hspace (height space)
# left cannot be >= right and bottom cannot be >= top

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.3, hspace=0.5)

figAdv5, axAdv5 = plt.subplots(1, 1)
      
axAdv5.plot(x, x**2, x, np.exp(x))
axAdv5.set_yticks([0, 50, 100, 150])

axAdv5.set_title("title")
axAdv5.set_xlabel("x")
axAdv5.set_ylabel("y")

figAdv5.subplots_adjust(left=0.15, right=.9, bottom=0.1, top=0.9);

# ----  Another example  ----
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

# Plot data on each subplot
axes[0, 0].plot(x, y1)
axes[0, 0].set_title('Sine Wave')

axes[0, 1].plot(x, y2)
axes[0, 1].set_title('Cosine Wave')

axes[1, 0].plot(x, y1 + y2)
axes[1, 0].set_title('Sine + Cosine')

axes[1, 1].plot(x, y1 - y2)
axes[1, 1].set_title('Sine - Cosine')

# Adjust the space between plots
# Note: left cannot be >= right and bottom cannot be >= top
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.5)
# now use following changed positions
# plt.subplots_adjust(left=0.4, right=0.5, top=0.5, bottom=0.4, wspace=0.8, hspace=0.9)


# Show the plot
plt.show()




# --------    Axis position adjustments    --------
# use 'grid' to turn on and off grid lines. 
# customize the grid lines using similar kwargs as 'plot' function:
figAdv6, axAdv6 = plt.subplots(1, 2, figsize=(10,3))

# default grid
axAdv6[0].plot(x, x**2, x, x**3, lw=2)
axAdv6[0].grid(True)

# custom grid
axAdv6[1].plot(x, x**2, x, x**3, lw=2)
axAdv6[1].grid(color='b', alpha=0.3, linestyle='dashed', linewidth=0.75)



# --------    Axis spines (i.e. X, Y axis lines)    --------
figAdv7, axAdv7 = plt.subplots(figsize=(6,2))

# color
axAdv7.spines['bottom'].set_color('blue')
axAdv7.spines['top'].set_color('red')

axAdv7.spines['left'].set_color('green')
axAdv7.spines['left'].set_linewidth(2)

# turn off axis spine to the right
axAdv7.spines['right'].set_color("none")
axAdv7.yaxis.tick_left() # only ticks on the left side



# --------    Twin axes    --------
# Dual x or y axes are useful when plotting curves with different units together.
# twinx() for a second y-axis
# twiny() for a second x-axis

figAdv8, axAdv8 = plt.subplots()

axAdv8.plot(x, x**2, lw=2, color="blue")
axAdv8.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
for label in axAdv8.get_yticklabels():
    label.set_color("blue")
    
ax2 = axAdv8.twinx()
ax2.plot(x, x**3, lw=2, color="red")
ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")



# --------    axes with origin point    --------
figAdv9, axAdv9 = plt.subplots()

axAdv9.spines['right'].set_color('none')
axAdv9.spines['top'].set_color('none')

axAdv9.xaxis.set_ticks_position('bottom')   # tick position
axAdv9.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0

axAdv9.yaxis.set_ticks_position('left')     # tick position
axAdv9.spines['left'].set_position(('data',0))   # set position of y spine to y=0

cu_be = np.linspace(-0.75, 1., 100)
axAdv9.plot(cu_be, cu_be**3);



# --------    Other 2D plot styles    --------
# instead of plot() there are other methods that can generate different kinds of plots
# for more: https://matplotlib.org/2.0.2/gallery.html
# Some of the more useful ones are: scatter(), step(), bar(), fill_between()

n = np.array([0,1,2,3,4,5])

figAdv10, axAdv10 = plt.subplots(1, 4, figsize=(12,3))

axAdv10[0].scatter(xx, xx + 0.25*np.random.randn(len(xx)))
axAdv10[0].set_title("scatter")

axAdv10[1].step(n, n**2, lw=2)
axAdv10[1].set_title("step")

axAdv10[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axAdv10[2].set_title("bar")

axAdv10[3].fill_between(x, x**2, x**3, color="green", alpha=0.5);
axAdv10[3].set_title("fill_between");



# --------    Text annotation    --------
figAdv11, axAdv11 = plt.subplots()

axAdv11.plot(cu_be, cu_be**2, cu_be, cu_be**3)

axAdv11.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
axAdv11.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green");




# ----  rev[16-Oct-2024]  ----

# --------    multiple subplots and insets    --------
# You can manually add axes to a figure using fig.add_axes, or 
    # use "Layout Managers" like subplots, subplot2grid, or gridspec

# ----  subplots  ----
# we've discussed it earlier
figAdv12, axAdv12 = plt.subplots(2, 3)
axAdv12.tight_layout()



# ----  subplot2grid  ----
# subplot2grid is a Matplotlib function for creating "subplots in a grid"
    # It offers flexibility in setting the size and position of each subplot.
# Unlike subplots, which creates "evenly spaced plots", 
    # subplot2grid allows subplots to "span multiple rows and columns"

figAdv13 = plt.figure()
axAdv13_ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
axAdv13_ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
axAdv13_ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
axAdv13_ax4 = plt.subplot2grid((3,3), (2,0))
axAdv13_ax5 = plt.subplot2grid((3,3), (2,1))
fig.tight_layout()



#### gridspec

import matplotlib.gridspec as gridspec

fig = plt.figure()

gs = gridspec.GridSpec(2, 3, height_ratios=[2,1], width_ratios=[1,2,1])
for g in gs:
    ax = fig.add_subplot(g)
    
fig.tight_layout()



#### add_axes

Manually adding axes with `add_axes` is useful for adding insets to figures:

fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)
fig.tight_layout()

# inset
inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35]) # X, Y, width, height

inset_ax.plot(xx, xx**2, xx, xx**3)
inset_ax.set_title('zoom near origin')

# set axis range
inset_ax.set_xlim(-.2, .2)
inset_ax.set_ylim(-.005, .01)

# set axis tick locations
inset_ax.set_yticks([0, 0.005, 0.01])
inset_ax.set_xticks([-0.1,0,.1]);






# --------    Colormap and CONTOUR    --------

Colormaps and contour figures are useful for plotting functions of two variables. In most of these functions we will use a colormap to encode one dimension of the data. There are a number of predefined colormaps. It is relatively straightforward to define custom colormaps. For a list of pre-defined colormaps, see: http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps

alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T


#### pcolor

fig, ax = plt.subplots()

p = ax.pcolor(X/(2*np.pi), Y/(2*np.pi), Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)



#### imshow

fig, ax = plt.subplots()

im = ax.imshow(Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
im.set_interpolation('bilinear')

cb = fig.colorbar(im, ax=ax)



#### contour

fig, ax = plt.subplots()

cnt = ax.contour(Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])









# --------    3D figures    --------

To use 3D graphics in matplotlib, we first need to create an instance of the `Axes3D` class. 3D axes can be added to a matplotlib figure canvas in exactly the same way as 2D axes; or, more conveniently, by passing a `projection='3d'` keyword argument to the `add_axes` or `add_subplot` methods.

from mpl_toolkits.mplot3d.axes3d import Axes3D


#### Surface plots

fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)



#### Wire-frame plot

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1, 1, 1, projection='3d')

p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)



#### Coutour plots with projections

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*np.pi, cmap=matplotlib.cm.coolwarm)

ax.set_xlim3d(-np.pi, 2*np.pi);
ax.set_ylim3d(0, 3*np.pi);
ax.set_zlim3d(-np.pi, 2*np.pi);






""" 
    --------    Further reading    --------
    http://www.matplotlib.org -     The project web page for matplotlib.
    https://github.com/matplotlib/matplotlib -  The source code for matplotlib.
    https://matplotlib.org/2.0.2/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended! 
    
    Nicolas P. Rougier (https://github.com/rougier):
        https://github.com/rougier/matplotlib-tutorial -  A good matplotlib tutorial.
        https://www.labri.fr/perso/nrougier/

    https://lectures.scientific-python.org/
        https://lectures.scientific-python.org/intro/matplotlib/index.html -    Another good matplotlib reference.

 """


* http://www.matplotlib.org - The project web page for matplotlib.
* https://github.com/matplotlib/matplotlib - The source code for matplotlib.
* http://matplotlib.org/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended! 
* http://www.loria.fr/~rougier/teaching/matplotlib - A good matplotlib tutorial.
* http://scipy-lectures.github.io/matplotlib/matplotlib.html - Another good matplotlib reference.
