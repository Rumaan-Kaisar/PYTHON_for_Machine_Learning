
################# 6.5: full, 6.6: 1.04
# copy:  
#        
#        
################# (03-jul-24 for 05-jul-24)

# Courses: PrTla PY for DS & ML >   6.5(11:40), 6.6, 6.7

import numpy as np
import pandas as pd

# retun random numbers from "standared NORMAL distribution" centered around 0
from numpy.random import randn

np.random.seed(101)
rnd_20 = randn(5, 4)

fd = pd.DataFrame(data=rnd_20, index=["r1", "r2", "r3", "r4", "r5"], columns=["c1", "c2", "c3", "c4"])



# ------------    changing index    ------------
# ----  reset_index  ----
fd
# resetting index to default
fd.reset_index()
# notice the old-index "r1", "r2", "r3", "r4", "r5" moved to a column
# now the actual index reset 0,1,2,3,4

# Note that: it doesn't occurs "inplace"
    # to make the change, use "inplace"
fd
# use
# fd.reset_index(inplace=True)


# ----  set_index  ----
# Awesome trick to create a list
    # calling split() on a string!!
    # don't need to typ ',' or ""
newind = "CA NY WY OR CO".split()   # split on a blank space
newind

# we insert this "newind" to our DataFrame,
    # notice the dimension must match
fd['States'] = newind
fd

# column as index: setting a column as index
    # instead of resetting we want the column "States" to be the index of our DataFrame
    # use set_index() instead of reset_index()
fd.set_index("States")  # overrides the old-index
# note: we need to apply 'inpalce'
# also we cannot retain information from the old-index (as in reset_index)




# --------    multi-index    --------
# multi-index DataFrame
import numpy as np
import pandas as pd

# two lists
# "Gl G1 G1 G2 G2 G2".split()
outside = ['Gl', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]

# create a "list of tuples / pairs"
hier_index = list(zip(outside,inside))  # zip is used to create pair (a, b)
hier_index  # [('Gl', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

# creating "Multi-index"
# "pd.Multiindex.from_tuples" creates a multi-index from a "list of tuples"
hier_index = pd.Multiindex.from_tuples(hier_index)
hier_index



# ---- rev[03-jul-2024: Update the code, not giving same output] ----


# create the DataFrame

# GPT:
# Multi-index DataFrame
import numpy as np
import pandas as pd

# Two lists
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]

# Create a "list of tuples / pairs"
hier_index = list(zip(outside, inside))  # zip is used to create pairs (a, b)
print(hier_index)  # [('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

# Creating "Multi-index"
# "pd.MultiIndex.from_tuples" creates a multi-index from a "list of tuples"
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

# Create a DataFrame with the multi-index
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
print(df)



# working with a multi-index DataFrame






# --------    index-hierarchy    --------


