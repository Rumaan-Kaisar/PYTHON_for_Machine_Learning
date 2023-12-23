
################# 5.6: 8:00
# copy:  
#        
#        
################# (22-dec-23 for 23-dec-23)

# Courses: A-Z PY for Data-Science    5.6

# Loading Dataset
from msvcrt import open_osfhandle
from os import O_RDONLY
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


