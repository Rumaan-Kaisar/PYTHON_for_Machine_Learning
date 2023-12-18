
################# 5.5: 5:10
# copy:  
#        
#        
################# (17-dec-23 for 19-dec-23)

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
result = stats['Birth rate'] * stats['Internet users']  # multiply on ecolumn with another
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



