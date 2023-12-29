
################# 5.8: 6:57
# copy:  
#        
#        
################# (27-dec-23 for 29-dec-23)

# Courses: A-Z PY for Data-Science    5.8, 5.9

# Loading Dataset
import pandas as pd
stats = pd.read_csv('./DataDemographic.csv')    # load datset

# rename to one words
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

stats.head()    # view dataset



# ----------------      seaborn      ----------------
# seaborn: statistical data visualization

# seaborn is a very powerful package of python for vizualization
    # Seaborn is a Python visualization library based on "matplotlib". 
    # It provides a high-level interface for drawing attractive statistical graphics.

    # Online documentation is available at 'seaborn.pydata.org'


# install via CLI: pip install seaborn


# 'matplotlib' is needed along with 'seaborn'


# seaborn Example gallery : use the examples to plot something awesome 
# https://seaborn.pydata.org/examples/index.html

# kdeplot: cubehelix palettes : https://seaborn.pydata.org/examples/palette_generation.html
# violinplot: Grouped violinplots with split violins : https://seaborn.pydata.org/examples/grouped_violinplots.html
    # Violinplot from a wide-form dataset: https://seaborn.pydata.org/examples/wide_form_violinplot.html

# Replacement for deprecated tsplot (not used anymore)
    # Timeseries plot with error bands : https://seaborn.pydata.org/examples/errorband_lineplots.html


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





# Visualize 'Distribution'
    # practice with live-data
# we'll use distplot(), 
    # there are some important ploot functions like: 
        # barplot(), boxplot()
        # FacetGrid(), PairGrid(), clustermap(), 

viz_1 = sns.distplot(stats.InternetUsers)
# Note: This function has been deprecated and will be removed in seaborn v0.14.0. 
    # It has been replaced by 'histplot' and 'displot', two functions with a modern API and many more capabilities.

# More Modification. e.g. 'increase bars'
    # use 'bins', 'hist'
viz_1 = sns.distplot(stats.InternetUsers, bins=30)


# --------    Boxplots    --------
