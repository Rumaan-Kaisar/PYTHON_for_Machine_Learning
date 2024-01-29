
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
# Our approach will be more related on 'Programming' rather than data-science
# Histogram of 'BudgetMillions'
hst_1 = plt.hist(movies.BudgetMillions)
plt.show()  # shows plot without any info


# Specific 'Genre' Histogram of 'BudgetMillions'
# Filter data for specific Genere. eg: 'Drama'
is_drama = (movies.Genre == 'Drama')   # Budget on certain 'Genre'
is_drama

# Now we create new data-frame for 'Drama-movies' only
drama_movies = movies[is_drama]     # ONLY Drama-movies data

# Visualize Drama-movies 'BudgetMillions'
hst_2 = plt.hist(drama_movies.BudgetMillions)
plt.show()


# Using same approach we can visualize Action-movies cost
    # NOTICE how we combine 3-steps using a single line
    # However it just vizualize the histogram
    # if we created the specific data-frame for 'Action-movies' we coud use it later
hst_3 = plt.hist(movies[movies.Genre == 'Action'].BudgetMillions)   # Action-movies Budget

# More Visualizations
hst_4 = plt.hist(movies[movies.Genre == 'Comedy'].BudgetMillions, bins=15)   # Comedy-movies Budget
hst_5 = plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins=15)   # Thriller-movies Budget



# Above Historams are 'Manually codded' for different 'Genre'
    # Now we use a FOR-LOOP to make saperate Data-farme for each 'Genre'
    # Then we visualize those in a single plot
        # Currently they're behaind each-other (hst_4 & hst_5)
        # We want them 'stacked on top of each-other'

# 'Stacked Histogram'
    # To create a 'Stacked Histogram' we need to pass a list of data-frame in hist()
    # the list of budgets of 'Comedy' & 'Thriller':
        # [movies[movies.Genre == 'Comedy'].BudgetMillions, movies[movies.Genre == 'Thriller'].BudgetMillions]
stckHst_1 = plt.hist([movies[movies.Genre == 'Comedy'].BudgetMillions, movies[movies.Genre == 'Thriller'].BudgetMillions], bins=15)
# Notice the bars is presented 'side-by-side' instead of 'stacked-on-top'
    # set attribute stacked = True
bdgt_ls1 = [movies[movies.Genre == 'Action'].BudgetMillions, movies[movies.Genre == 'Drama'].BudgetMillions]
stckHst_2 = plt.hist(bdgt_ls1, bins=15, stacked=True)


# We have 7 Genre, we can do the stacked plot manually
    # what if we had 100 Genre?
    # We have to solve it using python coding. We'll use 'For-loop'

# get all the 'Genre'
all_genre = movies.Genre.cat.categories
all_genre = list(all_genre) # convert to 'List'

# create the list of data-frames
bdgt_ls2 = []
for gnr in all_genre:
    bdgt_ls2.append(movies[movies.Genre == gnr].BudgetMillions)

# visualize
stckHst_3 = plt.hist(bdgt_ls2, bins=15, stacked=True)
plt.hist(bdgt_ls2)


# also we can use following code
list_1 = list()
for gen in movies.Genre.cat.categories:
    list_1.append(movies[movies.Genre == gen].BudgetMillions)
hs_1 = plt.hist(list_1) # side-by-side

# stacked 
    # remove gap between the bars (side): rwidth=1. range (0, 1)
hs_2 = plt.hist(list_1, bins=30, stacked=True, rwidth=1)

# Legends
all_genre = list(movies.Genre.cat.categories)
hs_3 = plt.hist(list_1, bins=30, stacked=True, rwidth=.8, label=all_genre)
plt.legend()
plt.show()

# Note: in 'R' or 'Tablue' it's more easy to create stacked-histogram



# -=-=-=-    using 'seaborn'    -=-=-=-
# 'seaborn' as sns. We do this in one line of code
hist_sns_1 = sns.histplot(data=movies, x='BudgetMillions', hue='Genre', multiple="stack", shrink=.8, linewidth=0, bins=30) 
# hue='Genre' gets all the 'Genre'
# shrink=.8 is similar to 'rwidth'
# multiple="stack" is similar to stacked=True
# linewidth=0 removes borders of the bars
# bins=30 number of bars

# What are 'bins'?
    # A histogram displays numerical data by grouping data into "bins" of equal width. 
    # Each bin is plotted as a bar whose height corresponds to how many data points are in that bin. 
    # Bins are also sometimes called "intervals", "classes", or "buckets".


