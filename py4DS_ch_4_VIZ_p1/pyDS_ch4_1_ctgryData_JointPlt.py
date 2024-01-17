
################# 6.1: 3:30
# copy:  Dataset, Update: py, ipynb
#        
#        
################# (16-jan-24 for 17-jan-24)

# Courses: A-Z PY for Data-Science    6.1, 6.2


# ------------    Categorical variables    ------------
# most of the time some 'categorical data' will appear in your Dataset
    # you need to know how to deal with 'catgrical data'
    # you have to deal with both 'catgrical data' and 'numerical data' simultaniusly


# import libraries & Dataset
import pandas as pd

# import os
# os.getcwd()     # get current working directory

movies = pd.read_csv("./MovieRatings.csv")

# check length of the dataset
len(movies)

# Explore the dataset
    # checking the datsset is a good habit 
    # however we can't fully explore if the dataset is too big and lots of columns
        # we can't see all the columns for example, if there is 1000 columns
movies.head()
movies.columns  # get column info

# RENAME the columns so that we can use '.' operator
    # notice "Rotten Tomatoes Ratings %" is actually a 'Critic Rating'
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.head()



# -=-=-=-  categorical data  -=-=-=-
# which data should we treat as category?
    # 'Year' is a numerical data, but we should treat it as 'category'. Why?
    # lets do more exploration to understand the reason - 


