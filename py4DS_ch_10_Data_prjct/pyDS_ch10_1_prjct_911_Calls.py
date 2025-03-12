
################# 10.1: in:169
# copy: py, ipynb
#        
#        
################# (11-Mar-25 for 12-Mar-25)

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

# Convert to datetime (since the column contains string timestamps)
    # Use pd.to_datetime to convert the column from strings to DateTime objects.
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# re-check
df['timeStamp'].dtype
type(df["timeStamp"].iloc[0])


# since the "timeStamp" column is now in DateTime format, individual components like hour, month, and day of the week 
    # can be extracted using their respective attributes (hour, month, dayofweek).

            # time = df['timeStamp'].iloc[0]
            # time.hour

    # There are various attributes we can call. 

# Now we'll use ".apply()" to create 3 new columns called 'Hour', 'Month', and 'Day of Week' based off of the timeStamp column
    # Each row's timeStamp value is passed to the lambda function, 
    # which extracts the relevant attribute and assigns it to the corresponding new column.
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)


# use .map() with following dictionary to map the actual string names to the day of the week
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# visualization for "Day of Week"
# use seaborn to create a "countplot" of the "Day of Week" column with the "Reason" column based "hue"
sns.countplot(data=df, x='Day of Week', hue='Reason', palette='viridis')
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# visualization for "Month"
sns.countplot(data=df, x='Month', hue='Reason', palette='viridis')
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)



# ----  more visualaization  ----

