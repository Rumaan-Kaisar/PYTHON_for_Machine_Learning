
# Courses: PrTla PY for DS & ML >    9.6, 9.7


# ------------    Regression Plots    ------------
# Seaborn includes many tools for regression plots (Regression will be discussed later in the machine learning section)
# For now, we'll focus on the lmplot() function

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# lets load a builtin dataset of seaborns: 'tips'
tips = sns.load_dataset('tips')
tips.head()


# ----  lmplot  ----
# lmplot: Displays linear models and allows:
# Splitting plots by features.
# Coloring using the hue parameter (based off of features)

sns.lmplot(x='total_bill', y='tip', data=tips)
# we got a scatterplot with a linear fit

# use 'hue' for data seperation based on categorical feature
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette="rocket")
# notice 2 scatterplot with 2 linear fit for 'male' and 'feamle'
# so male and female has almost same linear fits for "total_bill vs tips"

# Markers:
# Style the markers using matplotlib "style" parameter (matplotlib marker symbols)
    # scatter_kws is used to pass "matplotlib parameters" directly as a dictionary
    # because sns running matplotlib under the hood. Eg. 's' for marker size
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], scatter_kws={'s':100}, palette="husl")


# more options: Working with Markers
# palette: hls, husl, Set2, Paired (paired colors)
""" 
    "lmplot" passes its keyword arguments to "regplot", a more general form of lmplot().
        "regplot" has a "scatter_kws" parameter, which is passed to "plt.scatter"
        To adjust marker size, set the 's' key in "scatter_kws"
        Note: s controls the squared marker size.
        Use a dictionary for Matplotlib arguments, like {'s': 50} for marker size
    
    In other words you end up passing a dictionary with the base matplotlib arguments, in this case, s for size of a scatter plot.
        You might not remember this detail, so check the documentation when needed. 
        http://matplotlib.org/api/markers_api.html
"""

# use "grid" (seperate plot) insted of seperating by "hue" (do by color)
sns.lmplot(x='total_bill', y='tip', data=tips, col="sex")   # plot for each sex
# Gives two separate column plots separated by the 'sex' category

# we can do this for rows as well
sns.lmplot(x='total_bill', y='tip', data=tips, col="sex", row='time')   # plot for each sex
# This is similar to the grid and FacetGrid call we've done earlier.
# Now it's automatic because we specify 'row' and 'col' by passing them to 'lmplot'

# combined 'hue' (as time) and 'grid' (as sex)
sns.lmplot(x='total_bill', y='tip', data=tips, col="sex", hue='time')
# another example: 'hue' (as sex) and 'grid' (as day)
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', palette='coolwarm')


# ----  adjusting aspect-size ratio (ratio between height and width)  ----
# using 'aspect' and 'size' parameters
# sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', palette='coolwarm', aspect=0.6, size=8)
# lmplot() got an unexpected keyword argument 'size'. use 'height' instead
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', palette='coolwarm', aspect=0.6, height=8)




# ------------    style    ------------
# changing fontsize, asthetics, colors 

# ----  Styles  ----
# We can set particular "Background Styles"
sns.countplot(data=tips, x='sex')
# notice the background of the plot

# by using "sns.set_style" we change the styles to: darkgrid, whitegrid, dark, white, ticks
sns.set_style('darkgrid')
sns.countplot(data=tips, x='sex')

# shows ticks and no background
sns.set_style('ticks')
sns.countplot(x='sex',data=tips,palette='deep')



# ----  spine removal  ----
sns.set_style('ticks')  
sns.countplot(x='sex',data=tips,palette='deep')
sns.despine()   # removes top and right spines

# to remove bottom and left spines use: top=True, right=True, left=False, bottom=False
sns.set_style('ticks')  
sns.countplot(x='sex',data=tips,palette='deep')
sns.despine(left=True, bottom=True)   # removes top, right, left and bottom spines

# only left spine
sns.countplot(x='sex',data=tips)
sns.despine(left=True)



# ----  size and aspect  ----
# We can combine Matplotlib and Seaborn.  
    # Using Matplotlib's "plt.figure(figsize=(width, height))", we can adjust most Seaborn plots.  
    # "Seaborn" essentially calls back to "Matplotlib" for these adjustments.
    # For Seaborn grid plots, we can also control the size and aspect ratio using the "height" and "aspect" parameters.

plt.figure(figsize=(12, 3))
sns.countplot(x='sex', data=tips)
# Note: When Seaborn calls Matplotlib, the size is overridden. 
    # Matplotlib now sets the figure size for the Seaborn plot.

# size and aspect of Grid Type Plot
sns.lmplot(x='total_bill',y='tip', height=2, aspect=4, data=tips)



# ----  Scale and context    ----
# set_context() override default parameters and change font scales.  
# For example, we can create a plot suitable for a poster.  
    # Context options include: paper, notebook, talk, and poster.  
    # By default, it is set to 'notebook'.  

sns.set_context('poster')  
# Notice the figures will be much larger with larger fonts, making them suitable for a poster.  

# Setting font scale to 2x larger than the default.  
sns.set_context('poster', font_scale=2)  
sns.countplot(x='sex', data=tips)



# --------    Palettes and colors    --------
# We've seen the 'hue' and 'palette' parameters.  
# Different palettes can be found in the "Matplotlib colormap" documentation.  
# Examples include: viridis, inferno, plasma, and magma.  
# There are also sequential colormaps available.  
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')


# --------    here are the fiew colormaps    --------
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    # Save colormap list for later.
    cmaps[category] = cmap_list



plot_color_gradients('Perceptually Uniform Sequential',
                     ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])


plot_color_gradients('Sequential',
                     ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])


plot_color_gradients('Sequential (2)',
                     ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
                      'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
                      'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'])


plot_color_gradients('Diverging', ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'])


plot_color_gradients('Cyclic', ['twilight', 'twilight_shifted', 'hsv'])


plot_color_gradients('Qualitative',
                     ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
                      'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
                      'tab20c'])


plot_color_gradients('Miscellaneous',
                     ['flag', 'prism', 'ocean', 'gist_earth', 'terrain',
                      'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
                      'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
                      'turbo', 'nipy_spectral', 'gist_ncar'])

plt.show()




# --------  single colors  --------
import math

import matplotlib.pyplot as plt

import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle


def plot_colortable(colors, *, ncols=4, sort_colors=True):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig


plot_colortable(mcolors.BASE_COLORS, ncols=3, sort_colors=False)

plot_colortable(mcolors.TABLEAU_COLORS, ncols=2, sort_colors=False)

# CSS colors
plot_colortable(mcolors.CSS4_COLORS)
plt.show()

