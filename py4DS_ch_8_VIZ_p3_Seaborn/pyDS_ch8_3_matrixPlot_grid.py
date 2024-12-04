
################# 9.4: 2.38
# copy:  
#        
#        
################# (30-Nov-24 for 01-Dec-24)

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

# using correlation
tc = tips.corr()     # notice the same variable names in the column and row

# creating heatmap
sns.heatmap(tc)

# rev[2.38 03-dec-2024]

