
################# 6.14: full, 6.15: full, 7.7: full, 7.8: 4.00
# copy: dataset, pevious_chart, fill_in_blank.py [done]
#        
#        
################# (23-mar-24 for 24-mar-24)

# Courses: A-Z PY for Data-Science    6.14, 6.15, 7.7, 7.8, 7.9




# ------------    SECTION RECAP    ------------
""" 
    In this section we learned:

        1.	Category data type in Python
                * seperate 'numerical' data from 'categorical' data
                * e.g. "Years" are categorical data (even though they are numbers)
                * we converted "Years" numeric to categorical
            
        2.	JointPlots
                * Hex type of jointplot, kind='hex', 'Hexagonal' clustered presentation

        3.	Histograms

        4.	Stacked Histograms
                * used python to plot using 'pyplot'

        5.	KDE Plot
                * we mostly used

        6.	Using the Subplots() function
                * layout/figure containing multiple plots

        7.	Violinplots
                * comparison between 'Violinplots' & 'Boxplot'

        8.	Creating a Facet Grid
                * observe evolution of a dataset in a plot

        9.	Coordinates and Diagonals
                * setting facet-grids axix & draw diagonal for comparison

        10.	Building Dashboards
                * using 'subplots' with 'seaborn'
                * overlaying plots on top of other

        11.	Styling Tips
                * background, seaborn styles

        12.	Finishing Touches
                * Thematic changes, title, axis-lables, font-sizes, tick-font-size, legend size

"""




# ------------    Movie % Domestic Gross (HOMEWORK)    ------------
""" 
    The movie reviews website was very happy with your deliverable for the previous assignment (visualizations in this section, e.g. dashboard).
    
    Now they have a new request for you:
        The previous consultant had created a chart for them which is illustrated on the given image. 
        However the 'Python code' used to create the diagram has since been lost and cannot be recovered (LOL). 

    1. Your task is to come up with the code that will  re-create the same chart making it look as close as possible to the original.

    2. Also A new dataset has been supplied.



    --------    Dataset    --------
    Dataset: Following parameters are important for analysis.
        There are 608 data/entries

        Day of the week: the day movie was launched.
        Director
        Genre: action, comedy etc.
        Movie Title
        Relese date
        Studio

        Gross in milin dollers
        Adjusted gross: Because some Movies relesed in the previous years
                        Adjusted for the inflations
        Budget in milin dollers

        IMDB rating
        movieLens rating

        Oveseas gross: Earnings outside the US; 
        overseas %: for comparison with total gross
        Profit: million dollers (from budget and the gross)
        Profit %
        Runtime: length of the movie
        US gross & US gross %



    --------    Previous plot    --------
    It's a Boxplot
    X-axis: Genre
    Y-axis: Gross % in US (last column in our dtaset)
        action avg 40% gross
        comedy avg 50%
    
    Studios as 'hue/group' and colored legends
        represented dots by the columns



    --------    Hints/Clues    --------
    Hint 1: 
        Filter the dataset using '6 studios' from the given plot
            eg. 'TriStar' is not in the plot            
            Use: Bueno Vista Studios, Sony, Universal, WB, Paramount Pictures, Fox

        Filter the 'Genre' also, use 5-generes present in the plot
            eg. 'Biography' is not in the plot
            Use: action, comedy, adventure, animation, drama
                

    Hint 2: 
        Use the 'fill_in_blank' file
            Import library/packages
            Load data
            Explore the data
            Filter the data-set
            Make the plot

"""



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
movies = pd.read_csv("./Section6-Homework-Dataset.csv", encoding = 'latin1')




# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    Explore the data    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Visualize the dataframe, get Row, column numbers
movies
# 608 rows × 18 columns

movies.head(5)  # first 5 rows

movies.columns  # get column info

# Statistical info. Summary of the DATAFRAME
movies.describe()
    # mean, variance, max, min, 25%(1st quartel), 50%(median), 75%(3rd quartel)
    # "Gross % US" is in between 0 and 100%.

# Get structure of the dataframe, Data-type information.
movies.info()


# We'll use following variables from given dataset
        # Genere
        # Studio
        # Gross % in US




# --------    Vizualization 1 : Grouping the informations    --------
    # Day of week for a movie Relese
    # Notice most of the movies relesed on 'Friday' and 'Wednesday'
        # None of the movies relesed on 'Monday'
vis1 = sns.factorplot(data=movies, x='Day of Week', kind='count', size=10)
# factorplot has been changed to catplot. sns.factorplot > sns.catplot
    # Replace the above code with the following
vis1 = sns.catplot(data=movies, x='Day of Week', kind='count', height=10)

# sns.catplot(data=auto, x="fuel-type", y="horsepower", hue="num-of-doors", kind = 'point')

# chatGPT:
    # In Seaborn, the 'size' parameter in factorplot (deprecated since Seaborn version 0.11.0) was used to specify the 'height of the figure' in inches. 
    # It was essentially replaced by the 'height' parameter. 


# Type convertions
# -=-=-=-  To numerical data  -=-=-=-

# -=-=-=-  To categorical data  -=-=-=-
movies['Day of Week'] = movies['Day of Week'].astype("category")    # movies.'Day of Week' won't work. Need to rename
movies.Studio = movies.Studio.astype("category") # use assignment '=' to update the dataset
movies.Genre = movies.Genre.astype("category")   


# All studios: Explore the categorical variable 'Studio', used in this project
    # get all the categories i.e. studios
movies.Studio.unique()
# There are 36 different studios in this dataset
len(movies.Studio.unique())

# All Genres: Explore the categorical variable Genre, used in this project
movies.Genre.unique()
# There are 15 different Generes in this dataset




# ------------    Filter the dataframe by genre & studio    ------------
# Since we need only 5 genres and 6 studios:
    # studios: 
        # Bueno Vista Studios, 
        # Sony, 
        # Universal, 
        # WB, 
        # Paramount Pictures, 
        # Fox
    # genres: 
        # action, 
        # comedy, 
        # adventure, 
        # animation, 
        # drama

# Boolian values. only True-False
movies.Studio == 'Buena Vista Studios'
movies.Genre == 'action'

# Filter with these Boolian Values
movies[(movies.Genre == 'action')]  # 236 action movies
movies[movies.Studio == 'Buena Vista Studios']  # 93 movies by Buena Vista Studios

# ----    "NESTED FILTER"    ----
# Nested filtering: 'Action' movies by Buena Vista Studios
mov1G = movies[movies.Genre == 'action']
mov1GS = mov1G[mov1G.Studio == 'Buena Vista Studios']
mov1GS.head(5)
len(mov1GS)     # 30 movies


# So we filter our dataset as Below
    # We'll do a "NESTED FILTER"
    # we'll use conditionala OR '|' for multiple Studios/Genres
        # First we extract movies for 5-genres 
        # Then we take the filtered moves and apply another filter for 6-studios

# Filter the dataframe by GENRE
mov_Gnr = movies[(movies.Genre == 'action') | (movies.Genre == 'adventure') | (movies.Genre == 'animation') | (movies.Genre == 'comedy') | (movies.Genre == 'drama')]

# Filter the dataframe by STUDIO
mov_Sdo_Gnr = mov_Gnr[(mov_Gnr.Studio == 'Buena Vista Studios') | (mov_Gnr.Studio == 'Fox') | (mov_Gnr.Studio == 'Paramount Pictures') | (mov_Gnr.Studio == 'Sony') | (mov_Gnr.Studio == 'Universal') | (mov_Gnr.Studio == 'WB')]

# Check how the filters worked
print(mov_Sdo_Gnr.Genre.unique())
print(mov_Sdo_Gnr.Studio.unique())
print(len(mov_Sdo_Gnr))   # 423


# ALTERNATIVE: more neat & clean way (dry)-- use 'isin()' over the data-frame
# Filter the dataframe by GENRE, using array of Generes
genre_filter = ['action', 'adventure', 'animation', 'comedy', 'drama']
mov_Gnr_2 = movies[movies.Genre.isin(genre_filter)]

# Filter the dataframe by STUDIO, using array of Studios
studio_filter = ['Buena Vista Studios', 'Fox', 'Paramount Pictures', 'Sony', 'Universal', 'WB']
mov_Sdo_Gnr_2 = mov_Gnr_2[mov_Gnr_2.Studio.isin(studio_filter)]

# Check how the filters worked
print(mov_Sdo_Gnr_2.Genre.unique())
print(mov_Sdo_Gnr_2.Studio.unique())
print(len(mov_Sdo_Gnr_2))   # 423 (out of 608)




# --------    Vizualization 2 : Recrearte the given Box-plot    --------
# First we'll create the boxplot
    # then we place the 'Jitter' (for the studios) over the boxplot

# Define the style
sns.set(style="darkgrid", palette="muted", color_codes=True)

# Plot the boxsplots
    # we use our filtered dataframe
    # x agis: Genre
    # y axis: Gross % US
bx = sns.boxplot(data=mov_Sdo_Gnr_2, x='Genre', y='Gross % US', orient='v', color='lightgray', showfliers=False)
plt.setp(bx.artists, alpha=0.5)     # For Transperancy 

# Jitter: Add in points to show each observation
    # we're using striplot
    # we use our filtered dataframe again, x agis: Genre, y axis: Gross % US
    # We used hue = 'Studio' for 6 different studios
sns.stripplot(x='Genre', y='Gross % US', data=mov_Sdo_Gnr_2, jitter=True, size=6, linewidth=0, hue = 'Studio', alpha=0.7)

# --------   rev[23-mar-24]   --------
# problems: 
    # Deep copy
    # seperate Studios from all others
    # seperate Genrers from all others

bx.axes.set_title('_',fontsize=30)
bx.set_xlabel('_',fontsize=20)
bx.set_ylabel('_',fontsize=20)

# Define where to place the legend
bx.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)



