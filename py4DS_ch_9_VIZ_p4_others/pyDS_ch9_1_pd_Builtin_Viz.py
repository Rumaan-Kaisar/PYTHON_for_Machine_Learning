
################# 10.1: 7.53
# copy:
#        
#        
################# (07-Jan-25 for 08-Jan-25)

# Courses: PrTla PY for DS & ML >    10.1, 10.2, 10.3


# ------------    VISUALIZATION: Pandas Built-in Data Visualization    ------------
# Pandas' built-in visualization capabilities are built on top of Matplotlib.  
# These allow us to call visualization functions directly on a DataFrame.

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

