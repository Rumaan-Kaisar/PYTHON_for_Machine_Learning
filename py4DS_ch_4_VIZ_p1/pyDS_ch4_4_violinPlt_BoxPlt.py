
# Courses: A-Z PY for Data-Science    6.7


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




# ----------------    violinplots vs boxplots    ----------------
# we'll plot 'violinplots' and 'boxplots'
    # we'll compare which one is better & which one people often use

# boxplot & boxenplot
bxp_1 = sns.boxplot(data=movies, x='Genre', y='CriticRating', hue='Genre')  # box-plot
# following gives n-box plot, 'outliers' are shown as 'circles'
bxp_n = sns.boxenplot(data=movies, x='Genre', y='CriticRating', hue='Genre') 

# violinplot
vlp_1 = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre')

# violinplots vs boxplots
    # notice at the bottom we have all 'Genre' as x-label
    # The both plot shows us how the 'CriticRating' distributes across different 'Genre'
    # boxplot:
        # shows the quartiles, 
            # Q1: bottom of the box
            # Q2 or median: horizontal line middle of the box
            # Q3: Top of the box
            # outliers are excluded (not shown)
        # Observations: 
            # for example: the Horror movies, critic ratings are lower than others, 
                # it has median at 22, lowest of all 'Genre'
                # the highest median has 'Thriller' and gets best critic-ratings
                # 'Comedy' and 'Drama' has similar boxplot (but violinplot of those 2 are different)
                # 'Comedy' is little lower than 'Drama'
            
            # for a rough insight: if we want to create an average type of movie
                # it will be best to crate 'Thriller' than a 'Horror'

            # You'll get more insights if we comapre two 'Genre' side by side:
            # For example 'Action' vs 'Comedy', 
                # the "median" is almost the same
                # but 'Comedy' has more streached distribution than 'Action'


    # violinplot
        # The violinplot tells us prettyy-much the same thing, but in different characteristics
        # It has "Width" tells us number of points falling in that certain-area, 
            # where the boxplot onlyy shows the 'quartiles' and four quarters of the data
        # for eaxmple in 'Action' we have 2-wide areas and in 'Comedy' we have 3-wide areas
        # we can't get those from a boxplot
        # so violinplot shows us the concentration of points

        # in other words, 'violinplot' gives ud bit more info than 'boxplot'
            # cosider following example


# observations for criticrating of 'Drama' (subset of above dataset) for different 'years' (instead of Genre)
    # movies[movies.Genre=='Drama'] filters the data only for 'Drama'
    # now we compare the 'boxplot' and 'violinplot' for this specific data

# box-plot for 'CriticRating' in different 'Year' for 'Drama'
bxp_2 = sns.boxplot(data=movies[movies.Genre=='Drama'], x='Year', y='CriticRating', hue='Year')
sns.move_legend(bxp_2, "upper right", bbox_to_anchor=(1.2, .45))    # move legends
# violinplot for 'CriticRating' in different 'Year' for 'Drama'
vlp_2 = sns.violinplot(data=movies[movies.Genre=='Drama'], x='Year', y='CriticRating', hue='Year')
sns.move_legend(vlp_2, "upper right", bbox_to_anchor=(1.2, .45))    # move legends

# Observations
    # notice the years 2008 and 2011
    # they look similar in 'boxplot', though '2008' has more streached boxplot than '2011', 
    # but in 'violinplot' they look very different
    # '2008' has smooth violinplot than '2011'
    # '2008' has one wide area, '2011' has two wide area, 
    # i.e '2011' has two 'concentration of points' in two specific 'CriticRating' and '2008' has only one
    # in boxplot we dont have these, it doesnot move the median toward the 'concentration of points'

    # when you analyze your own dataset you'll get more insight on 'violinplot' than boxplot
    # however boxplot is more popular among 'executives'
        # theyy don't like the wierd shape of 'violinplot'

""" 
    ------------------------    QUARTILES    ------------------------
    What are Quartiles?
        Quartiles are three values that 'split' your dataset into 'quarters'.

    A MEDIAN divides a given dataset (which is already sorted) into two equal halves 
        similarly, the QUARTILES are used to divide a given dataset into 'four equal halves'. 
        Therefore, logically there should be 'three quartiles' for a given distribution, 
        however, the second_quartile = median 

    These values are the following:
        Q1 First quartile: 25% of the data are below this value.
        Q2 Second quartile / Median: This value splits the data in half.
        Q3 Third quartile: 25% of the data are above this value.

    Quartiles also correspond to 'percentiles': 
        Q1 is the 25th percentile, 
        Q2 is the 50th, and 
        Q3 is the 75th.

    How to Find Quartiles:
        The simple method for finding quartiles is to list the values in your dataset in numeric order. 
        Then find the 'three values' that split your data into quarters, as shown below.

            11
            13
            16
            19
            20   # Q1
            21
            23
            25
            26
            29   # Q2 or Median
            33
            34
            36
            38
            39   # Q3
            46
            52
            55
            58

 """

