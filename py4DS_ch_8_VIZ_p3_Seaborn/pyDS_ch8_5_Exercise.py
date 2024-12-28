
################# 9.8
# copy:  
#        
#        
################# (27-Dec-24 for 28-Dec-24)

# Courses: PrTla PY for DS & ML >    9.8

# ------------    seaborn exercise    ------------

# Recreate the plots shown below (no need to match the exact colors, just focus on the plot itself)

# Dataset
    # We'll use the famous "Titanic" dataset for these exercises. 
    # Later, in the Machine Learning section, we'll revisit this dataset to predict "passenger survival rates"
    # For now, let's focus on visualizing the data with Seaborn.


# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# --------    "Titanic" dataset    --------
# Using the Titanic dataset, recreate the plots below. 
    # There are very few hints since most can be done with just one or two lines of code, 
    # a hint would essentially reveal the solution
    # so pay close attention to the "x and y labels" for hints.

# lets load a builtin dataset of seaborns: 'titanic'
ttnc = sns.load_dataset('titanic')
ttnc.head()

# plot age-fare distribution in jointpolt
sns.jointplot(x='fare', y='age', data=ttnc, kind='scatter')

