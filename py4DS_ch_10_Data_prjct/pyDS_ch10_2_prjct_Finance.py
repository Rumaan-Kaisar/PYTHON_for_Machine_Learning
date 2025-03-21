
################# 10.6:
# copy: topics txt, py(s)
#        
#        
################# (01-Mar-25 for 02-Mar-25)

# Courses: PrTla PY for DS & ML >    10.6, 10.7, 10.8, 10.9

# Download data: https://www.dropbox.com/s/s9uq4qvls4rghm7/all_banks?dl=0


# Finance Data Project 

In this data project we will focus on exploratory data analysis of stock prices. Keep in mind, this project is just meant to practice your visualization and pandas skills, it is not meant to be a robust financial analysis or be taken as financial advice.
____
** NOTE: This project is extremely challenging because it will introduce a lot of new concepts and have you looking things up on your own (we'll point you in the right direction) to try to solve the tasks issued. Feel free to just go through the solutions lecture notebook and video as a "walkthrough" project if you don't want to have to look things up yourself. You'll still learn a lot that way! **
____
We'll focus on bank stocks and see how they progressed throughout the [financial crisis](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308) all the way to early 2016.


## Get the Data

In this section we will learn how to use pandas to directly read data from Google finance using pandas!

First we need to start with the proper imports, which we've already laid out for you here.

*Note: [You'll need to install pandas-datareader for this to work!](https://github.com/pydata/pandas-datareader) Pandas datareader allows you to [read stock information directly from the internet](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) Use these links for install guidance (**pip install pandas-datareader**), or just follow along with the video lecture.*


# summerize GPT
The 2008 financial crisis, also known as the global financial crisis, was a major worldwide economic crisis, centered in the United States, which triggered the Great Recession of late 2007 to mid-2009, the most severe downturn since the Wall Street crash of 1929 and Great Depression. The causes of the financial crisis included predatory lending in the form of subprime mortgages and a resulting U.S. housing bubble, excessive risk-taking by global financial institutions, and lack of regulatory oversight. The first phase of the crisis began in early 2007, as mortgage-backed securities (MBS) tied to U.S. real estate, and a vast web of derivatives linked to those MBS, collapsed in value. A liquidity crisis spread to global institutions by mid-2007 and climaxed with the bankruptcy of Lehman Brothers in September 2008, which triggered a stock market crash and international banking crisis.[1]








### The Imports




Already filled out for you.\




from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
%matplotlib inline    

