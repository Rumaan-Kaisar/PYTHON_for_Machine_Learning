
################# 15.1-15.5: doene, 15.6: 282 (next 2 joint plots)
# copy: 
#       
#   
#
################# (15-Aug-25 for 16-Aug-25)

# Courses: PrTla PY for DS & ML >  15.1 (ipynb), 15.3, 15.4, 15.5, 15.6  >>  details in ipynb


""" 
    Project 1:
        Now we'll use scikit-learn in Python to create a linear regression model using "Housing price data".

"""


# Example 1: Predicting house price

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


# read data
df = pd.read_csv('data_USAhousing.csv')
df.head()


# ----  check info  ----
df.info()
df.describe()
df.columns


# ----  basic visulaization and analysis  ----
# sns.pairplot(df, height=2, aspect=1.3)

# save as image, then load it in "markdown cell"
plot = sns.pairplot(df, height=2, aspect=1.3)
plot.savefig("./ch11_img/house_pairplot.png", dpi=50)
plt.close() # prevents the plot from displaying and embedding


# ----  histogram  ----
sns.histplot(df['Price'], kde=True, shrink=0.95, edgecolor='white', color="#23aae3")

# Modern font settings
plt.rcParams["font.family"] = "DejaVu Sans"

# Title and axis labels
plt.title("House price distribution in $M", fontsize=15, color="#54626f", pad=15)
plt.xlabel("Price $M", fontsize=12, color="#87a96b")
plt.ylabel("Count", fontsize=12, color="#87a96b")

# Ticks and grid
plt.xticks(fontsize=10, color="#54626f")
plt.yticks(fontsize=10, color="#54626f")
plt.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.6, color="#72a0c1")

# Minimalist styling
for spine in plt.gca().spines.values():
    spine.set_visible(False)


# ----  Heatmap  ----
# numeric_only=True to avoid strings
dt_crr = df.corr(numeric_only=True)
dt_crr

sns.heatmap(dt_crr, cmap='rocket')
sns.heatmap(dt_crr, cmap='rocket', annot=True)


# ----------------    Model creation    ----------------
df.columns

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
lm = LinearRegression()
lm.fit(X_train, y_train)    # notice the output -> it has been trained


# ----  evaluating model performance  ----
print(lm.intercept_)
lm.coef_
X_train.columns
X.columns

# coefficent analysis
import pandas as pd
cdf = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
# lm.coef_ as data. 
# X.columns as index
# columns = ['Coeff'] names the column as 'Coeff'
print(cdf)

# ----  accuracy  ----
predictions = lm.predict(X_test)
print(predictions)     # these are the predicted prices
print(y_test)  # these are the actual prices

# Create the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, color="#89cff0", edgecolors='#318ce7', s=10, alpha=0.8)

# histogram for "residuals"
sns.histplot(y_test - predictions, kde=True, shrink=0.95, edgecolor='white', color="#1abcdf")


# ----  Evaluation matrix  ----
from sklearn import metrics
import numpy as np

# MAE
metrics.mean_absolute_error(y_test, predictions)

# MSE
metrics.mean_squared_error(y_test, predictions)

# RMSE
np.sqrt(metrics.mean_squared_error(y_test, predictions))


-------------------------------------

# NXT >> add codes from ipynb here




"""  
    --------  portfolio project exercise: Ecommerce analysis  --------

    Data file: data_Ecommerce_Customers. its a FAKE data.

    
    Background: 
        NYC e-commerce firm sells clothes online + offers in-store stylist help. 
        Users see stylist, then order via app or site. 
        
        Goal: choose whether to improve app or site. 
        Task: use data to decide.


    Steps: 
        Load libs & data -> EDA (Seaborn) -> answer pattern Qs 
        split train/test -> train linear regression 
        predict -> check metrics -> check residuals -> write conclusion.
"""

# import libraries
import numpy as np
import pandas as pd

# We'll use following visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# shows figures in ipynb
%matplotlib inline


# Get the Data
    # We will use the Ecommerce Customers file "data_Ecommerce_Customers" 
        # (no .csv extension, but still loadable with read_csv).

    # The dataset contains customer information such as 
        # Email, 
        # Address, and 
        # Avatar color.

    # It also includes numerical columns:
        # Avg. Session Length – minutes
        # Time spent on App – minutes
        # Time spent on Website – minutes
        # Time length of Membership – Number of years as a member.

# Read in the csv file and as a dataframe named customers.
customers = pd.read_csv("./data_Ecommerce_Customers")


# ----  check info  ----
# Check head() of customers, info() and describe()

customers.head()
customers.info()
customers.describe()
customers.columns


# ------------   EDA   ------------
# Exploratory Data Analysis
# Now we'll only use the numerical data of the csv file.

# jointplot
    # Use sns.jointplot to compare the "Time on Website" and "Yearly Amount Spent" columns. 
        # Does the correlation make sense?
    # Do the same but with the "Time on App" column instead.
    # Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.


# ----  jointplot 1  ----

sns.jointplot(data= customers, x=customers['Time on Website'], y=customers['Yearly Amount Spent'])


# with sns plotstyle
sns.set_palette("OrRd_d")
sns.set_style('whitegrid')

sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)


# with more style

fig1 = sns.jointplot(
    data=customers,
    x="Time on Website",
    y="Yearly Amount Spent",
    kind="scatter",
    height=6,
    color="#89cff0",
    edgecolor="#2978c7",
    s=12,
    marginal_kws=dict(bins=20, fill=True, color="#00c4b0", edgecolor="white", alpha=0.8)
).set_axis_labels("Time on Website", "Yearly Amount Spent")

fig1.ax_joint.grid(True, linestyle="--", alpha=0.5)


# correlation: More time on site, more money spent.
    # Customers who spend more time on the site tend to spend more money.
    # Most customers spend around 37 minutes on the site, with an average yearly spending of about $500.


# GPT: a clear, pointwise simplification with mid-ground details while preserving full context:



