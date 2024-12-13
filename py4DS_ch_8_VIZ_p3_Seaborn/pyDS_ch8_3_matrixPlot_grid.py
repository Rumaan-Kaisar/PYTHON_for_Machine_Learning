
################# 9.4: full, 9.5:2.50
# copy:  
#        
#        
################# (12-Dec-24 for 13-Dec-24)

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
# Order maintained
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
# No order maintained
# The clustermap uses "hierarchal clustering" to produce a clustered version of the heatmap.
sns.clustermap(flPv)

# Notice that the years and months are now grouped by "passenger count" similarity rather than being in order. 
# For example, August and July are similar, which makes sense as both are summer travel months

# cluster columns and rows togather based of their similarity
# notice the "years" axis and "month" axis.
# notice the months/years are not in order: 
#   months with nearby values (passengers) are grouped first then paires are grouped and so on
#   i.e. they're clustured by months with similar values
#   same goes for "year"
# Eg: 1959 and 1960 are similar and "april" and "july"

# change colormap
sns.clustermap(flPv, cmap="coolwarm")

# view similarities in normalized scale
sns.clustermap(flPv, cmap="coolwarm", standard_scale=1)
# notice winter moths has low passengers, summer months has more passengers




# ------------    Grids    ------------
# Use sns grid capability to automate subplots based on features on our data
# Grids are plots that let you organize different types of plots into rows and columns, 
    # making it easy to create similar plots grouped by specific features.

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# "iris" dataset: Measurments of different flowers
    # Iris is a genus of 310 flowering plant species known for their vibrant flowers. 
    # The term "iris" is used both as the scientific and common name for all species in this genus.

iris = sns.load_dataset('iris')
iris.head()

# last column of the dataset is for 3-different species
iris['species'].unique()
# other four columns are just features of the flower


# ----  pairplot  ----
# it's just the automated jointplot for the dataset
# just pass the DataFrame, the plot will autometically created
sns.pairplot(iris)


# ----  PairGrid  ----
# pairplot is just simplified version of PairGrid
    # use PairGrid to modify the plots more
    # takes all the numerical columns and grid them up
    # makes a kind of subplots
sns.PairGrid(iris)  # takes all the numerical columns and grid them up

# map scatter-plot using PairGrid
g = sns.PairGrid(iris)
g.map(plt.scatter)

# specify diagonal, upper-diagonal (upper-half), lower-diagonal (upper-half)

