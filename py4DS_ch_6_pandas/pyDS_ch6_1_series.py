
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
    # but we mostly use DataFrames instead of Series

# A "series" is very similar to "numpy-array"
    # it's actually built on top of "numpy-array object"

# The difference bewteen "pandas-series" and "numpy-array" is:
    # series can access lebels, i.e. it can "indexed by labels"


# lets create some series from various object types
from audioop import avg
import numpy as np
import pandas as pd

# we create 4 different python objects: 2 lists, 1 np-array, 1 dict
laBls = ['a', 'b', 'c']
my_dt = [10, 20, 30]
arr_1 = np.array(my_dt)   # convert to numpy-array
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


# --------    other ways to create a series    --------
# ----  using NumPy-array  ----
pd.Series(arr_1)
# we can also attach our "index" to it
pd.Series(data=arr_1, index=laBls)

# ----  using Dictionary  ----
    # the "keys" will become index and 
    # "values" will be corresponding data-points
pd.Series(data= dct)    # passing dictionary as data



# --------    pandas-Series can hold "any types"    --------
# Note:
    # another thing that differentialte pandas-Series from numpy-array
    # pandas-Series can hold "any types" as data points
# strings as data points
pd.Series(data= laBls)

# function references as data points
    # we can insert "list of functions" as data-points into a Pandas-Series
    # in that case the Series will hold the function-referances as the data-points
# following we use "list of built-in functions" as data-points
pd.Series(data= [sum, avg, max, min], index=["s", "a", "mx", "mn"])



# ----  using index of a series  ----
    # The key to using a Series is: understanding its index.
    # it works like a "HASH-table" or a "dictionary"

# grab information from a Series.
ser_1 = pd.Series(data=[1,2,3,4], index=['USA', 'Germany', 'USSR','Japan'])
ser_2 = pd.Series(data=[1,2,5,4], index=['USA', 'Germany', 'Italy','Japan'])
ser_3 = pd.Series(data= laBls)
# dtype shows the type of the data: "int64" for integers, "object" for strings and others

# accessing data: specify the index labels
ser_1['USA']
ser_3[2]


# basic operations are done w.r. to "index"
# addition:
    # try to match-up the operation based on the undex
    # eg: 'USA'  matched and thus it will be 2
    # "NaN" is used for non-matched items. eg: 'USSR' & 'Italy'
ser_1 + ser_2 

# Note: "int" will convert to "float" Working with NumPy or Pandas based object
#           it's done to retain all the information. eg: int-division data loss


