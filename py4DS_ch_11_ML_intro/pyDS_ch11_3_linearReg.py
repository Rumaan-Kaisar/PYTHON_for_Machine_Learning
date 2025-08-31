
################# 15.1-15.5: done, 15.6: interpretation edit (coefficients in ipynb, all in py)
# copy: no ipynb for now, 2x py only
#       
#   
#
################# (29-Aug-25 for 30-Aug-25)

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
    # Use jointplot to create a 2D hex bin plot comparing "Time on App" and "Length of Membership".


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



# ----  jointplot 2  ----

# More time on app, more money spent.
fig1 = sns.jointplot(
    data=customers,
    x="Time on App",
    y="Yearly Amount Spent",
    kind="scatter",
    height=6,
    color="#ffa98f",
    edgecolor="#e52b52",
    s=12,
    marginal_kws=dict(
        bins=20, 
        fill=True, 
        color="#ee4466",      # histogram fill color
        edgecolor="white", 
        alpha=0.5,
        kde = True,             # enable KDE
        line_kws=dict(linewidth=2)  # KDE curve width
    )
).set_axis_labels("Time on App", "Yearly Amount Spent")

fig1.ax_joint.grid(True, linestyle="--", alpha=0.5)

# error occurs using "kde_kws=dict(linewidth=2)" because the KDE plotting function 
    # in Seaborn does not accept a color argument through kde_kws when used alongside histplot via jointplot. 
    # Seaborn specifically uses line_kws instead for styling the KDE curve.

# correlation:
    # Customers who spend more time on the 'App' tend to spend more money.  
    # Most customers spend around "12 minutes" on the 'App' and spend around $400-$600.



# ----  jointplot 3  ----

# Hex Bin: More time on app, longer membership
fig1 = sns.jointplot(
    data=customers,
    x="Time on App",
    y="Length of Membership",
    kind="hex",
    height=6,
    color="#1abcde",
    edgecolor="#f9f9f9",
    marginal_kws=dict(
        bins=20, 
        fill=True, 
        # color="#ee4466",      # histogram fill color
        edgecolor="white", 
        alpha=0.5,
        kde = True,             # enable KDE
        line_kws=dict(linewidth=2)  # KDE curve color
    )
).set_axis_labels("Time on App", "Length of Membership")

fig1.ax_joint.grid(True, linestyle="--", alpha=0.5)


# correlation
    # Customers who spend more time on the "App" tend to be long-time members.
    # Most customers spend about "12 minutes" on the "App" and have been members for around **2 to 5 years**."


# ----  pairplot  ----
# sns.pairplot(df, height=2, aspect=1.3)

# save as image, then load it in "markdown cell"
plot = sns.pairplot(customers, height=2, aspect=1.3)
plot.savefig("./ch11_img/ecommerce_pairplot.png", dpi=50)
plt.close() # prevents the plot from displaying and embedding

# attach in markdown:   ![Alt Text](./ch11_img/ecommerce_pairplot.png)

# observation: 
    # Based on above plot what are the most correlated feature with "Yearly Amount Spent"?
    # ans: "Length of Membership"


# ----  lmplot  ----
# Make a sns.lmplot (linear model plot) of  "Yearly Amount Spent" vs. "Length of Membership". 
sns.set_style('whitegrid')

sns.lmplot(
    x='Length of Membership', 
    y='Yearly Amount Spent', 
    data=customers, 
    scatter_kws=dict(
        color="#89cff0", 
        edgecolor="#2978c7", 
        s=12
    )
)


# ----------------    Training and Testing a Model    ----------------

# ----  Feature & Target  ----
# Feature and Target:
    # Extract features 'X' and target 'y' from the data
    # select feature columns
customers.columns

# 'Email', 'Address', 'Avatar' are just info, so we avoid these
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]

# we make 'Yearly Amount Spent' as target
y = customers['Yearly Amount Spent']



# ----  split  ----
# Split the data into "train" and "test"
    # Use train_test_split() from sklearn.model_selection.
    # Pass X (features) and y (target) as inputs.
    # Set test_size
        # Defines what fraction of data goes to testing.
        # Common values: 0.3 (30%) or 0.4 (40%).
    # Set random_state for reproduce the result (like random_state=101).
    # store output:
        # X_train, X_test: features for training and testing. 
        # y_train, y_test: labels for training and testing.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)



# ----  model train  ----
# Create and Fit Model
    # Import and instantiate the LinearRegression model.
        # Import the Model Class: import LinearRegression from sklearn.linear_model
        # Create the Model Instance: Instantiate an object of LinearRegression().
    
    # Train it using model.fit(X_train, ytrain).
        # train the model By calling the .fit() over the object
        # use X_train (features) and y_train (target values) as arguments.
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)    # notice the output -> it has been trained



# ----  model iterpretation  ----
# Make Predictions
    # Use the trained model to predict on the test set with model.predict(X_test).

# coefficient
    # Each feature has a coefficient, interpret those coefficient (lm.coef_)
    # Create a DataFrame from the coefficients for Clarity
    # Uses lm. coef_ as data
    # Uses X.columns as the index (feature names)
    # Match Coefficients to Feature Names

# Intercept
    # get the intercept value of the regression line (lm.intercept_)

print(lm.intercept_)
lm.coef_
X_train.columns

# Examin the coefficint on x_train
import pandas as pd
cdf = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
print(cdf)


# iterpretation of coefficinet
""" 
    Model Setup:
        We trained a linear regression model to predict Yearly Amount Spent based on:
            Avg. Session Length
            Time on App
            Time on Website
            Length of Membership

        The fitted model is:

        Yearly Amount Spent = —1045.12 + 25.69*(Session Length) + 37.89*(Time on App) + 
                                0.56*(Time on Website) + 61.65*(Membership Length)
    
        Notice the use of "Intercept" and "coefficients" in above equation.
        

    Intercept:
        -1045.12
        This is the baseline prediction when all features are 0.
        Since "0 minutes" and "0 years of membership" are unrealistic, 
        the intercept doesn't have a strong practical meaning here. 
        It mainly adjusts the regression line to fit the data correctly.

        Coefficients:
            Each coefficient shows how much the Yearly Amount Spent changes if 
            that feature increases by 1 unit, holding the others constant.

            Avg. Session Length (25.69)
                For each extra unit (minute) in session length, yearly spending increases by about $25.69.
                Suggests in-store style advice sessions are "positively correlated" with spending.

            Time on App (37.89)
                Each extra minute on the App leads to about $37.89 more in yearly spending.
                Strongest impact per unit -> the App experience drives sales significantly.

            Time on Website (0.56)
                Each additional minute on the website adds only $0.56 in yearly spending.
                Weak effect -> website engagement is "less linked" to spending.

            Length of Membership (61.65)
                Each extra year as a member adds about $61.65 to yearly spending.
                Long-term customers are consistently more valuable.


    Summary:
        The "App" and "Membership length" are the strongest predictors of higher yearly spending.
        The Website contributes very little, suggesting the company should 
            focus more on improving the App experience than the website.

        Spending increases the most with "Length of Membership", making it the most important feature.
        The second most important feature is "Time on App", which also has a strong effect.
        The third most important feature is "Average Session Length".
        Time on Website has very little impact and seems the least important.


    Note:
        It seems like  "Membership length" has bigger implact that "Time on App" 
        But its not the case, because "Membership length" measured in Year and "Time on App" measured in minutes
        so the units are different, and actually making "Time on App" is the strongest and "Average Session Length" is second most impactful

        So technically Time on App has a larger coefficient (37.89) than Membership (61.65 per year)

        Membership increases in years, while "Time on App" increases in minutes.
            
"""



# ----  model evaluation  ----
# Evaluate Performance using following:

# Get Predictions: lm.predict(X_test)
predictions = lm.predict(X_test)
print(predictions)


# comparison: ompare predictions with y_test
    # Visual Evaluation: Scatter Plot of the comparison
    # How far the predictions from the actual prices
y_test  # these are the actual prices

# Create the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, color="#89cff0", edgecolors='#318ce7', s=10, alpha=0.8)


# Analyzing Residuals
    # create a histogram of the distribution of residuals
    # Residuals = Actual - Predicted
sns.histplot(y_test - predictions, kde=True, shrink=0.95, edgecolor='white', color="#1abcdf", bins=50)

# Evaluation Metrics
    # Mean Absolute Error (MAE)
    # Mean Squared Error (MSE)
    # Root Mean Squared Error (RMSE)


