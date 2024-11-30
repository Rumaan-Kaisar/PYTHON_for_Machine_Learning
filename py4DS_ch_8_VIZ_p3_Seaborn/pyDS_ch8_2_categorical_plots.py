
# Courses: PrTla PY for DS & ML >    9.3


# ------------    categorical plots    ------------

# Seaborn provides several plot types for visualizing categorical data, including:
    # factorplot
    # boxplot
    # violinplot
    # stripplot
    # swarmplot
    # barplot
    # countplot

# For categorical plots, we'll focus on visualizing the distributions of categorical columns 
    # such as 'sex,' 'smoker,' 'day,' or 'time' in relation to either numerical or other categorical columns.


# import libraries
import seaborn as sns
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# lets load a builtin dataset of seaborn. tips: a dataset of restaurant patrons' tipping behavior
tips = sns.load_dataset('tips')
tips.head()



# ------------    barplot and countplot    ------------
# These similar plots help visualize aggregate data for a categorical feature:
    # Barplot: Displays aggregated categorical data based on a function (default is the mean).
    # Countplot: Shows the count of observations in each category.

# We can think of it as the visualization of a Pandas groupby action.

""" 
Aggregate data:
    Aggregate data refers to data that has been combined or summarized to represent a "higher-level overview".
    Instead of looking at individual data points, it groups or combines them using specific functions like:
        Sum
        Mean
        Count
        Median
        Standard deviation
"""

# ----  barplot  ----
# it aggregate the categorical data based on a function (mean is default)
sns.barplot(x='sex', y='total_bill', data=tips)
# notice x is categorical and y is numerical
# shows mean of 'total_bill' per categorical value i.e. 'sex': 'male' or 'female'
    # observation: average 'total_bill' of male is higher than female

# change estimator object (affects the grouping/aggregation)
# estimator: also called aggregate function 
    # Statistical function to estimate within each categorical bin.
    # by default it is the mean
    # also we can put our custom function
    # it's just a "groupby" mechanism

# following aggregate on "std-deviation"
import numpy as np
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)



# ----  countplot  ----
# mostly same as "barplot" except the estimator is explicitly counting the "number of occurrences"
    # thats why we only pass the x value (which is categorical):
sns.countplot(x='sex',data=tips)
# more male than female



# ------------    boxplot and violinplot    ------------
# Boxplots and violin plots display the distribution of data.

# Boxplot (box-and-whisker plot): 
    # Summarizes the distribution of quantitative data for comparison across categories.
    # The "box" represents the quartiles (middle 50% of the data).
    # The "whiskers" extend to show the data range, excluding outliers.
    # Outliers are identified based on the interquartile range (IQR).

# x= categorical, y= numerical
sns.boxplot(x='day', y='total_bill', data=tips)

# setting up hue (use another categorical data)
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')
# now we can classify even further. Eg: on Thurseday non-smokers give more tips

# more modifications
# color palette
sns.boxplot(x="day", y="total_bill", data=tips, palette='rainbow')
sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")

# Can do entire dataframe with orient='h'
sns.boxplot(data=tips, palette='rainbow', orient='h')



# ----  violinplot  ----
# A "violin plot" is similar to a "box and whisker plot" but provides more detail about the data "distribution".
    # but it needs more time to understand
# It shows how quantitative data is "distributed across categories" for easy comparison. 
# Unlike a boxplot, it includes a kernel density estimation (KDE), 
    # giving a smooth curve that represents the data's underlying distribution.

# it takes same arguments as boxplot
sns.violinplot(x='day', y='total_bill', data=tips)

# with hue
sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', palette='rainbow')


# with "splitted-hue": gives lot more information
# directly campare the distribution for different categories
    # and compoare categories themselvs on top of x-axis
# Audience: it's useful for more thechnical people (those who can understand it).
# for CEO or executive type management people, it won't help much (for those people use boxplot)
sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', split=True, palette='rainbow')



# ------------    stripplot and swarmplot    ------------
# ----  stripplot()  ----
# Displays a scatterplot where one variable is categorical
# Can be used alone or alongside box/violin plots to show all data points with the underlying distribution.

# in stripplot() we can't tell how many points are on top of each other
sns.stripplot(x="day", y="total_bill", data=tips, palette='Set1', jitter=False)

# to visualize the density use "jitter" in stripplot(), sepertaes the stacked points
# Upodate: by default jitter=True, howver we're going to use it anyway
sns.stripplot(x="day", y="total_bill", data=tips, palette='Set1')

# Notice the difference after using "jitter=True"
sns.stripplot(x="day", y="total_bill", data=tips, palette='Set1', jitter=True)

# using "hue" (more category) and split (seperates the colors)
sns.stripplot(x="day", y="total_bill", data=tips, palette='Set1', hue='sex', jitter=True)
# split parameter is not available in sns.stripplot, use "dodge=True" instead
sns.stripplot(x="day", y="total_bill", data=tips, palette='Set1', hue='sex', jitter=True, dodge=True)


# ----  swarmplot()  ----
# The stripplot is slightly harder to interpret compared to a boxplot/violinplot.
# hence the idea of swarmplot, combining the idea of "violinplot + stripplot"
# swarmplot() is similar to stripplot() but adjusts points along the categorical axis to avoid overlap.
# Better for visualizing distributions but less effective with large datasets 
    # due to clutter and computational complexity.

# we can see all points using swarmplot()
sns.swarmplot(x="day", y="total_bill", data=tips)

# combine a swarmplot with violinplot (on top of each-other)
# Note: The palette is different to make the colors stand out from one another
sns.violinplot(x="day", y="total_bill", data=tips, palette='rainbow')
sns.swarmplot(x="day", y="total_bill", data=tips, palette='Set1')

# another example
sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)



# ------------    factorplot()    ------------
# it's a general form of the above plots
# in addition of x, y, hue and data it take "kind"
    # "kind" describe sthe factor plot itself
    #  eg: kind="violin" or kind="bar"
sns.factorplot(x="day", y="total_bill", data=tips, palette='rainbow', kind="bar")

# "seaborn.factorplot" is deprecated and replaced by "seaborn.catplot", 
# which provides the same features with a more flexible and consistent API.
sns.catplot(x="day", y="total_bill", data=tips, palette='rainbow', kind="bar")


