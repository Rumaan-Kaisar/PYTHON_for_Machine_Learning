
################# 6.7:
# copy:  quartiles image, txt (rev)
#        
#        
################# (6-feb-24 for 7-feb-24)

# Courses: A-Z PY for Data-Science    6.7


# ------------    Load Dataset & Libraries    ------------
# Import the following packages needed to perform the analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# plot shown in Jupyter Notebook
%matplotlib inline  
# expand the figure-width
plt.rcParams['figure.figsize'] = 8, 4


# Loading Dataset
# Import the csv dataset
movies = pd.read_csv("./MovieRatings.csv")     # load datset

# -=-=-  Explore the data  -=-=-
# Visualize the dataframe
movies

# rename the column names to single-string names
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.head()    # view dataset


# ----   convert 'numerical-type',' object-type' to "categorical-type"   ----
movies.Film = movies.Film.astype("category") # use assignment '=' to update the dataset
movies.Genre = movies.Genre.astype("category")   
movies.Year = movies.Year.astype("category")   
movies.info()   # check the data-type changes




# ----------------    violinplots vs boxplots    ----------------
# we'll plot 'violinplots' and 'boxplots'
    # we'll compare which one is better & which one people often use

z = sns.violinplot data=movies, x='Genre , y= CnticRatmg
z = sns.violinplot(data=movies, x='Genre', y='CriticRating')

# ----  rev  ----
""" 
What are Quartiles?
Quartiles are three values that split your dataset into quarters.

A median divides a given dataset (which is already sorted) into two equal halves similarly, the quartiles are used to divide a given dataset into four equal halves. Therefore, logically there should be three quartiles for a given distribution, but if you think about it, the second quartile is equal to the median itself! 

These values are the following:

Q1 First quartile: 25% of the data are below this value.
Q2: Second quartile / Median: This value splits the data in half.
Q3 Third quartile: 25% of the data are above this value.
Quartiles also correspond to percentiles. Q1 is the 25th percentile, Q2 is the 50th, and Q3 is the 75th.

How to Find Quartiles
The simple method for finding quartiles is to list the values in your dataset in numeric order. Then find the three values that split your data into quarters, as shown below.

        11
        13
        16
        19
        20  # Q1
        21
        23
        25
        26
        29 # Q2 or Median
        33
        34
        36
        38
        39 # Q3
        46
        52
        55
        58

 """

