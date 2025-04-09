
################# 10.6: in 81
# copy: new ipynb + py
#        
#        
################# (08-Apr-25 for 09-Apr-25)

# Courses: PrTla PY for DS & ML >    10.6, 10.7, 10.8, 10.9

# Download data: https://www.dropbox.com/s/s9uq4qvls4rghm7/all_banks?dl=0


# --------------------    Finance Data Project    --------------------
# This project is challenging as it introduces many new concepts. 
# You may need to research on your own, but guidance will be provided.


# ----  Get the Data  ----
# This section covers using pandas to read stock data from "Google Finance". 

# install:  First, "install pandas-datareader" (pip install pandas-datareader). 

# It allows fetching stock data directly from the internet. More details:  
    # GitHub: pandas-datareader (https://github.com/pydata/pandas-datareader)  
    # Pandas docs (http://pandas.pydata.org/pandas-docs/stable/remote_data.html)


# This project focuses on exploratory data analysis of "stock prices", 
    # specifically bank stocks, from the 2008 financial crisis to early 2016. 
    # The goal is to practice visualization and pandas skills, 
    # it is not meant to be a robust financial analysis or be taken as financial advice

# The 2008 financial crisis:
    # The 2008 financial crisis was a major global economic downturn triggered by subprime mortgages, 
    # excessive risk-taking by financial institutions, and regulatory failures. 
    # It led to a stock market crash and an international banking crisis, 
        # with Lehman Brothers' bankruptcy in September 2008 marking a key event. More details: 
    # Financial crisis (2007–08): https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308


# ----  Getting basic info from the dataset  ----

# import libraries
import numpy as np
import pandas as pd

from pandas_datareader import data, wb
import datetime

# We'll use following visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# --------  loading provided "pickle file" of the "stock data from Jan 1st 2006 to Jan 1st 2016"  --------

# provided data is a "pickle" file so read_csv wont work
# Read in the csv file and as a dataframe
# df = pd.read_csv("./data_all_banks")
df = pd.read_pickle("data_all_banks")  # Load a pickle file into a DataFrame

# data info
df.info()

# inspect first 5 row
df.head(5)

# It's in multi-level index form of DataFrame
    # there are 6 banks (first level)
    # each bank contains 2517 rows × 5 columns (second level)

df['BAC']
df['C']




# --------  about the Data  --------

# We need to get data using "pandas datareader". We will get stock information for the following banks:
    # Bank of America
    # CitiGroup
    # Goldman Sachs
    # JPMorgan Chase
    # Morgan Stanley
    # Wells Fargo


# Get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. 
    # Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. 

# This will involve a few steps:
    # 1. Use datetime() to set start and end datetime objects.
    # 2. Figure out the ticker symbol for each bank.
    # 2. Figure out how to use datareader to grab info on the stock.
    #    -  Use Google Finance (or Yahoo Finance)

# Use this documentation: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html


# Use Google Finance (or Yahoo Finance) as a source, for example:
    # Bank of America
    # BAC = data.DataReader("BAC", 'google', start, end)


# NOTE: Check the link above for the latest API (or search online for latest API), as 'google' may not always work.
        # Google Finance no longer provides a public API or support in pandas-datareader. 
        # Use Yahoo Finance, Alpha Vantage, or Market Data API for real-time and historical stock data.


# --------  ONLINE: getting data from "yahoo finance"  --------

import datetime
import pandas as pd
import pandas_datareader.data as data

# Define start and end dates
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# Define bank tickers
# Create a list of the "ticker symbols" (as strings) in alphabetical order. 
    # Call this list: "tickers"
tickers = ['BAC', 'CTG', 'GS', 'JPM', 'MS', 'WFC']

# Fetch data for each bank using "Yahoo Finance" since 
BAC = data.DataReader("BAC", 'yahoo', start, end)       # Bank of America
CTG = data.DataReader("CTG", 'yahoo', start, end)       # CitiGroup
GS = data.DataReader("GS", 'yahoo', start, end)     # Goldman Sachs
JPM = data.DataReader("JPM", 'yahoo', start, end)       # JPMorgan Chase
MS = data.DataReader("MS", 'yahoo', start, end)     # Morgan Stanley
WFC = data.DataReader("WFC", 'yahoo', start, end)       # Wells Fargo

# Fetch data for all banks in a single call
df = data.DataReader(tickers, 'yahoo', start, end)

# Fetcing could also do this for a "Panel Object"
# df = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'], 'yahoo', start, end)


# ----------------    Concatenate dataframes    ----------------
# Concatenate dataframes into a single dataframe:
# Use "pd.concat" to concatenate the bank dataframes together to a single dataframe called bank_stocks
    # Set the keys argument equal to the "tickers" list. 
    # Also pay attention to what axis you concatenate on.
bank_stocks = pd.concat([BAC, CTG, GS, JPM, MS, WFC], axis=1, keys=tickers)

# Set column name levels
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

# Display the head of the dataframe
print(bank_stocks.head())

# Save as a pickle file for efficient storage
import pickle
with open("bank_stocks_yahoo.pkl", 'wb') as f:
    pickle.dump(bank_stocks, f)



# --------  ALTERNATIVE(online): getting data from "yfinance"  --------

# Install yfinance from PYPI using pip
    # pip install yfinance
    # https://yfinance-python.org/
    # https://github.com/ranaroussi/yfinance

# check first: Use "yfinance" Directly Instead of "pandas_datareader"
    # This method bypasses "pandas_datareader" and directly uses "yfinance", which is more reliable.
    # If this works, it means yfinance is functioning properly.
import yfinance as yf
import datetime

# Define start and end dates
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2024, 1, 1)

# Fetch stock data directly using yfinance
df = yf.download("AAPL", start=start, end=end)

# Display the first few rows
print(df.head())
# ------------------------------------------------



# ----------------    now we get our DataSet    ----------------
import datetime
import pandas as pd
import yfinance as yf

# Define start and end dates
start = "2006-01-01"
end = "2016-01-01"

# Define bank tickers
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']  # Fixed 'CTG' -> 'C' for CitiGroup

# Fetch data for all banks using yfinance
bank_data = {ticker: yf.download(ticker, start=start, end=end) for ticker in tickers}

# Concatenate dataframes into a single dataframe with MultiIndex
bank_stocks = pd.concat(bank_data, axis=1, keys=tickers)

# Display the first few rows
bank_stocks.head()


# Note that: we can't set the multi-level index as before because "bank_stocks" has three levels instead of two. 
    # This happens since "yfinance.download()" already returns a "MultiIndex" with Stock Info (Open/Close) and Ticker, 
    # and concatenating adds another level.

# we use following way ----
# Check the number of levels in the MultiIndex
print(bank_stocks.columns.nlevels)  # Should print 3

# Drop the extra level by resetting the column index
bank_stocks.columns = bank_stocks.columns.droplevel(2)  # Drops the repeated ticker level
bank_stocks.head()  # Display the change


# Now correctly assign MultiIndex column names
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

# Display the fixed columns
bank_stocks.head()


# ----    save as pickle    ----
# to_pickle() comes from "pandas". 
    # It is a method available for pandas "DataFrames" and "Series", 
    # allowing you to serialize and save data in "pickle" format
bank_stocks.to_pickle("bank_stocks_yahoo.pkl")




# ----------------    EDA    ----------------
# EDA stands for Exploratory Data Analysis. 
# It involves analyzing and visualizing datasets to understand 
    # patterns, trends, and relationships before applying further data processing or modeling.

# ----  load the pickle dataset  ----
df1 = pd.read_pickle("bank_stocks_yahoo.pkl")  # Load a pickle file into a DataFrame

# data info
df1.info()

# inspect first 5 row
df1.head(5)

# The DataFrame has a multi-level index:
    # 6 banks at the first level.
    # Each bank has 2517 rows and 5 columns
df1['BAC']
df1['C']


# ----    cross-section (xs)    ----
# Check the column index levels
print(df1.columns)  # This will show the structure of the MultiIndex columns

# DataFrame has a two-level MultiIndex for columns:
    # Level 0: Bank Ticker (BAC, C, GS, etc.)
    # Level 1: Stock Info (Close, High, Low, etc.)

# xs can skip levels to get deep into multi-level-index
# returns cross-section of row(s) or column(s) in multi-indexed dataframe
    # axis=0: Operate on rows (index-wise)
    # axis=1: Operate on columns (column-wise)
close_prices = df1.xs('Close', level="Stock Info", axis=1) # 'Close' valuse for all 6 banks
print(close_prices)

# What is the max Close price for each bank's stock throughout the time period?
max_close_prices = close_prices.max()
print(max_close_prices)

# in single line
df1.xs(key='Close', axis=1, level='Stock Info').max()



# ------------    calculate RETURNS    ------------
# Create a new empty DataFrame called "returns" for daily return percentages for each bank's stock.
# This dataframe will contain the returns for each bank's stock. 
returns = pd.DataFrame()

# LATEX note: 
    # block level math $$...$$ and \[...\]
    # inline math $...$ and \(...\)

# returns are typically defined by:
    # $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$
    # Where $p_t$ is today's price and $p_{t-1}$ is the previous day's price.


# Use .pct_change() to compute daily returns for each bank's "Close" price.
# Store the results in returns.

for bank in close_prices.columns:
    returns[bank+' return'] = close_prices[bank].pct_change()


# about pct_change(): 
    # It is fractional change between the current and a prior element.
    # Computes the fractional change from the immediately previous row by default. 
    # This is useful in comparing the fraction of change in a time series of elements.



# ---------------  observations  ---------------
# observations from "returns"
    # The "returns" DataFrame contains the percentage change in stock prices for each bank over time. 
        # Each column represents a bank's stock, and each row represents the daily return for that bank.
        
    # In the "returns" DataFrame, what do +ve and -ve values mean?
        # (+ve) : Indicates the stock price increased compared to the previous day.
        # (-ve) : Indicates the stock price decreased compared to the previous day.


# Create a pairplot using seaborn from "returns" data 
import seaborn as sns
sns.pairplot(returns[1:])
# To set the bin size, use the "diag_kws" parameter, which allows passing arguments to the "diagonal histograms".
sns.pairplot(returns[1:], diag_kws={'bins': 30})  # Set bins to 30


# How to Identify the Best/Worst Performing Stock?

# --------  Calculate Summary Statistics  --------
#     Use .mean() to get the average return.
#     Use .std() to check volatility (higher standard deviation means more risk).

returns.mean()
returns.std()

# Find the Best/Worst Performing Stock:
    # The highest mean return -> Best-performing stock.
    # The lowest mean return -> Worst-performing stock.

best_stock = returns.mean().idxmax()
worst_stock = returns.mean().idxmin()
print(f"Best performing stock: {best_stock}")
print(f"Worst performing stock: {worst_stock}")


# Visualize Returns:
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.boxplot(data=returns)
plt.title("Stock Return Distribution")
plt.show()



# -------------  subplots  -------------
# Below is a subplots-based visualization that separately plots histograms with 
    # KDE (Kernel Density Estimation) and 
    # standard deviation (std) lines 
# for each bank in the returns DataFrame.

# Histogram & KDE are plotted together (sns.histplot() with kde=True).
# Standard deviation lines are drawn using ax.axvline().

# Handles multiple banks dynamically (for i, bank in enumerate(returns.columns)).

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Define number of banks (columns in 'returns')
num_banks = len(returns.columns)

# Create subplots: one row per bank
fig, axes = plt.subplots(num_banks, 1, figsize=(10, 3 * num_banks))

# Loop through each bank and plot histogram with KDE & std
for i, bank in enumerate(returns.columns):
    ax = axes[i] if num_banks > 1 else axes  # Handle single subplot case
    
    # Plot histogram & KDE
    sns.histplot(returns[bank], kde=True, bins=30, ax=ax)
    
    # Compute mean & standard deviation
    mean_val = returns[bank].mean()
    std_val = returns[bank].std()
    
    # Draw standard deviation lines
    ax.axvline(mean_val, color='red', linestyle='--', label='Mean')
    ax.axvline(mean_val + std_val, color='blue', linestyle='--', label='±1 Std')
    ax.axvline(mean_val - std_val, color='blue', linestyle='--')
    
    ax.set_title(f"Returns Distribution for {bank}")
    ax.legend()

# Adjust layout and show plot
plt.tight_layout()
plt.show()




# -------------  subplot (same scale)  -------------
# Volatility: A high standard deviation may indicate a riskier stock.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Define number of banks (columns in 'returns')
num_banks = len(returns.columns)

# Define subplot grid (3 rows, 2 columns)
fig, axes = plt.subplots(3, 2, figsize=(12, 10))

# Flatten axes array for easier indexing
axes = axes.flatten()

# Fixed x, y axis range
x_min, x_max = -0.1, 0.1
y_min, y_max = 0, 2000

# Loop through each bank and plot histogram with KDE & std
for i, bank in enumerate(returns.columns):
    ax = axes[i]

    # Plot histogram & KDE
    sns.histplot(returns[bank], kde=True, bins=30, ax=ax)
    
    # Compute mean & standard deviation
    mean_val = returns[bank].mean()
    std_val = returns[bank].std()
    
    # Draw standard deviation lines
    ax.axvline(mean_val, color='red', linestyle='--', label='Mean')
    ax.axvline(mean_val + std_val, color='blue', linestyle='--', label='±1 Std')
    ax.axvline(mean_val - std_val, color='blue', linestyle='--')
    
    # Set title and x-axis limits
    ax.set_title(f"Returns Distribution for {bank}")
    ax.set_xlim(x_min, x_max)  # Fixed x-axis range
    ax.set_ylim(y_min, y_max)  # Fixed y-axis range
    ax.legend()

# Hide unused subplots if num_banks < 6
for i in range(num_banks, len(axes)):
    fig.delaxes(axes[i])

# Adjust layout and show plot
plt.tight_layout()
plt.show()



# CONCLUSION:
    # Citigroup, has experienced significant stock price fluctuations over the years, notably during the 2007-2008 financial crisis.
    # Background on Citigroup's Stock Crash available here.
        # https://en.wikipedia.org/wiki/Citigroup#November_2008.2C_Collapse_.26_US_Government_Intervention_.28part_of_the_Global_Financial_Crisis.29

        # Citigroup, formed in 1998 through a merger, grew to be one of the world’s largest financial institutions. 
            # By 2006, it was highly valuable, with $1.9 trillion in assets.

        # However, during the 2007–2008 financial crisis, heavy exposure to "subprime mortgages" led to massive losses—
            # nearly $10 billion in one quarter—and its stock price collapsed to under $1 by early 2009.

        # The U.S. government stepped in with bailouts, but the company's value still dropped drastically. 
            # In 2011, a reverse stock split was used to stabilize its share price.

        # As of 2022, Citigroup's stock remained far below pre-crisis levels, showing how deeply the crisis impacted the company long-term.


# You'll also see the enormous crash in value if you take a look a the stock price plot (which we do later in the visualizations.




# --------  best and worst single day returns  --------

# short "returns" processing
df1 = pd.read_pickle("bank_stocks_yahoo.pkl")  # Load a pickle file into a DataFrame
close_prices = df1.xs('Close', level="Stock Info", axis=1) # 'Close' valuse for all 6 banks

returns = pd.DataFrame()
for bank in close_prices.columns:
    returns[bank+' return'] = close_prices[bank].pct_change()


# Identify the dates on which each bank stock had the "highest" (best) and "lowest" (worst) single-day returns.

for bank in returns.columns:
    max_return_date = returns[bank].idxmax()
    min_return_date = returns[bank].idxmin()
    max_return = returns[bank].loc[max_return_date]
    min_return = returns[bank].loc[min_return_date]

    print(f"{bank}:")
    print(f"  Best Day:   {max_return_date.date()} — Return: {max_return:.4f}")
    print(f"  Worst Day:  {min_return_date.date()} — Return: {min_return:.4f}")
    print()

# Notie: Four of the banks experienced their worst drop on the same date. 
#           it is "2009-01-20" and the banks are BAC, GS, JPM, WFC
#       Investigate whether a significant event occurred on that day.

""" 
    Significant Drop in Bank Stocks — January 20, 2009

    On January 20, 2009, four major U.S. banks —
        Bank of America (BAC), Goldman Sachs (GS), JPMorgan Chase (JPM), and Wells Fargo (WFC) 
        experienced their worst single-day stock return in the dataset.

    This sharp decline coincided with the "inauguration of President Barack Obama", 
    suggesting that the market downturn occurred during a period of heightened uncertainty and stress in the financial sector. 
"""


# --------  using "old pickle" from google  --------
# short "returns" processing. Now we use the "old pickle" from google
df1 = pd.read_pickle("data_all_banks")  # Load a pickle file into a DataFrame
close_prices = df1.xs('Close', level="Stock Info", axis=1) # 'Close' valuse for all 6 banks

returns = pd.DataFrame()
for bank in close_prices.columns:
    returns[bank+' return'] = close_prices[bank].pct_change()

# Worst Drop (4 of them on Inauguration day)
returns.idxmin()

# Best Single Day Gain
# citigroup stock split in May 2011, but also JPM day after inauguration.
returns.idxmax()



# --------  Citigroup's Largest Gain and Drop  --------

# Citigroup's biggest single-day gain and largest drop happened just days apart:
    #   C return:
    #       Best Day:   2011-05-09 — Return: 8.7699
    #       Worst Day:  2011-05-06 — Return: -0.8991

# ​In May 2011, Citigroup had a stock split:
""" 
    ----  Citigroup Reverse Stock Split - May 2011  ----
    In May 2011, Citigroup carried out a 1-for-10 reverse stock split, 
        meaning every 10 existing shares were combined into 1 new share. 
        This reduced the number of outstanding shares from about 29 billion to 2.9 billion.

    Effective Date: 
        The split became official after the market closed on May 6, 2011, 
        and trading resumed with adjusted prices on May 9, 2011.

    Purpose: 
        The move aimed to raise the share price and make the stock more attractive to institutional investors.

    # https://www.citigroup.com/global/investors/stockholder-services/stock-split-history
"""



# ----  rev[08-apr-2025]  ----
# riskiest stock
# ** Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire time period? Which would you classify as the riskiest for the year 2015?**

