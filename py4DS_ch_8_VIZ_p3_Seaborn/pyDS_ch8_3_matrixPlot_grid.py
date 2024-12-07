
################# 9.4: 07.26
# copy:  
#        
#        
################# (06-Dec-24 for 07-Dec-24)

# Courses: PrTla PY for DS & ML >    9.4, 9.5

# ------------    Matrix Plots    ------------
# Matrix plots display data as color-encoded matrices and can highlight clusters within the data.
# We'll learn how to create matrix plots (primarily heatmaps) in Seaborn.
# Let's explore Seaborn's heatmap and clustermap:

# import libraries
import seaborn as sns
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# lets load a builtin dataset of seaborn. we import 2 datasets: 'tips' and 'flights'
    # tips: a dataset of restaurant patrons' tipping behavior
    # flights: shows the number of passengers for each month of given years
tips = sns.load_dataset('tips')
tips.head()

flights = sns.load_dataset('flights')
flights.head()


# --------    heatmap    --------
# heatmap : primary way of showing the matrix plots
# in order to work with heatmap, our data need to be in "matrix form"
# "index name" and "column name" should match up so that 
#       the "cell value" indicates something relavant to both of those index name and column name

# matrix form
# consider "tips" dataframe. Variables (columns and row index) needs to be same
# we can use many methods
    # 1. through a pivot table
    # 2. Getting correlation data


# ----  using correlation  ----
tc = tips.corr()     # notice the same variable names in the column and row

# creating heatmap
sns.heatmap(tc)
# it just color those values based on some gradient scales
# it helps to compare relative values of a correlation

# annotations (show the values)
sns.heatmap(tc, annot=True)

# setting colormap
sns.heatmap(tc, annot=True, cmap='rainbow')


# ----  using Pivot  ----
# Pivot: use pivot table for Flight data. We transform this data as below: 
    # set "month" is the "index"
    # set "year" as "columns"
    # set number of passengers as "values"
flPv = flights.pivot_table(index='month', columns='year', values='passengers')
flPv    # notice the correlation
# heatmap
sns.heatmap(flPv)
# notice as the year increase, there's more flight
# also notice the popular months are the summer months: June, July, August

# change color map "cmap"
sns.heatmap(flPv, cmap='magma')

# to seperate the squares: linecolor, linewidth
sns.heatmap(flPv, cmap='coolwarm', linecolor='white', linewidth=1)



# --------    clustermap    --------
# The clustermap uses "hierarchal clustering" to produce a clustered version of the heatmap.

# rev[07.26 06-dec-2024]

