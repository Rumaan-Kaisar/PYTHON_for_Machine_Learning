
# Courses: A-Z PY for Data-Science    5.5

# --------    basic operations with a DATA FRAME    --------

# Loading Dataset

import pandas as pd

stats = pd.read_csv('./DataDemographic.csv')    # load datset
stats.head()    # view dataset

# Subsetting (review)
stats[['Country Code','Birth rate','Internet users']][4:8]




# --------    Mathematical opeartions    --------
# very similar to Matix operations
result = stats['Birth rate'] * stats['Internet users']  # multiply one column with another
result.head()

# rename to one words
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
result_2 = stats.BirthRate * stats.InternetUsers    # multiply on ecolumn with another
result_2.head()




# --------    Add a column to the dataframe    --------
# 'stats.MyCalc' short-cut way wont work
stats['MyCalc'] = result_2  # adding a column named 'MyCalc' whic stores our calculated result_2
stats.head()    # checking

# adding another column
stats['MyCalc_2'] = result_2 = stats.BirthRate / stats.InternetUsers
stats.head()    # checking


# Comparison with R (vecctorize vs non-vectorize)
# we can do followung operation in R
stats['xyz'] = [1, 2, 3, 4, 5, 6]   # ERR: no recycling optioon

# above give an ERR in Python, because each column has 193 elements
    # ValueError: Length of values does not match length of index
    # However in R it will work. Why?
        # Recycling Vector in R: Since R is a vectorize Programming language, 
        # it can recycle the values if youu supply some values
        # basically it pouplates rest of the column by copying supplied values




# --------    Remove a column from the dataframe    --------
# you have to specify the axis, i.e. row = 1, column = 0
    # axis : {0 or 'index', 1 or 'columns'}, default 0, i.e. removes row by default
# parameter-name, use the name of the parameter if the order is known, eg. stats.drop('MyCalc', 1)
    # eg: 'axis', 'index', 'labels' etc
stats.drop('MyCalc', axis=1)    # removes column called 'MyCalc'
stats.drop(index=[0, 1, 2])    # removes first 3 rows
stats.drop(columns=['MyCalc_2'])    # removes column called 'MyCalc'

# remove multiple columns
stats.drop(columns=['CountryName', 'BirthRate'])    # removes columns 'CountryName', 'BirthRate'

# 'stats' itself is unchanged
stats.head()

# ----  use assignmnet to uupdate  ----
# Note that applying 'drop()' will 'return a new object'
# so 'stats' is not changed, to update it we need 'assignment statement'
stats = stats.drop(index=[0, 1, 2], columns=['CountryName', 'BirthRate'])
stats.head()


