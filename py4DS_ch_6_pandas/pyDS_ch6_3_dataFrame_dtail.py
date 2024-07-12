
################# 6.5: full, 6.6: full, 6.7: 1:40
# copy:  
#        
#        
################# (10-JUL-24 for 12-JUL-24)

# Courses: PrTla PY for DS & ML >   6.5(11:40), 6.6, 6.7

import numpy as np
import pandas as pd

# retun random numbers from "standared NORMAL distribution" centered around 0
from numpy.random import randn

np.random.seed(101)
rnd_20 = randn(5, 4)

fd = pd.DataFrame(data=rnd_20, index=["r1", "r2", "r3", "r4", "r5"], columns=["c1", "c2", "c3", "c4"])



# ------------    changing index    ------------
# ----  reset_index  ----
fd
# resetting index to default
fd.reset_index()
# notice the old-index "r1", "r2", "r3", "r4", "r5" moved to a column
# now the actual index reset 0,1,2,3,4

# Note that: it doesn't occurs "inplace"
    # to make the change, use "inplace"
fd
# use
# fd.reset_index(inplace=True)


# ----  set_index  ----
# Awesome trick to create a list
    # calling split() on a string!!
    # don't need to typ ',' or ""
newind = "CA NY WY OR CO".split()   # split on a blank space
newind

# we insert this "newind" to our DataFrame,
    # notice the dimension must match
fd['States'] = newind
fd

# column as index: setting a column as index
    # instead of resetting we want the column "States" to be the index of our DataFrame
    # use set_index() instead of reset_index()
fd.set_index("States")  # overrides the old-index
# note: we need to apply 'inpalce'
# also we cannot retain information from the old-index (as in reset_index)




# --------    multi-index (index-hierarchy)    --------
# multi-index DataFrame
import numpy as np
import pandas as pd

# two lists
# "Gl G1 G1 G2 G2 G2".split()
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]

# create a "list of tuples / pairs"
hier_index = list(zip(outside,inside))  # zip is used to create pair (a, b)
hier_index  # [('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

# creating "Multi-index"
# "pd.Multiindex.from_tuples" creates a multi-index from a "list of tuples"
hier_index = pd.Multiindex.from_tuples(hier_index)
hier_index
# MultiIndex(levels=[[' G1', 'G2'], [1, 2, 3]], labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])

# creating a Dataframe using above Multi-Index
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
# np.random.randn(6, 2) creates a 6x2 matrix of 12 random numbers
# you'll notice the 2-level of index
    # 1st level [' G1', 'G2']
    # 2nd leevl [1, 2, 3] for each G1 and G2
    # so followwing is called: "Multi-level index" or "Index-Hierarchy"

""" 
                A	        B
    G1	1	0.622117	1.271678
        2	1.084815	0.474254
        3	-0.448297	0.217219
    G2	1	0.117091	0.311963
        2	-0.033285	-1.006097
        3	1.835885	-0.526372
"""


# working with a multi-index DataFrame:
    # Accessing data from a multi-level indexed DataFrame
    # we'll use row-selection first
    # call most-outside index and proceed deeper

# Grab most-outside index, we'll get a sub-DataFrame
df.loc['G1']
# then we use next level of index
df.loc['G1'].loc[1]     # returns the first row (labeled '1') of 'G1' as a Series

# accessing a single element, using both raw-index and column-index
df.loc['G2'].loc[2]['B']
# row.row.column, no '.' is used for column i.e. no attribute used

# naming multi-level index
df.index.names  # notice no names
df.index.names  = ["Groups", "Num"]
df



# ------    cross-section (xs)    ------
# returns cross-section of row(s) or column(s) in multi-indexed dataframe
# everything under 'G1'
df.loc['G1']    # using 'loc'
df.xs('G1')     # using 'xs', also notice '()' used

# xs can skip levels to get deep into multi-level-index
    # 'xs' mostly used data-visualization projects, to grab stacked-indexed data
    # lets grab "both Num=1 indexs" from both 'G1' and 'G2' groups
        # it's little bit treacky using 'loc'
df.xs(1, level="Num")
# above gets all "1 indexes" from index-level named "Num"




# ------------    missing data    ------------
# There are methods that can deal with missing data

# pandas wwill autometically fill the missing data with "NaN" value. 
# we can do either:
    # drop the NaN 
    # fill the NaN 

import numpy as np
import pandas as pd

# create a DataFrame
# just like we could create a "Series" from a "Dict", 
    # we can create a "DataFrame" from a "Dict" as wwell
    # the keys 'A', 'B', 'C' will be the columns
    # the points will be "list" of values for "each key"
    # we'll use "np.nan" to make a missing value
dCt = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

# To create a DataFrame we just pass the dictionary as a argumnet to pd.DataFrame()
df2 = pd.DataFrame(dCt)
df2
# notice 1st-row nad 3rd-column has no missing values


# ----  dropna()  ----
# drops any rows and columns that contains 1 or more NaN values
# axis = 0, row-wise is default
df2.dropna()    # drops rows

# drop columns
df2.dropna(axis=1)

# it can also specify a "threshold" for non-NA values, if we set the parameter "thresh"
    # "thresh = 2" keeps all rows / columns that has "at least 2" non-Na values
df2.dropna(thresh=2)    # keep rows, that has "at least 2" non-NaN values
df2.dropna(thresh=1)    # keep rows, that has "at least 3" non-NaN values


# ----  rev[10-JUL-2024]  ----

# ----  fillna()  ----
# fills the NaN with a given value
# following fills with a string


# following fills with a mean


