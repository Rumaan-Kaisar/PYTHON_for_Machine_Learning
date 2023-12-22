
################# 5.6: 1:15
# copy:  
#        
#        
################# (20-dec-23 for 22-dec-23)

# Courses: A-Z PY for Data-Science    5.6

# Loading Dataset
import pandas as pd
stats = pd.read_csv('./DataDemographic.csv')    # load datset
stats.head()    # view dataset


# --------    Filtering Data-Frames    --------
# filtering is important in Data-Science
    # it helps to find 'insights' and subset the data in proper way

# Filtering is all about ROWs
    # we look at the columns to filter the rows
    # eg: 'filter High Income', 'all countries starting with letter B'


