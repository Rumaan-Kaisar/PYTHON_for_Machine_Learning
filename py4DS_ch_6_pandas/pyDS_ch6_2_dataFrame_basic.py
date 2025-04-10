
# Courses: PrTla PY for DS & ML >   6.4, 6.5(11:38)

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



# --------    loc[], iloc[], at[], iat[]    --------
# Select row / columns using loc[], iloc[], at[], iat[]
# more detail: "py4DS_ch_9_VIZ_p4_others"

# Create an area plot of all the columns for just the rows up to 30. (hint: use .ix)
# Note: ".ix" was an indexer, but now deprecated and removed in Pandas 1.0.0
# instead select rows using: loc[] and iloc[] or at[], iat[]

# df.loc[raw_index, col_name]           eg: df.loc[2, 'column_name'], Selects a value by index label and column name
# df.iloc[raw_index, col_index]         eg: df.iloc[2, 3], Selects a value by row index and column index positions
# df.at[raw_index, col_name]            eg: df.at[2, 'a']. For fast access to a single scalar value by label.
# df.iat[raw_index, col_index]          eg: df.iat[2, 1]. For fast access to a single scalar value by integer position.

dTfr.iloc[:30, 2:].plot.area(alpha=0.5)
dTfr.loc[:30, ['a', 'b']].plot.area(alpha=0.5)

# Create an area plot of all the columns for just the rows up to 30.
dTfr.loc[:30].plot.area(alpha=0.5)




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
# instead of using conditions like "fd > 0", we'll use row/column values eg. fd['c2'] > 0
    # it'll only returns the rows / columns as the subset of DataFrame where condtions are true
    # where 'fd' is the whole dataset and 
    # fd['c2'] is a column

# "fd > 0" : condition for entire DataFrame
# "fd['c2'] > 0" : condition for a column

# Using fd[fd['c2'] > 0] will return a subset of the dataframe containing 
    # only the rows where the condition is true for the column "c2", instead of returning NaN.


# using column-condition
    # operation fd[fd['c2'] > 0] filters the dataframe "fd" to include 
        # only the rows where the values in column c2 are greater than 0.
fd['c2'] > 0    # condition for column c2

# filtering the DataFrame fd with condition "fd['c2'] > 0"
fd[fd['c2'] > 0]


# using row-condition
    # we have to use "loc" and slicing operator ":"
# we can filter "fd" for a row
fd.loc['r3'] > 0    # condition for row r3

# filtering the DataFrame fd with condition "fd.loc['r3'] > 0"
fd.loc[:, fd.loc['r3'] > 0]

# get all the rows where 'c4' < 0
# it returns the row 'r3', because it has -ve value in column 'c4'
fd[fd['c4']<0]

# work with resulting DataFrame, after filtering
reslt  = fd[fd['c2'] > 0]

# get result's 2nd row
reslt.loc['r3']     # because r2 and r4 are eliminated in "reslt"

# result's 1st column
reslt['c1']

# we can do it in a lingle line
fd[fd['c2'] > 0]['c1']

# getting multiple columns
fd[fd['c2'] > 0][['c2', 'c4']]

# getting 2nd row
fd[fd['c2'] > 0].iloc[1]

# "fd[fd['c2'] > 0][['c2', 'c4']]" is equivalent of following lines togather
boolser = fd['c2'] > 0 
result = fd[boolser] 
mycols = ['c2', 'c4'] 
result[mycols]
# since more variables use more memory, "fd[fd['c2'] > 0][['c2', 'c4']]" recommended



# --------  multiple conditions  --------
# use bitwise "&", "|" instead of "and", "or"

# following will return an error
fd[(fd['c2'] > 0) and (fd['c4'] > 1)]   # ERR
# Why error? The truth value of a Series is ambiguous
    # because python normal "and" operator can't compare a "Series of Boolean" to another "Series of Boolean"
    # "and" operator deal with single Boolean value at a time. E.g. True and True, True and False

# Use bitwise-AND operator "&"
    # always use () for seperations between conditions
fd[(fd['c1'] > 0) & (fd['c3'] > 1)]   # Notice "&" instead of "and"

# similarly we can use bitwise-OR operator "|"
fd[(fd['c1'] > 0) | (fd['c3'] > 1)]   # Notice "|" instead of "or"

