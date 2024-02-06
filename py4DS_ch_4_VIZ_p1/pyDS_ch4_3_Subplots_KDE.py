
# Courses: A-Z PY for Data-Science    6.5, 6.6


# ------------    Load Dataset & Libraries    ------------
# Import the following packages needed to perform the analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# plot shown in Jupyter Notebook
%matplotlib inline  
# expand the figure-width
plt.rcParams['figure.figsize'] = 8, 4


# Loading Dataset
# Import the csv dataset
movies = pd.read_csv("./MovieRatings.csv")     # load datset

# -=-=-  Explore the data  -=-=-
# Visualize the dataframe
movies

# rename the column names to single-string names
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.head()    # view dataset


# ----   convert 'numerical-type',' object-type' to "categorical-type"   ----
movies.Film = movies.Film.astype("category") # use assignment '=' to update the dataset
movies.Genre = movies.Genre.astype("category")   
movies.Year = movies.Year.astype("category")   
movies.info()   # check the data-type changes



# ------------    KDE PLOT: Kernel Density Estimate plot    ------------

# How can we visualize 'audiance rating' vs 'critic rating'?
    # We can use 'scatter-plot'
    # We also can use 'lmplot'
vis1_sctr = sns.scatterplot(data=movies, x='CriticRating', y='AudienceRating')    

# lmplot: recall 'pyDS_ch2_8_HW_wrldTrnd.py'
plt.style.use("seaborn")    # background color
vis2_lm = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating', fit_reg=False, hue='Genre', height=6, aspect=1, scatter_kws={'s': 10})
# setting x,y axis range
# vis2_lm.set(xlim=(-20, None))
vis2_lm.set(xlim=(-20, 120), ylim=(-10, 110))


# What are other way to visualize, other than 'scatter-plot' or 'lmplot'
    # To get more plot: Seaborn Gallery

# KDE: Kernel Density Estimate
kDe1 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating)  # this will get us a KDE-plot
# it's pretty much the same as 'scatter-plot' or 'lmplot' but instead of dots we get the 'kernel-density-estimate'
    # 'kernel-density-estimate' shows us most 'density of the data'
    # how the density is distributed across the chart for 'Bi-variate distribution'
    # further away the 'kernel' the density gets lower (fading away)

# why KDE used:
    # to get the idea 'where two data are mostly correlated'
    # how data is distributed accross the two-variables for a 'Bi-variate distribution'

# More Adjustments for the KDE-plot
    # It's more liak a 'Heat-map' or 'Heat-digram'
    # shade=True  we simply add a color
    # shade_lowest=False  it removes the color/shade of the last layer so that we can see the grids
    # We'll learn more styling, at the end of the section
kDe2 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False)

# cmap='Reds'  adds differnt color to our KDE-plot
kDe3 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds')

# without any shades/color, just the outlines
kDe4 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds')

# combine with border
    # in 'kDe3' it was slightly rough on the edges, 
    # so we combine 'shades' & 'border' like below, it'll give us overlaied plot
    # edge will look like more contured
kDe5 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds')
kDe6 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds') # ads border on top of 'kDe5'

# Below we try to create KDE-plot for other numeric variables




# ------------    Subplots()    ------------
# allows us to create some sophisticated visualizations
    # it COMBINES different visualizations togather

# Create new Kernel Density Estimate (KDE): BudgetMillions vs AudienceRating
# sns.set_style("dark")   # change seaborn-style, no-grid
k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating')
k_BA.set(xlim=(-40, 250), ylim=(-20, 120))  # we set the range to compare the plots

# Observations: It shows us wheather the budget of the movies affect the 'AudienceRating'
    # is there any 'skew' of the visualization to the Right/Left or UP/Down
    # slice the plot at AudienceRating = 40, notice the Budget is lie between (30, 45)
    # If we slice the plot at AudienceRating = 60, notice now the Budget is spread-out
    # if we slice it vertically BudgetMillions = 20, the Rating is streached around (20, 90)
    # But slicing vertically at BudgetMillions = 90, the Rating shrinks around (40, 70)
        #i.e. 'lower density' gets bit higher and the 'higher-density' gets low
    

# (KDE): BudgetMillions vs AudienceRating
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating')
k_BC.set(xlim=(-40, 250), ylim=(-20, 120))  # we set the range to compare the plots

# Observations: Similar to above plot
    # notice the CriticRating & BudgetMillions values go under 0.
    # its not in reality, actually its the 'way the KDE is constructed'
    # Actually the CriticRating is constructed at the KERNEL, between (20, 40)
        # and then its streached out
    # as we go above BudgetMillions = 50, the CriticRating start to shrink
        # max-CriticRating drops and min-CriticRating increase

# Notice from both plot/chart
    # the AudienceRating make the plot bit-tighter
    # the CriticRating make the plot bit-spread-out
    # the reason is:
        # AudienceRating is closer to 'Normal-distribution'
        # CriticRating is closer to 'Uniform-distribution'
    

# ----  subplots:  ----
    # Notice we have to set 'xlim' & 'ylim' same in the both plots 'k_BA' and 'k_BC' for camparison
    # subplot is a tool used to do that kind of comparison
    # subplot comes from 'pyplot'
    # in subplot we can show multiple plots at the same-time
    # a subplot can be a 1D or 2D array of plots
    # we can put the different plots in 'different locations' using coordinates (array-index)
    
    # Dashboard creation:
        # COMBINE any kind of plots: not only 'KDE' but we can also plot 'KDE', 'scatterplot' togater
        # subplot is commonly used to create DASHBOARDs


# Following is a coding convention- f:figure, ax:axes
f, axes = plt.subplots(1, 2)
# above creates an 1D array of 2-plots
    # (1, 2) means one-row, two columns
f, axes = plt.subplots(1, 2) # 1 row of 3-plots
f, axes = plt.subplots(3, 3) # 3 rows of 3-plots = 9 plots

# attributes
# figsize = Size of the "whole subplot figure", input is a tuple
    # figsize = (length, height) = (12, 6)


# we'll place 'k_BA' and 'k_BC' in the following subplot
f, axes = plt.subplots(1, 2, figsize = (12, 6))

# We have to specify the place of each plot, notice the arrgumnet ax=axes[0], ax=axes[1]
    # index is used: axes[0] is the first plot, axes[1] is the second plot
f, axes = plt.subplots(1, 2, figsize = (12, 6))
k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes[0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes[1])

# 'f, axes' is actually "fig, ax", its a tuple of two objects. 
    # 'f' is the figure, 
    # 'axes' is the array for acessing each of the plot
""" 
    *fig* is the :class:'matplotlib.figure.Figure' object

    *ax* can be either a 
        'single axis object' or 
        'an array of axis objects' if more than one subplot was created. 

    The dimensions of the resulting array can be controlled with the 'squeeze' keyword. 
"""

axes
# array([<AxesSubplot:xlabel='BudgetMillions', ylabel='AudienceRating'>,
#        <AxesSubplot:xlabel='BudgetMillions', ylabel='CriticRating'>],
#       dtype=object)


# ----  2D array of plots (array of axis objects)  ----
f, axes = plt.subplots(2, 2, figsize = (12, 6))
# k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes[0])   # ERROR
# k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes[1])     # ERROR

# Dimension: notice we have to specify 2-indexes for each plot,, otherwise we'll get an error
    # 2D set of subplots vs 1D set of subplots
        # for 1D array objects we use 1-index
        # in 2D array objects we use 2-indexes
k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes[0, 0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes[0,1])
k_AC = sns.kdeplot(data=movies, x='AudienceRating', y='CriticRating', ax=axes[1,1])


# setting the RANGE of x, y:
    # as before we use 'xlim' and 'ylim'
    # however, we can use 'sharex', 'sharey' attributes to set all same 'xlim & ylim'
f2, axes2 = plt.subplots(1, 2, figsize = (12, 6), sharex=True, sharey=True)
k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes2[0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes2[1])
k_BA.set(xlim=(-20, 160))
# We can use same for k_BC
    # k_BC.set(xlim=(-20, 160))
    # but it can be done with 'subplots' attribute "sharex"
    # 'sharex=True' set the same xlim for all plots
    # 'sharey' does the same thing for y-axis

# issue 1, label: sharex, sharey hides 'label'
    # the label exists, but it is not visible.
    # Add this line to get the label to be visible.
axes[1].yaxis.get_label().set_visible(True)
# now both charts are visually comparable

# issue 2, ticks: also you can use following workaround to show ticks (numbers)
fig, (ax,ax2) = plt.subplots(2, sharex=True)
ax.xaxis.set_tick_params(which='both', labelbottom=True)

# issue fixed: 
""" 
    matplotlib.axes.Axes.tick_params
    Axes.tick_params(axis='both', **kwargs)[source]
    Change the appearance of ticks, tick labels, and gridlines.

    Tick properties that are not explicitly set using the keyword arguments remain unchanged unless reset is True. For the current style settings, see Axis.get_tick_params.

Parameters:
    axis
    {'x', 'y', 'both'}, default: 'both'
    The axis to which the parameters are applied.

    which
    {'major', 'minor', 'both'}, default: 'major'
    The group of ticks to which the parameters are applied.

    reset
    bool, default: False
    Whether to reset the ticks to defaults before updating them. 
"""

f, axes = plt.subplots(2, 2, figsize = (12, 6), sharex=True, sharey=True)
k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes[0, 0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes[0,1])
k_AC = sns.kdeplot(data=movies, x='AudienceRating', y='CriticRating', ax=axes[1,1])
for i in range(0,2):
    for j in range(0,2):
        # show labels
        axes[i,j].yaxis.get_label().set_visible(True)
        axes[i,j].xaxis.get_label().set_visible(True)
        # show ticks
        axes[i,j].xaxis.set_tick_params(which='both', labelbottom=True)
        axes[i,j].yaxis.set_tick_params(which='both', labelleft=True)

