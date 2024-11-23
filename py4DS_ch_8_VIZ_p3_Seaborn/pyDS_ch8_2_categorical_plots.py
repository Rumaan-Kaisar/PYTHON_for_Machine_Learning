
################# 9.3: 4.33
# copy:  
#        
#        
################# (22-Nov-24 for 23-Nov-24)

# Courses: PrTla PY for DS & ML >    9.3


# ------------    categorical plots    ------------

# Seaborn provides several plot types for visualizing categorical data, including:
    # factorplot
    # boxplot
    # violinplot
    # stripplot
    # swarmplot
    # barplot
    # countplot

# For categorical plots, we'll focus on visualizing the distributions of categorical columns 
    # such as 'sex,' 'smoker,' 'day,' or 'time' in relation to either numerical or other categorical columns.


# import libraries
import seaborn as sns
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# lets load a builtin dataset of seaborn. tips: a dataset of restaurant patrons' tipping behavior
tips = sns.load_dataset('tips')
tips.head()



# ------------    barplot and countplot    ------------
# These similar plots help visualize aggregate data for a categorical feature:
    # Barplot: Displays aggregated categorical data based on a function (default is the mean).
    # Countplot: Shows the count of observations in each category.

# We can think of it as the visualization of a Pandas groupby action.

""" 
Aggregate data:
    Aggregate data refers to data that has been combined or summarized to represent a "higher-level overview".
    Instead of looking at individual data points, it groups or combines them using specific functions like:
        Sum
        Mean
        Count
        Median
        Standard deviation
"""

# ----  barplot  ----
# it aggregate the categorical data based on a function (mean is default)
sns.barplot(x='sex', y='total_bill', data=tips)
# notice x is categorical and y is numerical
# shows mean of 'total_bill' per categorical value i.e. 'sex': 'male' or 'female'
    # observation: average 'total_bill' of male is higher than female

# change estimator object (affects the grouping/aggregation)
# estimator: also called aggregate function 
    # Statistical function to estimate within each categorical bin.
    # by default it is the mean
    # also we can put our custom function
    # it's just a "groupby" mechanism

# following aggregate on "std-deviation"
import numpy as np
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)



# ----  countplot  ----
# mostly same as "barplot" except the estimator is explicitly counting the "number of occurrences"
    # thats why we only pass the x value (which is categorical):
sns.countplot(x='sex',data=tips)
# more male than female



# ------------    boxplot and violinplot    ------------



# rev[19-Nov-2024]




