
################# 6.3: full, 6.4: 
# copy: replacing_seaborn_distplot.ipynb
#        
#        
################# (26-jan-24 for 27-jan-24)

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


# CriticRating
hist_5 = sns.histplot(data=movies, x='CriticRating', kde=True, bins=15, kde_kws=dict(cut=3))
# without 'cut' only actual range of the data shown
    # 'cut=3' used to get 'full curve'
 

# ----    Another way to plot "Distribution" using pyplot 'plt'    ----
# Since seaborn is built on top of 'matplotlib.pyplot', we can directly use 'pyplot'
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5,)   # grid styling
plt.style.use("seaborn")    # background color
hist_5 = plt.hist(movies.AudienceRating, bins=15, edgecolor='black', linewidth=.2)
# edgecolor='black', linewidth=.2 used to show 'bar edege'
# Also notice the plot is RANGED from 0 to 100 (instead of -20 to 120)


# ----   seaborn styles    ----
# To reset all styles of seaborn use: 
# sns.set_style("white")

# To get a seaborn style use:
sns.set_style("darkgrid")
hist_6 = sns.distplot(movies.AudienceRating)


# Observations:
    # What is special about above 2 chatrs for: 'AudienceRating' & 'CriticRating' ?

    # 'AudienceRating' has a kind of NORMAL distribution
        # it's based on human rating using their 'natural intuition' on movies 

    # 'CriticRating' has some kind of UNIFORM distribution
        # there is a kind of average line between '20 to 30'
        # this rating is based on critria: movie-plot, story-telling, ligting, sound-effect




# ------------    STACKED HISTOGRAMS in python    ------------

# -=-=-=-    using 'pyplot'    -=-=-=-
# Histogram of 'BudgetMillions'
hst_1 = plt.hist(movies.BudgetMillions)
plt.show()  # shows plot without any info

# Specific 'Genre' Histogram of 'BudgetMillions'
# Filter data for specific Genere. eg: 'Drama'
drama_Bgt = (movies.Drama == 'Drama')



