
# Courses: A-Z PY for Data-Science    6.8, 6.9 : Facet Grid, Coordinates and Diagonals


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



# ------------    Facet Grid    ------------

# PREVIOUSLY we created following plot:
    # lmplot: recall 'pyDS_ch2_8_HW_wrldTrnd.py', 'pyDS_ch4_3_Subplots_KDE.py'
plt.style.use("seaborn")    # background color
vis2_lm = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating', fit_reg=False, hue='Genre', height=6, aspect=1, scatter_kws={'s': 10})
vis2_lm.set(xlim=(-20, 120), ylim=(-10, 110))   # setting x,y axis range

# it's a scatterplot
    # we got lots of different 'Genre' on one chart
    # thre are too many points and we're not getting clear insights
    # It's showing us Overall-Analytics:
    
# Facet Grid solvs that problem, 
    # it let us to analyze Density and Trends by splitting the chart
    # we need to split this chart, to make more simplified visualization
    # we'll plot multiple charts for seperate 'Genre' or othet 'criteria'


# ----  Facet Grid  ----
# first we need to prepare the facetgrid as below
    # we specify the dataset, 
    # we have to specify the type of 'Facet-grid', we set 'Genre' for both
        # we used 'raw' and 'hue'
        # 'raw' creates no. of rows for each 'Genre'
        # 'hue' colorize the rows (with differnt colors) for each 'Genre'
        # col='Year' creates no. of columns 

fct_grd_1 = sns.FacetGrid(movies, row='Genre', hue='Genre')

fct_grd_2 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')

# Above creates an epty list of plots
    # 7 rows corresponds to 'Genre' and 5 columns for 'Year'
    # we have to populate those with our plots
    # the concept is simialr to 'subpot' but its different

# 'sublot' vs 'facetgrid'
    # in 'sublpot' we populate it with different plots
        # we do comparison between different plot

    # in 'facetgrid' we're splitting a plot for better view.
        # we compare between data evolution
        # we're splitting-up a visualization w.r.to certain rules
        # we can't populate the array with different 



# ----  map()  ----
# use map(), to map something in facet grid
    # we use map() to populate the facetgrid 

# fct_grd_2.map(), for example we'll plot 'scatter'
    # the scatterplot will split across all of the grids for 'Year' and 'Genre'
    # fct_grd_2 is some kind of construct that we've created
    # following is the usual scatterplot
plt.scatter(movies.CriticRating, movies.AudienceRating)

# applying facet-grid to visualize 'CriticRating vs AudienceRating' evolution through 'Years' for different 'Genre'
# we'll map the 'scatter' on our facetgrid
# the function "plt.scatter" itself is passed as a parameter to FacetGrid(), and 
    # 'CriticRating', 'AudienceRating' as x & y data
    # notice no '()' used with 'plt.scatter' and we don't need to specify the dataset 'movies', i.e. "movies.CriticRating" 
        # also notice quatation "'" is used: 'CriticRating', 'AudienceRating'
    # beacuse our facetgrid "fct_grd_3" already built on the datset 'movies'
fct_grd_3 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
# plt.scatter(movies.CriticRating, movies.AudienceRating)
fct_grd_3.map(plt.scatter, 'CriticRating', 'AudienceRating')
# It maps 'func' in each of the grid of our facetgrid
# it based on the 'movies' dataframe and splitting the 'plt.scatter' accorss the grid according to 'Genre' & 'Year'
# Vertically it splitted by 'Year' and horizontally by 'Genre'
# colored by the rows according to 'Genre'

# general form is:
    # fct_grd_3.map(func, *args, **kwargs)
    # fct_grd_3.map() is going to map 'func' in each of the grid of our facetgrid



# populate facet-grid using different plot/chart: plt.hist
fct_grd_4 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
# plt.hist(movies.BudgetMillions)   # histogram
    # since histogram needs only one variable, we use 'fct_grd_4' as below
fct_grd_4.map(plt.hist, 'BudgetMillions')
# Note: sometimes it could be bit tricky to implement some sort of plot/chart and 
    # sometimes research needed to know how to populate specific types of chart




# Styling the plots using 'kwargs'
    # here the 'kw_rgs' used to set: size of the dots, border for each dots with edge-color black
    # notice the 'kw_rgs dictionary' passed to fct_grd_5.map()
    # it will makes the points a little bigger and helps to analuze
fct_grd_5 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kw_rgs = dict(s=50, linewidth=0.5, edgecolor='black')
fct_grd_5.map(plt.scatter, 'CriticRating', 'AudienceRating', **kw_rgs)
# note: In this chart, for specific 'Genre', we compare each scatter w.r.to 'Year'
    # We compare from left to Right, to notice the 'evolution'

# Observations:
# We can notice the relation between 'CriticRating' & 'AudienceRating' is evolving throughout the 'Year'
    # We can get some sort-of trends from the scatter-plot:
    # 'Action' movies: in 2009 it becomes little scattered, and in 2011 it forms two groups
    # 'Comedy' movies: More condensed in 2010, more lined-up in 2011
    # 'Comedy' movies: More condensed at top-right corner in 2011

# For analytics & visualizations in python 'facetgrid' is a useful tool




# ------------    Controlling Axes and Adding Diagonals    ------------
    # the facetgrid is telling us about the evolution of 'CriticRating' & 'AudienceRating' relation

# specify x, y range:
    # notice that the rage is from (-20, -20) to (100, 100)

# diagonal lines
    # we need a "Diagonal Line" for better comparison of 'CriticRating' vs 'AudienceRating'
    # to view tah the dots lie 'above the diagonal' or "below"
    # above: 'AudienceRating' is higher than 'CriticRating'
    # below: 'CriticRating' is higher than 'AudienceRating'

fct_grd_6 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kw_rgs = dict(s=50, linewidth=0.5, edgecolor='black')
fct_grd_6.map(plt.scatter, 'CriticRating', 'AudienceRating', **kw_rgs)

# set limit for x, y axis:
fct_grd_6.set(xlim=(0, 100), ylim=(0, 100))

# to draw diagonal for eacg of the grid we have to use a "FOR-loop"
    # because python isn't a vectorizr programming language like R
for ax in fct_grd_6.axes.flat:
    ax.plot((0, 100), (0, 100), c='gray', ls='--')

# fct_grd_6.axes: is an array of the subplot (array of the elements of the facetgrid)
    # we use "flat" on top of that to iterate over the array easily, 
    # since facetgrid is a 2D array and 'flat' will treat it as a list

# shortly: 'fct_grd_6.axes' gets the elements of the facetgrid as an array
    # 'flat' will flatten the array we get from 'fct_grd_6.axes'
    # ax.plot((0, 100), (0, 100), c='gray', ls='--')    plots the diagonal line
        # c='gray' is the color of the line, 
        # ls='--' is the line style (dashed)


# Observations:
    # in 2009 'AudienceRating' is much higher than 'CriticRating'
        # we can easily observe that, since most of the dots are above the diagonal
    # we can see the oppsite for Thriller & Drama in 2011, where 'CriticRating' is higher 

# adding legend
fct_grd_6.add_legend()


