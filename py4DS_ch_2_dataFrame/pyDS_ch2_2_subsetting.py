
################# 5.4: 6:35
# copy:  
#        
#        
################# (26-sep-23 for 27-sep-23)

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




# ----  subset by Rows  ----
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
