
################# 10.6:
# copy: topics txt, py(s)
#        
#        
################# (22-Mar-25 for 23-Mar-25)

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




# rev[22-Mar-2025]

# --------  about the Data  --------

# We need to get data using "pandas datareader". We will get stock information for the following banks:
    # Bank of America
    # CitiGroup
    # Goldman Sachs
    # JPMorgan Chase
    # Morgan Stanley
    # Wells Fargo

Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. 
Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:**

1. Use datetime to set start and end datetime objects.
2. Figure out the ticker symbol for each bank.
2. Figure out how to use datareader to grab info on the stock.

# Use this documentation: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html


# Use google finance as a source, for example:
    
    # Bank of America
    # BAC = data.DataReader("BAC", 'google', start, end)



# NOTE: Check the link above for the latest API (or search online for latest API), as 'google' may not always work.
        # Google Finance no longer provides a public API or support in pandas-datareader. 
        # Use Yahoo Finance, Alpha Vantage, or Market Data API for real-time and historical stock data.


# --------  ALTERNATIVE(online): getting data from "google finance"  --------

import pandas_datareader.data as web
import datetime

# Set the date range
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# Define the ticker symbols
tickers = ["BAC", "C", "GS", "JPM", "MS", "WFC"]

# Fetch stock data for each bank
stock_data = {ticker: web.DataReader(ticker, 'yahoo', start, end) for ticker in tickers}

# Example: Display first few rows of Bank of America stock data
print(stock_data["BAC"].head())



# old code

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# Bank of America
BAC = data.DataReader("BAC", 'google', start, end)

# CitiGroup
C = data.DataReader("C", 'google', start, end)

# Goldman Sachs
GS = data.DataReader("GS", 'google', start, end)

# JPMorgan Chase
JPM = data.DataReader("JPM", 'google', start, end)

# Morgan Stanley
MS = data.DataReader("MS", 'google', start, end)

# Wells Fargo
WFC = data.DataReader("WFC", 'google', start, end)


# Could also do this for a Panel Object
df = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],'google', start, end)

# Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers**
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
 

# ** Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list. Also pay attention to what axis you concatenate on.**
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)

# ** Set the column name levels (this is filled out for you):**
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

# ** Check the head of the bank_stocks dataframe.**
bank_stocks.head()




# ----------------    EDA    ----------------
# EDA stands for Exploratory Data Analysis. It involves analyzing and visualizing datasets to understand patterns, trends, and relationships before applying further data processing or modeling.
