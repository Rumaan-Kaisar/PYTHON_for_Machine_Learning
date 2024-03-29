
# Courses: A-Z PY for Data-Science    6.1, 6.2


# ------------    Categorical variables    ------------
# most of the time some 'categorical data' will appear in your Dataset
    # you need to know how to deal with 'catgrical data'
    # you have to deal with both 'catgrical data' and 'numerical data' simultaniusly


# import libraries & Dataset
import pandas as pd

# import os
# os.getcwd()     # get current working directory

movies = pd.read_csv("./MovieRatings.csv")

# check length of the dataset
len(movies)

# Explore the dataset
    # checking the datsset is a good habit 
    # however we can't fully explore if the dataset is too big and lots of columns
        # we can't see all the columns for example, if there is 1000 columns
movies.head()
movies.columns  # get column info

# RENAME the columns so that we can use '.' operator
    # notice "Rotten Tomatoes Ratings %" is actually a 'Critic Rating'
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.head()



# -=-=-=-  categorical data  -=-=-=-
# which data should we treat as category?
    # 'Year' is a numerical data, but we should treat it as 'category'. Why?
    # lets do more exploration to understand the reason - 

# Get some information
movies.info()

# Notice we have 6 columns
    # 2 of those are 'objects' but not 'category' yet
    # 4 of those are int type

    # 'CriticRating', 'AudienceRating', 'BudgetMillions' are meaningful in int-type
        # these can have mean, variance, max, min and other statistical-data

    # But "Years" cannot be treated as 'int-type'. There is no mean, variance for "Years"
        # We don't really treat "Years" as numerical data. "Years" is a 'Ctegorical data'
        # We have to convert "Years" from NUMERICAL data to 'CTEGORICAL data'
        # Notice right now we have mean, variance, max, min, 25%(1st quartel), 50%(median), 75%(3rd quartel)  for "Year". Which is absurd.


# Statistical info
movies.describe()
# mean, variance, max, min, 25%(1st quartel), 50%(median), 75%(3rd quartel) make sense for 
    # 'CriticRating', 'AudienceRating', 'BudgetMillions'
    # those statistical info have no meaning foor "Year"
        # So we treat "Year" as categorical data
        # "Years" are presented as numbers, but there could be moonths (Jan, Feb, Mar)
        # after transformatioon to categorical variable we can still do some basic arithmatic operation like 'Dofference', 'max', 'min'


# ----   convert 'numerical-type',' object-type' to "categorical-type"   ----
movies['Film'].astype("category")   # way 1: using [] to access column
movies.Genre.astype("category")   # way 2: using '.' to access column

# use assignment '=' operation to update the dataset
movies['Film'] = movies['Film'].astype("category")
movies.Genre = movies.Genre.astype("category")   # way 2: using '.' to access column
movies.Year = movies.Year.astype("category")   # way 2: using '.' to access column


# Explore the changes
movies.head() 
movies.info()   # notice the 'obect-type' are converted to 'category'
# in 'R-programming'  categories are called fdactors



# Getting 'uniques' used in a 'category' columns
    # there are 7 different 'Genres' on movies
movies.Genre.cat.categories
# Another way: How to get all 'Unique Categories'
movies.Genre.unique()  # shows all the 'categories' used in a column

# in 'R' these categories are called 'labels' or 'factors'

# Explore the 'statistical-info' again
    # notice 'Year' is no longer considered as 'numerical data', it act as 'category'
movies.describe()
 
# Conclusion: Above are the 'Data preparation step' for Data-analysis
    # Key point is how deal with 'categorical data' when we prepare our dataset
        # how to force data to act as 'categorical data'. Eg: 'years'
    # also its a good practice to explore the dataset before Data-analysis




# ------------    jointplots    ------------
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


# --------    Loading Dataset    --------
# Import the csv dataset
movies = pd.read_csv("./MovieRatings.csv")     # load datset

# -=-=-  Explore the data  -=-=-
# Visualize the dataframe
movies

# rename the column names to single-string names
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.head()    # view dataset


# -=-=-=-  Chart 1: Jointplots  -=-=-=-
# select dataset, sepcify the columns
jnPlt_1 = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating')

# What does the 'Jointplots' shows us:
    # basically it's a 'scatterplot', 
    # showing: is there any dependencies between 'CriticRating' and 'AudienceRating'
        # if we draw a diagonal, 'AudienceRating' stays above the diagonal
        # i.e. 'AudienceRating' usually greater than 'CriticRating'
        # However, for higer ratings 'AudienceRating' starts to match 'CriticRating', 
            # i.e. points getting near to the diagonal (more or less)
    # it helps us to visualize multivariate distribution 

    # 2 distributions
    # in jointplot we have 2 ditsributions on the top, and on the right
        # useful for bi-variate distribution,
        #  because the scatterplot alone we cannot get any idea about the distributions of the 'seperate variables'
        # notice 'AudienceRating' is some kind of 'normal ditribution'
        # also notice 'CriticRating' is a kind of 'uniform ditribution'

# Styling: 'Hexagonal' clustered presentation
    # change the style of the jointplot
    # to style jointplot use 'kind' attribute with values: 'scatter', 'reg', 'kde', 'hex'
    # Eg: 'hex' gives 'Hexagonal' kind of 'grops of the dots'. It kind of make a 'cluster'
        # Notice the clusters are associated with their corresponding distribution
        # color is denser if both distribution meets high values.
jnPlt_1 = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating', kind='hex')
# in python its easy to create, but in 'R', you have to give some effort

# Another try
jnPlt_2 = sns.jointplot(data=movies, x='AudienceRating', y='BudgetMillions', kind='kde')

# Try same variable for x, y both
jnPlt_1 = sns.jointplot(data=movies, x='AudienceRating', y='AudienceRating', kind='hex')


