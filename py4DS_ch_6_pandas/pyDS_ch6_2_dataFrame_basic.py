
################# 6.4: full, 6.5: 0.53
# copy:  
#        
#        
################# (19-jun-24 for 21-jun-24 )

# Courses: PrTla PY for DS & ML >   6.4, 6.5(1/2)

# ------------    dataframe basics    ------------
# we mainly work with "dataframes" in pandas
    # Dataframes are built from Series objects

import numpy as np
import pandas as pd

# retun random numbers from "standared NORMAL distribution" centered around 0
from numpy.random import randn

# we're going to use np.random.seed(), so that we'll get a same random values
    # np.random.seed() is a function in NumPy that sets the seed for the random number generator.
    # Setting the "seed" to a specific value makes the random number generation predictable
    # Every time you run this code with the seed set to 101, the same sequence of random numbers will be generated.
np.random.seed(101)
rnd_20 = randn(5, 4)
rnd_20



# Note on seed():
""" 
    you do not need to use np.random.seed(101) in each cell of a Jupyter notebook. 
    Setting the seed once will ensure that the random number generator produces 
    the same sequence of random numbers in subsequent calls within the same session. 

    However, the safest way is to run following code in a single cell:

            np.random.seed(101)
            rnd_20 = randn(5, 4)
            rnd_20
"""
# Set the seed
np.random.seed(42)

# Generate some random numbers
random_numbers = np.random.rand(5)

print(random_numbers)




# --------    Building a Dataframe    --------
    # similar to Series(), DataFrame() also takes, "data", "index" as arguments
    # there ia also a "columns" argumnet for columns
    # note that: "index" also represents the rows

# ----  creating a DataFrame  ----
fd = pd.DataFrame(data=rnd_20, index=["r1", "r2", "r3", "r4", "r5"], columns=["c1", "c2", "c3", "c4"])
# randn(5, 4) generates 5x4 matrix of 20 random numbers from "NORMAL distribution"
    # that's why we've used "5-index for 5-rows" and 4-columns

# Each column is a "Pandas-Series", so, "c1" is a Series, as well as "c2", "c3", "c4"
# and they all share a "Common-index"

# Basically all DataFrames is a bunch of series that shares a same index
# we can select these Series-objects



# --------    accessing Series from DataFrame: acessing columns and rows    --------
# method 1: specify the column name
fd['c3']
# it is actually a "Series", we can confirm it by type checking
type(fd['c3'])
# but the type of 'fd' is DataFrame
type(fd)

# method 2: SQL-format, useing "."
    # however it's good to use []-format, 
    # if we use'.', we can get confused with built-in methods (e.g. last, ilk, loc)
    # using SQL-format ".", can overrite those built-in methods with "column-names"
    # so pandas get confused
print(fd.c3)

# multiple columns: use list of column-names
    # we'll get a DataFrame instead of Series
    # single column: Series, multi-column: DataFrame
fd[['c2', 'c4']]



# ----  creating a new column  ----
fd['new1'] = [113, 123, 133, 143, 153]

# or we can use operations
fd['new2'] = fd['c1'] + fd['c2']
fd



# ----  DELETING a column  ----
# use "inplace" to make the change permanenet
# axis: 0 is row, 1 is column
fd.drop('nwe1', axis=1)

# Note: original dataframe not affected, i.e. the column is not deleted
    # not to accidentally lose information, it's done for safety
    # inplace=True, actually occur the changes in-place (to actually delete the data)
print(fd)
fd.drop('nwe1', axis=1, inplace=True)
print(fd)

# drop a row, axis = 0
fd.drop('r2')   # by default axis=0
# fd.drop('r2', axis=0)

# why axis=0 is row, and axis=1 is column?
    # if we notice the shape of the DataFrame
fd.shape    # (row, column)
    # (row, column) is a tuple, row at index 0, and column is index 1



# --------  selecting rows: loc[] and iloc[]  --------
# The "single row" of a DataFrame is also a "Series"
# There is two ways to select rows in a DataFrame
    # loc[] and iloc[] are methods of pandas, but notice we're using "[]" instead of "()"

# loc['label_of_row']   :   label based index
    # notice we have to use "labels" of the row
fd.loc['r2']    # accessing row 2 

# iloc[index_of_row]    :   numeric based index
    # notice in this case we use numerical "index" even if our rows are indexed by strings
fd.iloc[1]    # accessing row 2 




# ------------    subsetting: sub-sets of rows and columns    ------------
# use loc[row, column]
    # "row", "column" can be lables or 'list of labels'

# single value at row "r2" and at column "c3"
fd.loc['r2', 'c3']

# subset of valuees: use lists of "row", "column"
    #  getting values from r1, r3 rows and c2, c4 columns
fd.loc[['r1', 'r3'], ['c2', 'c4']]




# ------------    conditional selections and multi index    ------------

# ------    conditional selections    ------
# we can apply conditional selection using "[]" brackets notation in pandas
# it is very similar to NumPy

# Boolian DataFrame, similar to NumPy-array
fd > 0

# use boolian DataFrame for selection
booLdf = fd > 0

# filter / selecting
    # values for True and NaN for False
fd[booLdf]

# we can do it in single line
fd[fd > 0]

# ------   avoiding "NaN"   ------
# instead of using conditions like "fd > 0", we'll use row/column values
# eg. fd['r1'] > 0
# it'll only returns the rows / columns as the subset of DataFrame where condtions are true

