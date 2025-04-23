
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
# sns.set_style('whitegrid')

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
# Notice "C" Citigroup has wieard vertical scatterplot, it indicates the huge crash of Citigroup in 2008


# How to Identify the Best/Worst Performing Stock?

# --------  Calculate Summary Statistics  --------
#     Use .mean() to get the average return.
#     Use .std() to check volatility (higher standard deviation means more risk).

# Volatility: A high standard deviation may indicate a riskier stock.
    # When we get a large standard deviation it means the stocks going "up" and "down" a lot
    # small standard deviation means proce is steady

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
    # When we get a large standard deviation it means the stocks going "up" and "down" a lot
    # small standard deviation means proce is steady

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



# ----  riskiest stock  ----
# Overall Risk: 
    # Check the "standard deviation" of returns for each stock over the full time period. 
    # A higher value indicates more volatility (i.e., higher risk).

# Risk in 2015: 
    # Repeat the same analysis, but only using data from 2015 to see which stock was the most volatile that year.

# Overall standard deviation (entire time period)
overall_std = returns.std().sort_values(ascending=False)
print("Standard Deviation - Entire Period:")
print(overall_std)

# Standard deviation for the year 2015
returns_2015 = returns['2015']
std_2015 = returns_2015.std().sort_values(ascending=False)
print("\nStandard Deviation - Year 2015:")
print(std_2015)

# alternative:
returns.std()   # overall
returns.ix['2015-01-01':'2015-12-31'].std()     # for the year 2015

# results:
    # Overall Risk: Citigroup is riskiest
    # Risk in 2015: Morgan Stanley (MS), Bank of America (BAC)


# Create a distplot using seaborn of the 2015 returns for Morgan Stanley
returns["MS"]['2015']
sns.distplot(returns['2015']['MS return'], bins=100, color='red', kde=True)

# instead of distplot, we do histplot
ms_ret = returns['2015']['MS return']
sns.histplot(ms_ret, bins=100, color='red', kde=True)

# Create a distplot using seaborn of the 2008 returns for CitiGroup
c_ret = returns['2008']['C return']
sns.histplot(c_ret, bins=100, color='green', kde=True)




# ----------------    more VISUALIZATION    ----------------
# This project emphasizes visualizations. You can use any library you prefer—like 
# Seaborn, Matplotlib, Plotly, Cufflinks, or even just Pandas—to recreate the plots described below.

# Visualize Close prices of all Banks in line plot
    # Create a line plot to show the Close prices of all banks over time.
    # Tip: Use a loop or .xs() to extract Close prices for each bank.

# We'll use the "old pickle" from google
df1 = pd.read_pickle("data_all_banks")  # Load a pickle file into a DataFrame
close_prices = df1.xs('Close', level="Stock Info", axis=1) # 'Close' valuse for all 6 banks

# Plot using matplotlib
plt.figure(figsize=(12, 6))

for bank in close_prices.columns:
    plt.plot(close_prices.index, close_prices[bank], label=bank)

plt.title("Close Prices of All Banks Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.legend()
plt.tight_layout()
plt.show()


# alternative code 1: Builtin
for bank in close_prices.columns:
    close_prices[bank].plot(figsize=(12,4),label=bank)
plt.legend()


# alternative code 2: directly from DataFrame
df1.xs(key='Close', axis=1, level='Stock Info').plot()


# alternative code 3: using plotly
df1.xs(key='Close', axis=1, level='Stock Info').iplot()



""" 
    ----  Moving Averages  ----
    Whats a moving avearge? 
        A moving average (MA) is a statistical technique used to "smooth out short-term fluctuations" and 
        highlight longer-term trends in a dataset—commonly applied to time series data like stock prices.

    Its a sliding window:
        A moving average calculates the average value of a variable (e.g., stock closing price) over a sliding window of time.
        For example:
            A 5-day moving average of stock prices takes the average of the last 5 days, 
            then shifts forward one day and does it again.

    Types of Moving Averages:
        Simple Moving Average (SMA):    Equal weighting of past values over the selected window.
        Exponential Moving Average (EMA):   Gives more weight to recent data; reacts more quickly to changes.


    Usage of MA:
        Trend Detection: Helps identify bullish (upward) or bearish (downward) trends.
        Noise Reduction: Removes daily volatility and makes patterns clearer.
        It's widely used in-
                    machine learning (ML), 
                    deep learning (DL), and 
                    reinforcement learning (RL)  
            in different ways depending on the context.

            For example in Reinforcement Learning (RL):
                Moving average is used to track reward trends:
                To observe agent performance over time. 
"""


# Moving Averages in the year 2008. 
    # Analyze the 30-day moving average of Bank of America's (BAC) stock during the year 2008.
    # Plot both the "rolling 30-day average" and the "actual Close price" to observe trends and smoothing effects.

# following both give the same results:
close_prices['BAC']['2008']
# or
close_prices['BAC']['2008-01-01':'2009-01-01']

# BAC's close in 2008
bac_close_2008 = close_prices['BAC']['2008']

# Compute 30-day moving average
bac_rolling_30 = bac_close_2008.rolling(window=30).mean()

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(bac_close_2008, label='BAC Close Price (2008)', alpha=0.6)
plt.plot(bac_rolling_30, label='30-Day Moving Average', linewidth=2)

plt.title('Bank of America Stock - 30-Day Moving Average (2008)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.tight_layout()
plt.show()


# ALTERNATIVE: Using "ix"
plt.figure(figsize=(12,6))
close_prices['BAC']['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
close_prices['BAC']['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()


# --------    rolling() in Pandas    --------
# The .rolling() function in pandas is used to create a rolling view 
    # (or sliding window) over a time series or sequence of data.

    # It allows the computation of moving (rolling) statistics, such as:
        # Moving averages
        # Rolling sums
        # Rolling standard deviations
        # And more

df['Close'].rolling(window=30)
# This sets up a window of 30 values, moving one step at a time through the data. 
# But it doesn't compute anything until you apply an AGGREGATION FUNCTION, like .mean(), .sum(), .std(), etc.



# ----  heatmap and clustermap  ----

# Heatmap of the correlation between the Close Price.
sns.heatmap(df1.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)

# Clustermap to cluster the correlations:
sns.clustermap(close_prices.corr(),annot=True)




# ----    cufflinks: using local "Plotly.js"   ----
# use 'cdn' or 'plotly-2.35.2.min.js in working directory'
    # The HTML file's large size is primarily due to the embedded Plotly.js.
    # we can download "Plotly.js" to our working directory and reference it locally.
    # pio.write_html(fig, 'plot_local_plotly_js.html', include_plotlyjs='.\plotly-2.35.2.min.js')
import cufflinks as cf

import plotly.io as pio
import plotly.express as px

close_corr = df1.xs(key='Close', axis=1, level='Stock Info').corr()

# credentials required: skipped
fig1 = close_corr.iplot(kind='heatmap',colorscale='rdylbu')
# save to html
pio.write_html(fig1, 'stock_fig1_heatmap.html', include_plotlyjs='.\plotly-2.35.2.min.js')


# --------------  ALTRENATIVE: heatmap  --------------
# instead use following (directly use go.Figure obj to save as html)
import plotly.graph_objects as go
from plotly.offline import iplot, init_notebook_mode
import pandas as pd

# Initialize notebook mode
init_notebook_mode(connected=True)

# Example Data
corr = close_corr

# Heatmap figure
fig = go.Figure(data=go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.columns,
    colorscale='Viridis'
))

# Plot offline inside notebook
iplot(fig)

# save to html
pio.write_html(fig, 'stock_fig1_heatmap.html', include_plotlyjs='.\plotly-2.35.2.min.js')



# --------------  ALTRENATIVE: candleplot  --------------
# candle in iplot() and Candlestick in plotly.graph_objects refer to the same type of chart

# Use .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.
# df1['BAC'][['Open', 'High', 'Low', 'Close']]['2015']
# or
# df1['BAC'][['Open', 'High', 'Low', 'Close']]['2015-01-01':'2016-01-01']

# not works. Use alternative instead
fig1 = df1['BAC'][['Open', 'High', 'Low', 'Close']]['2015'].iplot(kind='candle')


# alternative candleplot
import plotly.graph_objects as go

# Filter BAC stock data for 2015
bac_2015 = df1['BAC'][['Open', 'High', 'Low', 'Close']]['2015']

# Create candlestick chart
fig1 = go.Figure(data=[go.Candlestick(
    x=bac_2015.index,
    open=bac_2015['Open'],
    high=bac_2015['High'],
    low=bac_2015['Low'],
    close=bac_2015['Close']
)])

fig1.update_layout(title='BAC Stock - Candlestick Chart (2015)',
                   xaxis_title='Date',
                   yaxis_title='Price',
                   xaxis_rangeslider_visible=False)

# Show the plot
fig1.show()

# save to html
pio.write_html(fig1, 'stock_fig2_candleplot.html', include_plotlyjs='.\plotly-2.35.2.min.js')




# --------  PLOTLY: Simple Moving Averages plot  --------
# provides a clear visualization of the stock's closing price alongside its short-term and long-term trends for a technical analysis

# Use .ta_plot(study='sma') to create a Simple Moving Averages plot of "Morgan Stanley" for the year 2015.
fig = MS['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='sma',periods=[13,21,55],title='Simple Moving Averages')


# Above is no longer used; use the following ALTERNATIVE instead.
# Note: 
        # "df1" must be a multi-level column structure with stock tickers at the top level
        # rolling(window).mean() function in pandas computes the moving average over the specified window

        # Each "go.Scatter" trace represents a line on the plot. 
            # You can customize the appearance by modifying parameters like "line=dict(color='blue')"

import pandas as pd
import plotly.graph_objects as go

# Assuming df1 is your DataFrame with multi-level columns
# Extract BAC data for 2015
bac_2015 = df1['MS'].loc['2015', ['Close']].copy()

# Calculate SMAs using pandas
bac_2015['SMA_13'] = bac_2015['Close'].rolling(window=13).mean()
bac_2015['SMA_21'] = bac_2015['Close'].rolling(window=21).mean()
bac_2015['SMA_55'] = bac_2015['Close'].rolling(window=55).mean()

# Create the figure
fig2 = go.Figure()

# Add Close price trace
fig2.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['Close'],
    mode='lines',
    name='Close Price',
    line=dict(color='black')
))

# Add SMA traces
fig2.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['SMA_13'],
    mode='lines',
    name='SMA 13',
    line=dict(color='blue')
))
fig2.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['SMA_21'],
    mode='lines',
    name='SMA 21',
    line=dict(color='orange')
))
fig2.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['SMA_55'],
    mode='lines',
    name='SMA 55',
    line=dict(color='green')
))

# Update layout
fig2.update_layout(
    title='BAC Close Price with SMAs (2015)',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False
)

# Show the plot
# fig2.show()

# save to html
import plotly.io as pio
pio.write_html(fig2, 'stock_fig3_SMA.html', include_plotlyjs='.\plotly-2.35.2.min.js')





# --------  PLOTLY: Bollinger Band Plot  --------

# Use .ta_plot(study='boll') to create a Bollinger Band Plot for Bank of America for the year 2015.
fig = BAC['Close'].ix['2015-01-01':'2016-01-01'].ta_plot(study='boll')

# Above is no longer valid; use the following ALTERNATIVE instead.
# What It Shows:
    # Close Price: Black line.
    # 20-day SMA: Blue line (midline of Bollinger Band).
    # Upper & Lower Bands: Green and red lines.
    # Shaded Region: Volatility envelope indicating ±2 standard deviations from SMA.

import pandas as pd
import plotly.graph_objects as go

# Extract BAC 'Close' data for 2015
bac_2015 = df1['BAC'].loc['2015', ['Close']].copy()

# Calculate 20-day Simple Moving Average (SMA)
bac_2015['SMA_20'] = bac_2015['Close'].rolling(window=20).mean()

# Calculate rolling standard deviation
bac_2015['STD_20'] = bac_2015['Close'].rolling(window=20).std()

# Calculate Upper and Lower Bollinger Bands
bac_2015['Upper Band'] = bac_2015['SMA_20'] + (2 * bac_2015['STD_20'])
bac_2015['Lower Band'] = bac_2015['SMA_20'] - (2 * bac_2015['STD_20'])

# Create the figure
fig3 = go.Figure()

# Close price
fig3.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['Close'],
    mode='lines',
    name='Close Price',
    line=dict(color='black')
))

# SMA 20
fig3.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['SMA_20'],
    mode='lines',
    name='SMA 20',
    line=dict(color='blue')
))

# Upper Bollinger Band
fig3.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['Upper Band'],
    mode='lines',
    name='Upper Band',
    line=dict(color='green'),
    opacity=0.5
))

# Lower Bollinger Band
fig3.add_trace(go.Scatter(
    x=bac_2015.index,
    y=bac_2015['Lower Band'],
    mode='lines',
    name='Lower Band',
    line=dict(color='red'),
    opacity=0.5
))

# Fill area between bands
fig3.add_trace(go.Scatter(
    x=bac_2015.index.tolist() + bac_2015.index[::-1].tolist(),
    y=bac_2015['Upper Band'].tolist() + bac_2015['Lower Band'][::-1].tolist(),
    fill='toself',
    fillcolor='rgba(173,216,230,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    showlegend=False
))

# Layout settings
fig3.update_layout(
    title='BAC Bollinger Bands (2015)',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False
)

# Show plot
# fig3.show()

# save to html
import plotly.io as pio
pio.write_html(fig3, 'stock_fig4_BollingerBand.html', include_plotlyjs='.\plotly-2.35.2.min.js')

