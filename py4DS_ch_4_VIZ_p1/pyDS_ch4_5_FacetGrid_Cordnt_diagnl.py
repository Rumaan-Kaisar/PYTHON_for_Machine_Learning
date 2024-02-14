
################# 6.8: 3.33
# copy:
#        
#        
################# (13-feb-24 for 14-feb-24)

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



# ----  rev[13-feb-24]  ----

# use map(), to plot the data
# fct_grd_2.map(), for example we'll plot 'scatter'
plt.scatter(movies.CriticRating, movies.AudienceRating)

# applying facet-grid to visualize 'CriticRating vs AudienceRating' evolution through 'Years' for different 'Genre'
fct_grd_3 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
# plt.scatter(movies.CriticRating, movies.AudienceRating)
fct_grd_3.map(plt.scatter, 'CriticRating', 'AudienceRating')


# populate facet-grid using different plot: plt.hist
fct_grd_4 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
# plt.scatter(movies.CriticRating, movies.AudienceRating)
fct_grd_4.map(plt.hist, 'BudgetMillions')


# Styling the plots using 'kwargs'
fct_grd_5 = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kw_rgs = dict(s=50, linewidth=0.5, edgecolor='black')
fct_grd_5.map(plt.scatter, 'CriticRating', 'AudienceRating')

