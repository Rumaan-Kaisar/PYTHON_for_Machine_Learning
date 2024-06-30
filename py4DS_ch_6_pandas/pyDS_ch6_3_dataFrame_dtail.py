
################# 6.5: 13.11
# copy:  
#        
#        
################# (29-jun-24 for 30-jun-24)

# Courses: PrTla PY for DS & ML >   6.5(11:40), 6.6, 6.7

import numpy as np
import pandas as pd

# retun random numbers from "standared NORMAL distribution" centered around 0
from numpy.random import randn

np.random.seed(101)
rnd_20 = randn(5, 4)

fd = pd.DataFrame(data=rnd_20, index=["r1", "r2", "r3", "r4", "r5"], columns=["c1", "c2", "c3", "c4"])


# ------------    changing index    ------------
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

