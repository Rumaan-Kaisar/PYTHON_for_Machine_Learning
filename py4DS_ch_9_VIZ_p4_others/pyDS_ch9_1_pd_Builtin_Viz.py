
################# 10.1: 2.55
# copy: csv files, py, ipynb
#        
#        
################# (04-Jan-25 for 05-Jan-25)

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


# --------    pandas built-in plot types    --------



