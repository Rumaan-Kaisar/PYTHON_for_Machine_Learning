
################# 10.1: rev vid
# copy: py, ipynb
#        
#        
################# (18-Mar-25 for 19-Mar-25)

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


# --------    fill missing info    --------
# notice something strange about above Plot: some missing months
    # Some months are missing, so a different approach is needed to visualize the data. 
    # A line plot can help fill in the gaps, but first, the data must be prepared.

# Create a groupby object called byMonth, grouping by the "Month" column and using count() to aggregate. 
    # Then, display the first few rows with head().

byMonth = df.groupby('Month')
counted = byMonth.count()     # looks at "Month" and give us the "count"
counted.head()  # prints all counted entries for each column (per group of months)
byMonth.head(1) # prints 1 row from each group of months (gruped by month)


# Now we'll create a simple plot using the dataframe indicating the count of calls per month
    # byMonth['title'] is a Pandas Series containing the count of calls per month.
    # .plot() is the "Pandas built-in method" that simplifies plotting without explicitly calling Matplotlib functions.
    # figsize, marker, and linestyle are passed as parameters to customize the plot.
import matplotlib.pyplot as plt

# plots the number of calls per month using the title column as the count
# Could be any column
counted['title'].plot(figsize=(10, 5), marker='o', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Number of Calls')
plt.title('911 Calls Per Month')
plt.show()


# SEABORN: use seaborn's lmplot() to create a "linear fit" on the "number of calls per month". 
# reset the index: Keep in mind you may need to reset the index to a column.
import seaborn as sns  

# Reset index so "Month" becomes a column  
counted = counted.reset_index()  
# Plot using seaborn's lmplot
sns.lmplot(x='Month', y='title', data=counted)  




# ------------  more visualaization  ------------
# Create a new column called 'Date' that contains the date from the 'timeStamp' column. 
    # use apply() along with the .date()
    # extructing date "YYYY-MM-DD" from 'timeStamp' column
df['Date']=df['timeStamp'].apply(lambda t: t.date())
df.head(1)

# ----  plot how many calls per date  ----
# how many calls per date
calls_per_day = df.groupby('Date').count()
calls_per_day.head(1)
# plot how many calls per date
calls_per_day['title'].plot(figsize=(10, 5), marker='o', markersize=1.5, linestyle='-', markerfacecolor='red', markeredgecolor='red')


# ----  plot how many calls per date for specific reasons like: Traffic, Fire or EMS  ----

callPerDay_Traffic = df[df['Reason']=='Traffic'].groupby('Date').count()
callPerDay_Fire = df[df['Reason']=='Fire'].groupby('Date').count()
callPerDay_EMS = df[df['Reason']=='EMS'].groupby('Date').count()

import matplotlib.pyplot as plt

# Plot each call type with different colors
plt.figure(figsize=(18,6))

plt.plot(callPerDay_Traffic['title'], label='Traffic', color='red')
plt.plot(callPerDay_Fire['title'], label='Fire', color='blue')
plt.plot(callPerDay_EMS['title'], label='EMS', color='green')

# Add title and labels
plt.title("911 Calls Per Day by Reason")
plt.xlabel("Date")
plt.ylabel("Number of Calls")

# Add legend
plt.legend()

# Show the plot
plt.show()



# ----  HeatMaps  ----
# To create heatmaps with seaborn and our data, We'll first need to restructure the dataframe 
    # so that the "columns" become the "Hours" and the "Index" becomes the "Day of the Week". 
    # try to combine "groupby" with an "unstack"

# Convert to datetime
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# use ".apply()" to create 3 new columns called 'Hour', 'Month', and 'Day of Week'
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)
# use .map() with following dictionary to map the actual string names to the day of the week
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

# ----  'Hour'  ----
# Group by 'Day of Week' and 'Hour' and count occurrences
group_day_hour = df.groupby(['Day of Week', 'Hour'])
print(group_day_hour.head(1))

heatmap_data = group_day_hour.count()['title'].unstack()
# Display the transformed DataFrame
print(heatmap_data)


# in one line
heatmap_data = df.groupby(['Day of Week', 'Hour']).count()['title'].unstack()

# If the output is still not fully visible, you can try increasing the width of the display:
pd.set_option('display.width', 1000)  # Adjust width (increase if needed)

# HeatMap
plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data, cmap='viridis')

# clustermap
sns.clustermap(heatmap_data, cmap="viridis")



# ----  Month  ----
# same plots and operations, for a DataFrame using "Month" as the column.
heatmap_data_month = df.groupby(['Day of Week', 'Month']).count()['title'].unstack()
# Display the transformed DataFrame
print(heatmap_data_month)

# HeatMap
plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data_month, cmap='viridis')

# clustermap
sns.clustermap(heatmap_data_month, cmap="viridis")

