
################# 6.3: 1.30
# copy: replacing_seaborn_distplot.ipynb
#        
#        
################# (23-jan-24 for 24-jan-24)

# Courses: A-Z PY for Data-Science    6.3, 6.4


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



# ------------    HISTOGRAMS    ------------
# We've already used the method to plot 'histogram'
# 'distplot' is used to visualize 'Ditribution in histogram'
# It has been replaced by 'histplot' and 'displot', two functions with a modern API and many more capabilities.
hist_1 = sns.distplot(movies.AudienceRating)

# using 'histplot'
hist_2 = sns.histplot(movies.AudienceRating)

hist_3 = sns.histplot(data=movies.AudienceRating, kde=True) 
# 'kde=True' shows the continuous line plot of the distribution
# plt.grid()    # shows plot grids
# sns.set_style('whitegrid')  # shows grid
# or use with grid()
# hist_2 = sns.histplot(data=movies.AudienceRating, kde=True).grid()

# with categorical data
    # To categorize on 'Genre', use: hue="Genre"
hist_4 = sns.histplot(data=movies, x='AudienceRating', hue='Genre', kde=True) 









