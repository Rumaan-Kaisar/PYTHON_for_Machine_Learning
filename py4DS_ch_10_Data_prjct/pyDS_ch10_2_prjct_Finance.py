
################# 10.6:
# copy: py, ipynb, new_data
#        
#        
################# (26-Mar-25 for 28-Mar-25)

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
df1.xs(key='Close',axis=1,level='Stock Info').max()


