
################# 10.1: full, 10.2: full
# copy:
#        
#        
################# (11-Jan-25 for 12-Jan-25)

# Courses: PrTla PY for DS & ML >    10.1, 10.2, 10.3


# ------------    VISUALIZATION: Pandas Built-in Data Visualization    ------------
# Pandas' built-in visualization capabilities are built on top of Matplotlib.  
# These allow us to call visualization functions directly on a DataFrame.
# For more functionality: use Seaborn instead

# import libraries
import numpy as np
import pandas as pd
import seaborn as sns

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# --------    importing dataset    --------
#  Notice we've specified the index
df1 = pd.read_csv('./y_dataFrame_1.csv', index_col=0)
# notice the index is actually dates (i.e. a time-series)
df1.head()

# following dataset is non-time-series
df2 = pd.read_csv('./y_dataFrame_2.csv', index_col=0)
# notice, it has sequential index insted of time-series
df2.head()


# --------  What can we actually do with these types of DataFrames?  --------

# histogram of 'A' column from df1
df1['A'].hist()     # notice it actually calling "matplotlib"

# so we can add "matplotlib" or "sns" style arguments
df1['A'].hist(bins=30)     # notice it actually calling "matplotlib"

# styling with "seaborn": no effect
    # just import the package, "matplotlib" autometically apply the style
df1['A'].hist(bins=30, edgecolor='black', linewidth=0.5)



# ----  Style Sheets  ----
""" 
    # Matplotlib has different style sheets
    # https://matplotlib.org/stable/gallery/style_sheets/index.html


    * Bayesian Methods for Hackers: bmh, plot_bmh, 
        plt.style.use('bmh')

    * FiveThirtyEight style sheet: fivethirtyeight, plot_fivethirtyeight,
        plt.style.use('fivethirtyeight')

    * ggplot style: ggplot, plot_ggplot
        plt.style.use('ggplot')

    * Dark background style:
        plt.style.use('dark_background')

    * Solarized Light styles:
        plt.style.use('Solarize_Light2')

    * Grayscale style:
        plt.style.use('grayscale')

    * Petroff10 style:
        plt.style.use('petroff10')


    - Style sheets make your plots visually cohesive and professional.
    - You can even create custom style sheets for consistent branding, though it can be a bit tedious.
        
"""
# Call the style:
import matplotlib.pyplot as plt

plt.style.use('ggplot')
df1['A'].hist(edgecolor='white', linewidth=0.5)

plt.style.use('bmh')
df1['A'].hist(edgecolor='white', linewidth=0.5)

plt.style.use('fivethirtyeight')
df1['A'].hist(edgecolor='white', linewidth=0.5)



# --------    pandas built-in plot types    --------
# Pandas provides several built-in plot types, most of which are statistical in nature. These include:
    # *     'df.plot.area': Area plot.
    # *     'df.plot.barh': Horizontal bar plot.
    # *     'df.plot.density': Density plot.
    # *     'df.plot.hist': Histogram.
    # *     'df.plot.line': Line plot.
    # *     'df.plot.scatter': Scatter plot.
    # *     'df.plot.bar': Vertical bar plot.
    # *     'df.plot.box': Box plot.
    # *     'df.plot.hexbin': Hexbin plot.
    # *     'df.plot.kde': Kernel Density Estimate (KDE) plot.
    # *     'df.plot.pie': Pie chart.

# most plots can be done using the DataFrame
    # call the DataFrame itself, or
    # use a column of the DataFrame
# then use plot(), specify "kind"
    # we can use 'df.plot(kind='hist')' and replace 'hist' with 
    # any other type from the list above (e.g., 'box', 'barh', etc.)

import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Histogram
df1['A'].plot(kind='hist')




# ----  using methods directly  ----
# anything of Matplotlib can be applicable to "df.plot"

# instead of using kind='hist' we can directly call hist()
df1['A'].plot.hist(edgecolor='white', linewidth=0.5)
# Histogram with specified bins
df1['A'].plot.hist(bins=50, edgecolor='white', linewidth=0.5)

# area plot, shows area of the values
df2.head()
df2.plot.area()
# use "alpha" for transperancy
df2.plot.area(alpha=0.5)

# barplot: takes index values as category
    # so index in our DataFrame should be "categorical"
    # sinc ethe dataset is so small, it won't matter
df2.plot.bar()

# make a stacked barplot
df2.plot.bar(stacked=True)



# ----  lineplot: plot the data according to time-series  ----
# specify x and y: we set index as x and any column as y
df1.plot.line(x=df1.index, y=df1['B'])  # raising ERROR: KeyError: "None of [Index(['2000-01-01', . . ., are in the [columns]
# adjust the figsize, linewidth 'lw'
df1.plot.line(x=df1.index, y=df1['B'], figsize=(12,3)) # raising ERROR

# ERR resolve: 
    # Pandas plot.line requires both x and y to be column names in the DataFrame, 
    # but df1.index is the DataFrame's index, not a column.

# Solution 1: Pandas will use the Index Automatically if x is not explicitly provided
df1['B'].plot.line(figsize=(12,3))
# or
df1['B'].plot.line(figsize=(16,3), linewidth=0.5)

# Solution 2: Create a new column called 'date' from the 'df1.index'
df1['date'] = df1.index
df1.plot.line(x='date', y='B')

# Solution 3: reset the index (altering the DataFrame)
df1.reset_index(inplace=True)  # Moves index into a column named "index"
df1.plot.line(x='index', y='B')



# scatterplots, need to specify x, y
df1.plot.scatter(x='A', y='B')
# setting color based off of another column, 'c' means color
# we can also choose colormap
df1.plot.scatter(x='A', y='B', c='D', cmap="coolwarm")
# in this way we can see 3-levels of information: 'A' vs 'B' vs 'D'

# relative sizing: 's' means size
# NOTE: s parameter needs to be an array, not just the name of a column
    # if we set the column s=df1['D'], the poins will be small
    # so we have to multiply the values by some factors
df1.plot.scatter(x='A', y='B', alpha=0.20, s=df1['D']*100)
# Now points on the scatterplot is A vs B and 
    # size indicates the size of 'D' values, relative to each other


# ----  Boxplot  ----
# We've seen sns boxplot; however, for a quick overview, we can use pandas boxplot.
df2.plot.box()
# It takes each column as a category and plots their distributions as box plots.


# ----  Hexagonal Bin plot  ----
# for bivariate data we can do Hexagonal Bin plot

# Let's first create a bivariate data
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df3

df3.plot.hexbin(x='a', y='b')

# increasing bin size
df3.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')


# ----  KDE: Kernel Density Estimation  ----
# to plot only kernel density estimation
df2['a'].plot.kde()
# or
df2['a'].plot.density()

# to entire DataFrame. Plots KDE for each of the columns
df2.plot.density()




# ------------    Pandas Data Visualization practice    ------------
# We'll use our 3rd DataFrame for this
# Our goal is to recreate the plots

# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# --------    importing dataset    --------
dTfr = pd.read_csv('./y_dataFrame_3.csv')
dTfr.head()
dTfr.info()

# Make "scatter plot" of b vs a. Set color and size of the points. Resize the figure (stretch)
# 's': size, 'edgecolor' and 'linewidth' used for border
dTfr.plot.scatter(x='a', y='b', figsize=(12,3), c='red', edgecolor='black', linewidth=0.5, s=100)


