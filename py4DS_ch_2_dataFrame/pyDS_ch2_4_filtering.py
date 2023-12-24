
# Courses: A-Z PY for Data-Science    5.6

# Loading Dataset
import pandas as pd
stats = pd.read_csv('./DataDemographic.csv')    # load datset

# rename to one words
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

stats.head()    # view dataset


# --------    Filtering Data-Frames    --------
# filtering is important in Data-Science
    # it helps to find 'insights' and subset the data in proper way

# Filtering is all about ROWs
    # we look at the columns to filter the rows
    # eg: 'filter High Income', 'all countries starting with letter B'

stats.InternetUsers < 2
# It gives a list of 'True' and 'False'
# These valuse tells us 'which ROWs meet the condition'

filtered_1 = (stats.InternetUsers < 2)
filtered_1.head(15)

# Now we can filter the ROW's using these True-Flase values
    # We gonna use our 'filtered_1' object

# we'll use 'True-Flase values' to slicing ROWs
stats[filtered_1]
# conceptually this is juust like R




# --------  More Filtering : Practice  --------
filtered_2 = (stats.BirthRate > 40)
stats[filtered_2]

# Or we can put the 'condition' inside '[]'
stats[stats.BirthRate > 40]




# --------    combine two conditions    --------
# We need to use 'bitwise and: &' instead of logical-and 'and'
stats[(stats.BirthRate > 40) and (stats.InternetUsers < 2)] # gives ERR. Why??
# ValueError: The truth value of a Series is ambiguous.
    # '(stats.BirthRate > 40) and (stats.InternetUsers < 2)' causing the ERR
    # because 'and' works with single value, it doesn't know how to work with 'list'
    # Its tryin to convert the whole series/list (stats.BirthRate > 40) into a single 'True' or 'False' value
    # Note that: in R we won't get this ERR, because R is 'vectorize-prgramming-language'

# To resolve this, we need to use 'bitwise and: &'
    # It'll deal with element-element level
    # it's straight-forward if we think True=1 and False=0
        # then ['False', 'False', 'False', 'True', 'True'] & ['False', 'False', 'False', 'True', 'False']
        # is actually [0, 0, 0, 1, 1] & [0, 0, 0, 1, 0] = 00011 & 00010 = 00010
filtered_1 & filtered_2
stats[filtered_1 & filtered_2]

# following also gives same result
stats[(stats.BirthRate > 40) & (stats.InternetUsers < 2)] # gives ERR. Why?? Didn't use '()'



# --------    More Filtering    --------
# Filter Categorical data
stats[stats.IncomeGroup == "High income"]

# How to get all 'Unique Categories'
stats.IncomeGroup.unique()  # shows all the 'categories' used in a column

# Quick Exercise: Find specific data/row
# Find out everything about the country 'Malta'
stats[stats.CountryName == "Malta"]

# Find out everything about the country 'Malta', 'Canada', 'China'. HINT: use 'Bitwise OR |'
stats[(stats.CountryName == "Malta") | (stats.CountryName == "Canada") | (stats.CountryName == "China")]


