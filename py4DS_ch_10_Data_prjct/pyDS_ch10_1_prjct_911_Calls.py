
################# 10.1:
# copy: py, ipynb
#        
#        
################# (07-Mar-25 for 08-Mar-25)

# Courses: PrTla PY for DS & ML >    10.1, 10.2, 10.3, 10.4


# ----------------    project: Emergency - 911 Calls    ----------------

# For this project, we'll analyze 911 call data from Kaggle (https://www.kaggle.com/mchirico/montcoalert)
# Since the dataset is large, we'll use a smaller version from any GitHub repo with similar data. 

# --------  About dataset:  --------
    # The dataset includes the following fields:
        # lat : String variable, Latitude
        # lng: String variable, Longitude
        # desc: String variable, Description of the Emergency Call
        # zip: String variable, Zipcode
        # title: String variable, Title
        # timeStamp: String variable, YYYY-MM-DD HH:MM:SS
        # twp: String variable, Township
        # addr: String variable, Address
        # e: String variable, Dummy variable (always 1)


# ----  Getting basic info from the dataset  ----

# import libraries
import numpy as np
import pandas as pd

# We'll use following visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# Read in the csv file and as a dataframe
df = pd.read_csv("./data_call_911_small.csv")

# data info
df.info()

# inspect first 5 row
df.head(5)

# top 5 most appeared zip codes
df["zip"].value_counts().head(5)

# top 5 townships (twp) for 911 calls?
df["twp"].value_counts().head(5)

# how many unique title codes are in the 'title' column?
df['title'].unique.value_counts()

# how many unique title codes are in the 'title' column?
# df['title'].unique # gets the uniques
df['title'].nunique()



# ----  Creating new features  ----

# ----  apply() with "LAMBDA expression"  ----
# Extract the department (EMS, Fire, or Traffic) from the title column using 
    # .apply() with a lambda function and store it in a new column called Reason.
    # Example: If title is "EMS: BACK PAINS/INJURY", then Reason will be "EMS".
df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])

# What is the common Reasons for a 911 call (use new column)?
df["Reason"].value_counts()

#  use seaborn to create a countplot of 911 calls by Reason.
sns.countplot(x='Reason', data=df, palette='magma')




# ----  time information  ----
# lets focus on time information. 
df["timeStamp"].dtypes  # Check the column's data type

# data type of the objects in the timeStamp column
type(df["timeStamp"].iloc[0])   # Check the type of individual elements


# rev[08-Mar-2025]

# Convert to datetime (since the column contains string timestamps)
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['timeStamp'].dtype
type(df["timeStamp"].iloc[0])


# ----  more visualaization  ----

