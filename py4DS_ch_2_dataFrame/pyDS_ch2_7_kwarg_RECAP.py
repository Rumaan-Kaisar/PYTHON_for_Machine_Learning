
################# 5.10 : full
# copy:  
#        
#        
################# (2-jan-24 for 3-jan-24)

# Courses: A-Z PY for Data-Science    5.10, 5.11

# In previous plot we had very small 'markers'
    # now we'll resize the 'markers'
    # to do this we'll use "Keyward Arguments"

# Loading Dataset
import pandas as pd
stats = pd.read_csv('./DataDemographic.csv')    # load datset

# rename to one words
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
stats.head()    # view dataset

# introduction to seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# plot shown in Jupyter Notebook
%matplotlib inline  
# expand the figure-width
plt.rcParams['figure.figsize'] = 8, 4

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')




# --------    Keyword Arguments in Python    --------
# The 'size' parameter has been renamed to 'height' in new version 0.13
viz_3 = sns.lmplot(data = stats, x='InternetUsers', y='BirthRate', hue='IncomeGroup', fit_reg=False, height=10, aspect=2)

# there is no keywars in 'lmplot' for "colors or marker-size"
# We need 'keyward arguments', these are passed to 'plt.scatter' and 'plt.plot'
    # since 'seaborn' is built on 'matplotlib' and we're using 'pyplot' as 'plt'
    # most of the parameters of 'seaborn' are from "pyplot"
    # if you need to pass additional parameters from 'seaborn', use "{scatter, line}_kws: dictionaries"

    # from "pyplot" documentation:
        # matplotlib.pyplot.scatter
        # 'lmplot' is actually a wrapper of 'matplotlib.pyplot.scatter'
        # therer are other parameters of 'matplotlib.pyplot.scatter' not listed in 'lmplot'
            # we can use those as kwargs: e.g. 's' is the parameter for 'size'
            # we'll use a dictionary to pass thoose kwargs scatter_kws = {"key1": val1, "key2": val2, . . . }. 
            # seaborn will pass thoe 'kwargs' to 'pyplot' to take the actions
            # eg.   scatter_kws = {"s": 200}

# using 'kwargs' & 'dictionaries'
viz_4 = sns.lmplot(data = stats, x='InternetUsers', y='BirthRate', hue='IncomeGroup', fit_reg=False, height=10, aspect=2, scatter_kws={'s': 100})



