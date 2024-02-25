
################# 6.11: 11.12
# copy:  
#        
#        
################# (24-feb-24 for 25-feb-24)

# Courses: A-Z PY for Data-Science    6.11, 6.12, 6.13


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




# ------------    Dashboard    ------------
# What is a dashboard?
    # a dasboard is a combination of charts
    # for example sub-plot we built previously is a king of dashboard
    # because it combines two types of plot with different informations

# In this section we'll use "subplot" to create a 'Dashboard'
    # we'll populate those dashboard with different types of chart
    # we'll use a 2x2 subplot

# We'll include our dashboard:
    # kdeplot
    # violinplot
    # colored kdeplot

sns.set_style('darkgrid')   # change style
dshBd, axes = plt.subplots(2, 2, figsize = (15, 15))    # 2x2 subplot
# Note: we don't use 'sharex', 'sharey' at the first try, 
    # because we need to view all different plots first
# dshBd, axes = plt.subplots(2, 2, figsize = (15, 15), sharex=True, sharey=True)
    # used 'sharex', 'sharey' attributes to set all same 'xlim & ylim'

# kdeplot: 
    # BudgetMillions' vs 'AudienceRating'
    # BudgetMillions' vs 'CriticRating'
    # notice 2D indexes used

k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes[0, 0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes[0, 1])
k_BA.set(xlim=(-40, 250))   # setting the RANGE for k_BA
k_BC.set(xlim=(-40, 250))   # setting the RANGE for k_BC
# We use k_BC "k_BC.set(xlim=(-20, 160))" but it can be done with 'subplots' attribute "sharex"
    # the reason is: we have different kind of plots (we don't know how they look), 
    # so we do it manually


# violinplot: we put violinplot at (1, 0)
vlp_1 = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre', ax=axes[1, 0])


# kdeplot (shaded): CriticRating vs AudienceRating at (1, 1) i.e. ax=axes[1, 1]
    # combine 'shades' & 'border'  to get a overlaied plot
    # notice we also used ax=axes[1, 1] for the outlines 'kDe2'
    # we put two plots in one plotting space (overlaying)
# if we dont specify the axes, the plots will be added to the last subplot
kDe1 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds', ax=axes[1, 1])
kDe2 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds', ax=axes[1, 1]) # ads border on top of 'kDe5'
# kDe2 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds', ax=axes[0, 0]) # different axes

# So it's so simple to add charts to a 'Dashboard'




# ------------    Non-Seaborn plot    ------------
# how do we add a 'non-seaborn' plot into our diagram?
    # above we'll used ony sns (seaborn) plots
# How do we add a plt (pyplot) chart, EG: 'Histogram', to visualize distribution?

# ERR: we can not use 'sns' syntax to add a 'plt.hist' for example in the 4th digram of our dashboard
hs_1 = plt.hist(movies.CriticRating, rwidth=.8, ax=axes[1, 1])
# rwidth=.8 gaps between bars

# we must use following 'pyplot' syntax: The procedure is bit diffeent
    # actually we use now the "standared approach", above we used a 'seaboarn way'

# standared approach: since 'dshBd, axes = plt.subplots()' is pyplot entity
    # we use 'axes[i, j].hist()' instead of "plt.hist()"
    # because each axes[i, j] itself is a 'pyplot-object'
axes[1, 1].hist(movies.CriticRating, rwidth=.8)    



# Following dashboard uses a histogram as 'non-seaboarn' plot
sns.set_style('darkgrid')   # change style
dshBd_2, axes_2 = plt.subplots(2, 2, figsize = (15, 15))    # 2x2 subplot

# kdeplot:
k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes_2[0, 0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes_2[0, 1])
k_BA.set(xlim=(-40, 250))   # setting the RANGE for k_BA
k_BC.set(xlim=(-40, 250))   # setting the RANGE for k_BC

# violinplot: we put violinplot at (1, 0)
vlp_1 = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre', ax=axes_2[1, 0])

# Histogram
axes_2[1, 1].hist(movies.CriticRating, rwidth=.8) 
plt.show() 


