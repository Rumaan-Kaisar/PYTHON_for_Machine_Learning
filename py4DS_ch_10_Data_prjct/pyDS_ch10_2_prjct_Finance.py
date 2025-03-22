
################# 10.6:
# copy: topics txt, py(s)
#        
#        
################# (01-Mar-25 for 02-Mar-25)

# Courses: PrTla PY for DS & ML >    10.6, 10.7, 10.8, 10.9

# Download data: https://www.dropbox.com/s/s9uq4qvls4rghm7/all_banks?dl=0


# --------------------    Finance Data Project    --------------------
# This project is challenging as it introduces many new concepts. 
# You may need to research on your own, but guidance will be provided.


# ----  Get the Data  ----
# This section covers using pandas to read stock data from Google Finance. 

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

# We'll use following visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# provided data is a "pickle" file so read_csv wont work
# Read in the csv file and as a dataframe
# df = pd.read_csv("./data_all_banks")
df = pd.read_pickle("data_all_banks")  # Load a pickle file into a DataFrame

# data info
df.info()

# inspect first 5 row
df.head(5)










from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
%matplotlib inline    

