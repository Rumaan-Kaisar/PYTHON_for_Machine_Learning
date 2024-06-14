
################# 6.1: FULL, 6.2: full, 6.3: 3.41
# copy:  
#        
#        
################# (12-jun-24 for 14-jun-24)

# Courses:  PrTla PY for DS & ML >   6.1, 6.2, 6.3
#           Previously: py4DS_ch_2_dataFrame 



# ------------    pandas    ------------
# pandas is a library for datascience tools
    # it is used for data analysis and manipulation
    # it provides data structures like "DataFrame" and "Series" for handling and analyzing structured data.

# we can call it: python version of excel or python vesrsion of R

# Pandas is an open source library built on top of "NumPy" 
    # i.e. you need to learn numpy first

    # It allows for :
            # fast analysis 
            # data cleaning  
            # preparation

    # It excels in performance and productivity
    # It also has built-in data-visualization features
    # It can work with data from a wide variety of sources.

# install: 
    # open cmd          >>  pip install pandas
    # or open conda     >>  conda install pandas


# --------   Objectives   --------
    # Series 
    # DataFrames 
    # Missing Data 
    # GroupBy
    # Mergingjoining^nd Concatenating 
    # Operations
    # Data Input and Output: csv, excel files, SQL and more



# --------    series    --------
# it's the one of the "Pandas Data-type"
    # we'll use series a lot to build Data-Frames

# A "series" is very similar to "numpy-array"
    # it's actually built on top of "numpy-array object"

# The difference bewteen "pandas-series" and "numpy-array" is:
    # series can access lebels, i.e. it can "indexed by labels"


# lets create some series from various object types
import numpy as np
import pandas as pd

# we create 4 different python objects: 2 lists, 1 np-array, 1 dict
laBls = ['a', 'b', 'c']
my_dt = [10, 20, 30]
arr = np.array(my_dt)   # convert to numpy-array
dct = {'a':10, 'b':20, 'c':30}


# ------  creating a series  ------
    # pd.Series() takes lots of parameters. 
    # We'll use the parameters "data" & "index"
pd.Series(data=my_dt)   # notice the index appears autometically

# The special thing is: we can set our own index
# following we set the list "laBls" as the index to the "Series"
sr_1 = pd.Series(data=my_dt, index=laBls)
sr_1

# so unlike np-array we can have lables in a Series
# we can access the elements by their 'lables'


# ----  other ways to create a series  ----



