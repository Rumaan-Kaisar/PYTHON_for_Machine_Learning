
################# 6.5: 2:50
# copy:  
#        
#        
################# (30-jan-24 for 31-jan-24)

# Courses: A-Z PY for Data-Science    6.5, 6.6


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



# ------------    KDE PLOT: Kernel Density Estimate plot    ------------

# How can we visualize 'audiance rating' vs 'critic rating'?
    # We can use 'scatter-plot'
    # We also can use 'lmplot'
vis1_sctr = sns.scatterplot(data=movies, x='CriticRating', y='AudienceRating')    

# lmplot: recall 'pyDS_ch2_8_HW_wrldTrnd.py'
plt.style.use("seaborn")    # background color
vis2_lm = sns.lmplot(data=movies, x='CriticRating', y='AudienceRating', fit_reg=False, hue='Genre', height=6, aspect=1, scatter_kws={'s': 10})

# What are other way to visualize, other than 'scatter-plot' or 'lmplot'
    # To get more plot: Seaborn Gallery

# KDE: Kernel Density Estimate




