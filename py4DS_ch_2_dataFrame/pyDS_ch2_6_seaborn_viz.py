
# Courses: A-Z PY for Data-Science    5.8, 5.9

# Loading Dataset
import pandas as pd
stats = pd.read_csv('./DataDemographic.csv')    # load datset

# rename to one words
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

stats.head()    # view dataset



# ----------------      seaborn      ----------------
# seaborn: statistical data visualization

# seaborn is a very powerful package of python for vizualization
    # Seaborn is a Python visualization library based on "matplotlib". 
    # It provides a high-level interface for drawing attractive statistical graphics.

    # Online documentation is available at 'seaborn.pydata.org'


# install via CLI: pip install seaborn


# 'matplotlib' is needed along with 'seaborn'



# introduction to seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# plot shown in Jupyter Notebook
%matplotlib inline  
# expand the figure-width
plt.rcParams['figure.figsize'] = 8, 4

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')





# Visualize 'Distribution'
    # practice with live-data
# we'll use distplot(), 
    # there are some important ploot functions like: 
        # barplot(), boxplot()
        # FacetGrid(), PairGrid(), clustermap(), 

viz_1 = sns.distplot(stats.InternetUsers)
plt.show()  # use matplot to show the plot
# Note: This function has been deprecated and will be removed in seaborn v0.14.0. 
    # It has been replaced by 'histplot' and 'displot', two functions with a modern API and many more capabilities.

# More Modification. e.g. 'increase bars'
    # use 'bins', 'hist'
viz_1 = sns.distplot(stats.InternetUsers, bins=30)
# observations: 
# some countries has internet users between 0 & 20% acces to internet
    # most of the countires has 30% to 70% access
    # the curve slowly drops off for 100% access
    # the curve is "double bell-shaped"


# --------    Boxplots    --------
# we'll visualize 'IncomeGroup' vs 'BirthRate'
viz_2 = sns.boxplot(data = stats, x='IncomeGroup', y='BirthRate')
plt.show()

# Observations: 
# for "HighIncome" group the birth rate is sitting between 10 & 15 and its 12, there are also 1st, 2nd, 3rd quartels
# also notice 'outlier', the "arrow or little ball" upward, indicating "High Income group" has high-birth-rate
    # also "Low Income group" has low-birth-rate
# notice "High Income" birthrate is closer to "Low middle Income" and 
    # "Low Income" birthrate is closer to "Lower middle Income"



# --------  Seaborn gallery  --------
# seaborn Example gallery : use the examples to plot something awesome 
# https://seaborn.pydata.org/examples/index.html

# kdeplot: cubehelix palettes : https://seaborn.pydata.org/examples/palette_generation.html
# violinplot: Grouped violinplots with split violins : https://seaborn.pydata.org/examples/grouped_violinplots.html
    # Violinplot from a wide-form dataset: https://seaborn.pydata.org/examples/wide_form_violinplot.html

# Replacement for deprecated tsplot (not used anymore)
    # Timeseries plot with error bands : https://seaborn.pydata.org/examples/errorband_lineplots.html




# Example 1: Now we try to analyze "BirthRate vs InternetUsers", we'll trt to find pattern inside of these data
                # plot these parameters against each other

# --------  lmplot()  --------
# lm : linear model
# lmplot() : Plot data and regression model fits across a FacetGrid.
viz_3 = sns.lmplot(data = stats, x='InternetUsers', y='BirthRate')
# plt.show()
# always use keywards for argumnets, to avoid 'order of the arguments'
    # use the order (x, y, data) if you dont use keywards

# Observations:
    # the data isn't look like a 'linear relationship'
    # so we cannot fit a 'linear-regression model' to these data, so we set it false 'fit_reg=False'
    # pattern: 'more internet user' lower the 'birth-rate'
    # the data more looks like '1/x' kind-of non-liner relation
viz_3 = sns.lmplot(data = stats, x='InternetUsers', y='BirthRate', fit_reg=False)

# viz_4 = sns.distplot(stats.BirthRate, bins=30)

# Now we braek it up into 'IncomeGroup' categorical data
# add some color, we use 'hue' attribute for 'IncomeGroup' categorical data 
    # along with 'InternetUsers' and 'BirthRate'
viz_3 = sns.lmplot(data = stats, x='InternetUsers', y='BirthRate', hue='IncomeGroup', fit_reg=False)

# observations : we're observing relation between 3-data at once
    # low interent users has high birth-rate and has 'low income'
    # high internet users have low birth-rate and hsa 'Hihg income'



# ----  resize 'FacetGrid'  ----
# 'FacetGrid' takes lots of space
# to resize it need it's own paramters
    # 'size : resize' and 
    # aspect : acpect ratio (1, 1.5, 2, 3 etc to increase width; 0.5, 0.75 etc for decrease width)
viz_3 = sns.lmplot(data = stats, x='InternetUsers', y='BirthRate', hue='IncomeGroup', fit_reg=False, size = 10, aspect=2)

# The 'size' parameter has been renamed to 'height' in new version 0.13
viz_3 = sns.lmplot(data = stats, x='InternetUsers', y='BirthRate', hue='IncomeGroup', fit_reg=False, height=10, aspect=2)


