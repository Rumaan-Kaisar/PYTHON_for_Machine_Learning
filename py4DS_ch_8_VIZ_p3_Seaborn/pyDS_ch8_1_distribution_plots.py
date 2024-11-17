
# Courses: PrTla PY for DS & ML >    9.1, 9.2


# ------------    distribution plots    ------------

# Let's go over some plots that help visualize the distribution of a dataset
        #   distplot
        #   jointplot
        #   pairplot
        #   rugplot
        #   kdeplot

# what is seaborn:
    # Seaborn is a statistical plotting library based on Matplotlib
    # It has default styles that works with pandas DataFrame objects
    # It has a wide range of plot types for visualizing 
        # distributions, 
        # relationships, and 
        # categorical data.

# how to install:
    # conda install seaborn
    # or
    # pip install seaborn

# documentation:
    # GitHub: we can find it on GitHub since it's open-source:  https://github.com/mwaskom/seaborn
    # official: https://seaborn.pydata.org/
        # use "gallery" as reference, eg: heatmap, vilinplot, boxplot, joint plot
        # API: reference for various plot-types


# import libraries
import seaborn as sns
%matplotlib inline  # shows figures in ipynb

# lets load a builtin dataset of seaborn. tips: a dataset of restaurant patrons' tipping behavior
tips = sns.load_dataset('tips')
tips.head()

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')



# ------------    distplot    ------------
# it shows the distribution of uni-variate (one-variable) set of observations
# use a single column of your datsset
sns.distplot(tips['total_bill'])

# Notice we have a "kde (kernel density estimation) layer" (the blue line)
# to remove it, we just use "kde=False"
sns.distplot(tips['tip'], kde=False)
# now we just have a "histogram" is just a distribution of the data-points
# Y-axis is the "counts" and X-axis is the "data"
# so $2 nad $3 are most given tips

# change noumber of bins (depends on dataset)
# bins too high plots every single instance, make your plot wierd
sns.distplot(tips['total_bill'], kde=False, bins=40)
# most of the bills happens in between 10 and 20 dollers



# ------------    jointplot    ------------
    # jointplot() creates a combined view of two distributions for bivariate (2-variable) data, 
    # allowing you to select a comparison type with the kind parameter:
    #   "scatter" -  scatter plot
    #   "reg"     -  regression plot
    #   "resid"   -  residuals plot
    #   "kde"     -  kernel density plot
    #   "hex"     -  hexbin plot

# For example we can combine 2 dstribution plots of both (columns of or dataset) "total_bill" and "tip" 
#   also we can plot their relation on a scatterplot (to compare those 2 distributions)
sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
# notice, higher the total_bill has higher tips
# most of the tips lie between (1, 5) for total_bill (5, 35)

# ----  hexbin plot  ----
# hexagon distribution representation
sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex')
# hexagon gets darker if it has certain number of points in it 

# ----  regression plot  ----
# plots an additional "regression line" (we'll discuss more in Machine Learning)
# notice the linear fitting using p-value (and pearsonr coefficient)
sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')
# by default "kind" is "scatter", now we've set it to 'hex' and 'reg'

# ----  2D kde  ----
# density of the points. Use 'shade' or 'fill' for coloring
sns.jointplot(x='total_bill',y='tip',data=tips, kind='kde', fill=True)



# ------------    pairplot    ------------
# pairplot will plot "pairwise relationships" across an entire dataframe (for the numerical columns) 
# it supports a color hue argument (for categorical columns). 
sns.pairplot(tips)
# it applies jointplot to all possible combination of our dtaset's numerical columns
# so it takes more time for larger dataFrames
# good way to quickly visualize our data

# hue using 'sex' variable from our dataset
# we have to use a 'categorical' column like "sex"
# use "palette" to modify color
sns.pairplot(tips, hue='sex', palette='coolwarm')



# ------------    kdepot, rugplot    ------------
# A rugplot is a simple plot that places a "dash mark" for each point in a "univariate" distribution
# They are the building block of a KDE plot
sns.rugplot(tips['tip'])

# compare to histogram: shows how many dashes (stacked) in a bin, 
# less high in "histogram" means less dashes in "rugplot"
# sns.histplot(tips['tip'], kde=True)
sns.distplot(tips['tip'], kde=True)

# ----  kdeplot  ----
# if we just want the kde only (not bins)
sns.kdeplot(tips['tip'])




# ----  How to build "kde" using "rugplot"?  ----
# kde has a kind of relation with rugplot count
# kde: kernel density estimation

# we'll construct a dataset, we then observe the "normal Gaussian distribution" of the dashes of rugplot, 
# and then we'll see how to construct kde from those distributions (by adding)

# to observe this, we'll copy some code (don't worry about understanding this code)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    # "stats.norm" plots the normal distribution for each of the rugplot
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)

# notice in the figure: each of the normal-distribution for each of the bule-dashes
# each normal distribution is centered around each dash
# we're having bunch of them in top of each other
    # now we're going to "sum them all up" to get the "kernel density basis function"
    # to do that we're going to use following code


# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")

# Note: that's how the "kdeplot" is constructed in the "distplot"


# ----  kdeplot and rugplot togateher  ----
sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])

sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])
