
################# 6.4: 3.50
# copy:  
#        
#        
################# (18-jun-24 for 19-jun-24 )

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

fd = pd.DataFrame(data=rnd_20, index=["r1", "r2", "r3", "r4", "r5"], columns=["c1", "c2", "c3", "c4"])
# randn(5, 4) generates 5x4 matrix of 20 random numbers from "NORMAL distribution"
    # that's why we've used "5-index for 5-rows" and 4-columns

# Each column is a "Pandas-Series", so, "c1" is a Series, as well as "c2", "c3", "c4"
# and they all share a "Common-index"

# Basically all DataFrames is a bunch of series that shares a same index
# we can select these Series-objects

# --------    accessing Series from DataFrame    --------
# method 1: specify the column name
fd['c3']
# it is actually a Series, we can confirm it by type checking
type(fd['c3'])
# but the type of 'fd' is DataFrame
type(fd)

# method 2: SQL-format, useing "."


