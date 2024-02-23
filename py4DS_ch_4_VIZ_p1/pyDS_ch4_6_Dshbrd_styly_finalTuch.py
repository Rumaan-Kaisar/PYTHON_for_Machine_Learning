
################# 6.11: 3.40
# copy:  
#        
#        
################# (21-feb-24 for 23-feb-24)

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
k_BA.set(xlim=(-20, 160))   # setting the RANGE for k_BA
k_BC.set(xlim=(-20, 160))   # setting the RANGE for k_BC
# We use k_BC "k_BC.set(xlim=(-20, 160))" but it can be done with 'subplots' attribute "sharex"
    # the reason is: we have different kind of plots, so we do it manually



# ----  rev[21-2-24]  ----
# kdeplot (shaded): CriticRating vs AudienceRating
    # combine 'shades' & 'border'  to get a overlaied plot
kDe1 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds')
kDe2 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds') # ads border on top of 'kDe5'




# violinplot:
vlp_1 = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre')




""" 
# issue 1, label: sharex, sharey hides 'label'
axes[1].yaxis.get_label().set_visible(True)

# issue 2, ticks: also you can use following workaround to show ticks (numbers)
axes[i,j].xaxis.set_tick_params(which='both', labelbottom=True)
axes[i,j].yaxis.set_tick_params(which='both', labelleft=True)

"""
# use for loop to fix issue 1 & issue 2
for i in range(0,2):
    for j in range(0,2):
        # show labels
        axes[i,j].yaxis.get_label().set_visible(True)
        axes[i,j].xaxis.get_label().set_visible(True)
        # show ticks
        axes[i,j].xaxis.set_tick_params(which='both', labelbottom=True)
        axes[i,j].yaxis.set_tick_params(which='both', labelleft=True)

