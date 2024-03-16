
################# 6.14: full, 6.15: full, 7.7: 2.29
# copy: dataset, pevious_chart, fill_in_blank.py [done]
#        
#        
################# (13-mar-24 for 15-mar-24)

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
            Bueno Vista Studios
            Use: Sony, Universal, WB, Paramount Pictures, Fox

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

# Statistical info. Summary of the dataframe
movies.describe()
# mean, variance, max, min, 25%(1st quartel), 50%(median), 75%(3rd quartel)

# Get structure of the dataframe, information,
movies.info()





# Type convertions
# -=-=-=-  To numerical data  -=-=-=-

# -=-=-=-  To categorical data  -=-=-=-





# rename the column names to single-string names
# movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
# movies.head()    # view dataset


# ----   convert 'numerical-type',' object-type' to "categorical-type"   ----
# movies.Film = movies.Film.astype("category") # use assignment '=' to update the dataset
# movies.Genre = movies.Genre.astype("category")   
# movies.Year = movies.Year.astype("category")   
# movies.info()   # check the data-type changes




# fill in the blanks

# Explore the categorical variable 'Studio', used in the assignment
mov.Studio._()


# Explore the categorical variable Genre, used in the assignment
mov.Genre._()


# Filter the dataframe by genre
mov2 = mov[(mov._ == 'action') | (mov._ == 'adventure') | (mov._ == 'animation') | (mov._ == 'comedy') | (mov._ == 'drama')]


# Filter the dataframe by studio
mov3 = mov2[(mov2._ == 'Buena Vista Studios') | (mov2._ == 'Fox') | (mov2._ == 'Paramount Pictures') | (mov2._ == 'Sony') | (mov2._ == 'Universal') | (mov2._ == 'WB')]

# Check how the filters worked
print (_.Genre.unique())
print (_.Studio.unique())
print (len(_))



# Define the style
_.set(style="darkgrid", palette="muted", color_codes=True)

# Plot the boxsplots
ax = sns._(data=_, x='_', y='_', orient='v', color='lightgray', showfliers=False)
plt.setp(ax.artists, alpha=0.5)

# Add in points to show each observation
_.stripplot(x='_', y='_', data=_, jitter=True, size=6, linewidth=0, hue = 'Studio', alpha=0.7)

ax.axes.set_title('_',fontsize=30)
ax.set_xlabel('_',fontsize=20)
ax.set_ylabel('_',fontsize=20)

# Define where to place the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
