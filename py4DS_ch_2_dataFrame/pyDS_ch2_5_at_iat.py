
# Courses: A-Z PY for Data-Science    5.7

# Loading Dataset
import pandas as pd
stats = pd.read_csv('./DataDemographic.csv')    # load datset

# rename to one words
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

stats.head()    # view dataset


# --------    Accessing individual element/cell    --------
stats[1, 2] # won't gonna work
# We have to use at(), and iat() functions

# .at for 'LABELS'. Important: even integers (counting trated as label) are treated as labels 
# .iat for "integer location".

# .iat() : following looks at 3rd row and 5th column
stats.iat[2, 4] # 'Upper middle income'

# .at() : following looks at 'labeled 2 row' and 'labeled IncomeGroup column'
stats.at[2, 'IncomeGroup'] # 'Upper middle income'

# more example
stats.iat[0,1]
stats.at[2, 'BirthRate']

# Both gives the same result, but they works differently
    # Notice the following example, it gives different result
    # The reason is : 
        # .iat() is looking for 'integer-index' whereas
        # .at() is looking for 'LABELS'

# Example: why we need at()
sub_10 = stats[::10]    # 10 multiple rows

# looking at '10 INDEXED row and 0 INDEXED column' at new dataframe
sub_10.iat[10, 0]   # 'Libya'

# looking at '10' LABELED row and column LABELED 'CountryName' at new dataframe
sub_10.at[10, 'CountryName']    # 'Azerbaijan'

# that's why the results are different


