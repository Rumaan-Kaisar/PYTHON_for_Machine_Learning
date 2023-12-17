
# Courses: A-Z PY for Data-Science    5.4


# ------------    subsetting    ------------
# subsetting dataframes in PANDAS

# We will do this in 3-parts
    # -Rows
    # -Columns
    # -Combine the two

# Loading Dataset

import pandas as pd

stats = pd.read_csv('./DataDemographic.csv')    # load datset
stats.head()    # view dataset




# ----  PART 1: subset by Rows  ----
# Its exactly similar to "SLICING" matrix or list
    # 'slice by ROWs' is deafault
    # usually when we slice a dataset we slice it by ROWs
        # Note: In case of MATRIX we sepearted 'rows', 'columns' by comma ','

# its because in most of the cases 
    # these 'structures' has heading at the top and data goes down
    # new entry of data added at the bottom

# Note that the real data-set 'stats' wont change unless we make an ASSIGNMENT
# stats = stats[::-1]

stats[20:25]    # last index not inclusive
stats[0:25]
stats[100:110]

# every thing 
stats[:]

# from 185 to the end
stats[185:]

# from start to 10
stats[:10]  # same as stats.head(10)


# Reverse
# Note that the real data-set 'stats' wont change (modified) unless we make an ASSIGNMENT
# stats = stats[::-1]
stats[::-1]     # wont change the real data
stats

# Get only every 20th country
stats[::20]




# ----  PART 2: subset by columns  ----
# To get the columns: Just specify the 'name of the column'
    # and to get the ROWs just use 'slicing-technique'

stats.columns    # Get all the name of the columns first
# ['Country Name', 'Country Code', 'Birth rate', 'Internet users', 'Income Group']

stats['Country Name']   # access the specific column
# Note that aboove is not a data-frame
    # if we use only one column, it wont be a data-frame
    # it's some kind of list to do other staff

# However, if we use 2 or more columns, we'll get a Data-frame
    # we first need to create a "list of column-names": e.g. ['Country Name', 'Birth rate']
    # at first-lok following may look like a 2d-matrix but the fist '[]' is with 'stats' object
        # we're just passing a list into stats[] object
        # In R you'd be passing a Vector: c('CountryName', 'BirthRate'), so in that case no '[[' happens
stats[['Country Name', 'Birth rate']]

# also note that, we can create our own ORDER
stats[['Country Code', 'Country Name', 'Internet users']]


# we can also use head() on those data-frames
stats['Country Name'].head()
stats[['Country Code', 'Country Name', 'Internet users']].head(15)


# Convention!!
# --------  quick Acess - requires the name to be one word  --------
    # this is only good for 'one column'
    # also the name needs to be one word

stats.head()    # check the column names
# rename to one words
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

stats.birthRate # quick access, (R has similar '$' operator: stats$birthRate)
stats.birthRate.head()




# ----  PART 3: subset by combining 'ROW & COLUMNS'  ----
# we can combine Rows and Columns in 2 ways
    # subset by rows (seperate ROWs first) - then subset by columns
    # subset by columns (seperate COLUMNs first) - then subset by rows
    # actually we're doing "Two-Subsetting at once"
    # both cases we can same result

# seperate ROW first
stats[20:30][['CountryName', 'CountryCode']]
# above works, because 'stats[20:30]' is also a Data-frame, we then apply 'column-seperaton' on it
    # we can break it down as below
df_1 = stats[20:30]
df_1[['CountryName', 'CountryCode']]

stats[20:30:2][['CountryName', 'BirthRate']].head(3)    # we can also use head()


# seperate COLUMN first
stats[['CountryName', 'CountryCode']][20:30]
# stats[['CountryName', 'CountryCode']] itself a Data-frame, we then apply 'row-seperaton' on it
    # we can break it down as below
df_2 = stats[['CountryName', 'CountryCode']]
df_2[20:30]

stats[['CountryName', 'BirthRate']][20:30:2].head(3)    # we can also use head()


