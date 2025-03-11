
# Courses: PrTla PY for DS & ML >   6.8, 6.9, 6.10, 6.11


# ------------    Groupby    ------------
# Groupby allows you to "group together rows" based off of a column and perform an aggregate function on them.
    # the aggregate function cann be a mean, meadian or other statistical character

# Groupby and SQL: this kind of operations are common in SQL

# for example we have 3 partitions of ID's 1, 2,  3 and we have several values for them

""" 
    we can groupby the ID column and aggrigate them in 
    some sort of aggregate function, say "sum" or "product" or "mean"

        --------------------
            ID      value
        --------------------        partition 1
            1	    50.30
            1	    123.30          
            1	    132.90
        --------------------        partition 2
            2	    50.30
            2	    123.30
            2	    132.90
            2	    88.90
        --------------------        partition 3
            3	    50.30
            3	    123.30
        --------------------


        Groupby result by aggrigate function as "sum"
        --------------------
            ID      value
        --------------------        
            1	    306.50
            2	    395.40
            3	    173.60 

"""

# aggregate function:
    # It is just a fancy-name of the kind of functions that takes multiple values and output a single value
    # for example taking sum, standared deviation, average etc are all aggregate functions



# ----  groupby with pandas  ----
# groupby() allows us to: 
    # choose a column to group-by 
    # it gathers all the rows togather based of that column value and 
    # we perform an aggregate function on them

# pandas groupby() allows you to group "rows of data" together and call aggregate functions

# create a DataFrame
import pandas as pd

# Create dataframe, from a dictionary
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
df

# we have the companies: Google, Microsoft and FaceBook, name of different people & their sales

# groupby(): now we group the rows based-on of a column name
# groupby "company":
df.groupby('Company')
# it'll  create a groupby object, stored in a memory:  <pandas.core.groupby.DataFrameGroupBy object at <sEftislsK015E8B8C36D8>

# we can apply an aggregate function as below
byComp = df.groupby('Company')
byComp.mean()   # looks at "Sales" and give us the "mean"

# pandas automatically ignores "non-numeric" columns
    # it applies mean() to all the columns that have "numerical values"
    # notice "Person" isn't counted because these are strings

# applying other aggrigate functions
byComp.sum()    # sum
byComp.std()    # standared deviations
# notice, it outputs a DataFrame
    # so we can access the row of 'FB', careful about '['
byComp.sum().loc['FB']

# most of the time we'll do that in one line of code:
df.groupby('Company').sum().loc['FB']

# counts: counts noumber of instences for column
df.groupby('Company').count()
# notice "Person" is appeared, because "strings" are countable

# max, min
df.groupby('Company').max()
# also notice "Person", but in this case its maxed it according to "alphabetical order"
df.groupby('Company').min()
# so in this case we need to avoid "Person"
    # it's not a good idea to use max, min on a string column

# describe: its very useful for analyzing data-set
    # gives bunch-of information all at once
    # such as: count, mean, std, min, max, quartiles
df.groupby('Company').describe()
# we can transpose it for better view (columns become rows)
df.groupby('Company').describe().transpose()

# we can also call the column names of this transpose matrix
df.groupby('Company').describe().transpose()['FB']




# ------------    Merging Joining and Concatenating    ------------

# combine DataFrames using different methods
# There are 3 main ways of combining DataFrames together: 
        # Merging, 
        # Joining and 
        # Concatenating.


# --------    concatenation    -------- 

# Example DataFrames
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                        index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

print(df1)
print(df2)
print(df3)


# It glues together DataFrames
    # DIMENSIONs should match along the axis you are concatenating on. 
    # use-    pd.concat(list of DataFrames)
    # by Default, axis to join on is 0, i.e. it joins "row-wise"
pd.concat([df1, df2, df3])    # concate row-wise

# axis = 1: concate column-wise
    # the DataFrames are placed diagonally in a bigger matrix
    # all other elements are "NaN"
    # the reason is the row-index are different [1,2,3, . . ., 11]
pd.concat([df1, df2, df3], axis = 1)




# --------    Merging    -------- 
# using "merge logic" is similar to 'merging SQL tables' togather

# let's create two more "Example DataFrames"

lEft = pd.DataFrame( {'key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
   
riGht = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})    

print(lEft)
print(riGht)

# Notice, both have a COMMON column 'key'

# The merge() function allows you to merge DataFrames together 
    # using a similar logic as merging SQL Tables together. For example:


# pd.merge(df1, df2, how='inner', on='col_name')
    # by defaulet, how='inner'
    # on: merge on a key-column, you can pass one or more key-column
    # we merge/combine those DataFrames w.r to those key-colums
pd.merge(lEft, riGht, how='inner', on='key')
# just concatination will result repeated key-columns
# By merging we are joining the DataFrames on the common key-column they share
    # when we merge, insted of gluing the DataFrames, 
    # we're looking for which values to match up on the key-column
    # then it creates the rows using that key-column


# ----  multiple key-columns  ----

lEft2 = pd.DataFrame( { 'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
   
riGht2 = pd.DataFrame({ 'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})    

print(lEft2)
print(riGht2)

""" 

  key1 key2   A   B
0   K0   K0  A0  B0 <-
1   K0   K1  A1  B1 
2   K1   K0  A2  B2 <-
3   K2   K1  A3  B3

  key1 key2   C   D
0   K0   K0  C0  D0 <-
1   K1   K0  C1  D1 <-
2   K1   K0  C2  D2 <-
3   K2   K0  C3  D3

"""

# notice: lEft2, riGht2 has 2 key-columns 'key1' and 'key2' but they have different elemnts
#  to use multiple key-columns, use the list for 'on='

pd.merge(lEft2, riGht2, on=['key1', 'key2'])       # how='inner' is default 

""" 
        key1	key2	A	B	C	D
    0   K0	    K0	    A0	B0	C0	D0
    1   K1	    K0	    A2	B2	C1	D1
    2   K1	    K0	    A2	B2	C2	D2

    Note: "A2	B2" repeated since lEft2 has only on row containing combination "K1   K0"


    ******     Explain above using ChatGPT     ******



    Matching Rows:
        The output DataFrame only includes rows where the combination of key1 and key2 exists in "both" lEft2 and riGht2.

    Merged Columns:
        The resulting DataFrame includes all columns from both lEft2 and riGht2. 
        For matching rows, the values from both DataFrames are included.



    First Row:
        Both lEft2 and riGht2 have key1='K0' and key2='K0', 
            -so this row appears in the merged DataFrame with values from both.

    Second and Third Rows:
        Both have key1='K1' and key2='K0' in lEft2 and riGht2. 
        However, riGht2 has two rows matching this key combination (C1, D1 and C2, D2), 
            - so the row from lEft2 is repeated for each match.

"""




# SQL syntax: inner, outer, right, left
    # most of the time in PANDAS we'll use "inner" join

# merge OUTER
pd.merge(lEft2, riGht2, how="outer", on=['key1', 'key2'])

# merge RIGHT
pd.merge(lEft2, riGht2, how="right", on=['key1', 'key2'])

# merge LEFT
pd.merge(lEft2, riGht2, how="left", on=['key1', 'key2'])

# notice the MISSING values




# --------    Joining    -------- 

# combines the columns of two potentially "differently-indexed DataFrames" 
    # into a single result DataFrame.

# it's similar to merge but the "keys" to join is 'index' instead of 'columns' 

# notice the "index" are different 

left3 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right3 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

print(left3)
print(right3)

# autometically  inner-join, based on the key "index"
    # NOTE: use 'merge' to join them based on of columns
left3.join(right3)

# we can also set 'how' attribute
left3.join(right3, how='outer')




# ----------------    OPERATIONS    ----------------
# useful operations in pandas

# Creating DataFrame
import pandas as pd

dfo = pd.DataFrame({'col1':[1,2,3,4],
                    'col2':[444,555,666,444],
                    'col3':['abc', 'def','ghi','xyz']})
dfo.head()

# notice '444' is repeated

# find "uniques"
    # there are 3 methods

# ----  unique(), nunique()  ----
# all the uniques in a col
dfo['col2'].unique()       # numpy-array of all uniques in 'col2'

# number of unique-values
len(dfo['col2'].unique())
dfo['col2'].nunique()  # gives same result


# ----  value_counts()  ----
# how many times each unique-value shows up in a DataFrame
dfo['col2'].value_counts()
# no. of appearnce of unique values in 'col2'


# --------  selecting data  --------
# use conditional-selection
dfo[dfo['col1']>2]
dfo['col1']>2   # just a Boolian-Series

# using joint conditions
dfo[(dfo['col1']>2) & (dfo['col2']==444)]


# ----  apply()  ----
# it apply a "custom-function"
    # apply(function_name)
    # NOTICE: no '()' is used with "function_name"
    # it broadcast that function to each element of that column
    # it's one of the most powerfull tools in pandas
    
def times2(x):
    return x*2

dfo["col2"].apply(times2)

# apply "builtin-functions"
dfo["col3"].apply(len)  
# applying "len" to return the length of each string

# ----  apply() with "LAMBDA expression"  ----
# instead of defining whole function we can use LAMBDAS
dfo["col2"].apply(lambda x: x*2)  


# ----  map()  ----
# the map() function is a method available on Series objects that lets you transform the values in that Series.
# It works by applying a mapping—either through a dictionary, another Series, or a function—to each element of the Series.
    # Dictionary Mapping: Replace values based on a dictionary.
    # Function Application: Apply a function to each element.
    # Returns a New Series: The result is a new Series with the transformed values.

# Example Series
s = pd.Series(['apple', 'banana', 'apple', 'cherry'])

# map() Using a dictionary
fruit_map = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}     # Mapping dictionary
mapped_s = s.map(fruit_map)    # Apply mapping
print(mapped_s)

# map() Using a Function:
mapped_s = s.map(lambda x: x.upper())    # Convert each string to uppercase
print(mapped_s)



# ----  removing columns  ----
# need to specify the axis (col / row)
dfo
# remove column 1
dfo.drop("col1", axis=1)
# use "inplae=True" to make the change parmanent

# Permanently Removing a Column
del dfo['col1']


# ----   col / index names   ----
# get the column names
dfo.columns

# get the index names
dfo.index
# if the index is numerical (similar to 'range'), start, stop, step-size are shown


# ----   sorting / ordering   ----
# sort by col2: dfo.sort_values(by='column_name')
# notice the index is changed (they're attached to the rows)
dfo.sort_values(by='col1')


# ----  find Null  ----
# find "Null" values in a DataFrame: returns "Boolian DataFrame"
dfo.isnull()



# ----  PIVOT table  ----
# it's familier to advanced excel-users

# let's define a new DataFrame
import pandas as pd

data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]
        }

dfpv = pd.DataFrame(data)

# Notice the repeating values in columns: A, B, C, D
# We'll create a "multi-index DataFrame" from this table

# we'll use: pd.pivot_table(values, index, columns)
    # lets consider column 'D' is the value
    # columns 'A'. 'B' are the multi-layer-index
    # also consider 'C' be the actual column, 
        # we'll get one column for x and another for y

dfpv.pivot_table(values='D', index=['A', 'B'], columns=['C'])

# notice 'C' is in a list
# also notice the 'NaN' values, because
    # there's no value for ('bar', 'two', 'x')
    # there is no value for ('foo', 'two', 'y')





# ------------    Data I/O    ------------
# How to input data from files
# How to save data in a file

# ----  Data file types and sources  ----
    # CSV
    # Excel
    # HTML
    # SQL

# in order to work with HTML and SQL, use following librariees

""" 
    We can install with "pip" or "conda"

        conda install sqlalchemy
        conda install lxml 
        conda install html5lib 
        conda install BeautifulSoup4

"""

# Put the XML or CSV files to your current "working directory" / location
# to get the location of current "working directory":
pwd

# ----  open and read CSV files  ----
import pandas as pd
# pd.read_csv()
df_x = pd.read_csv('z_prTla_example')

# Notice: we didn't use any ".csv" extension because our file doesn't have any file extension
# most of the time a CSV file has .csv extension, in that case we must use that in read_csv()
df_x = pd.read_csv('z_prTla_example.csv')

# other read functions from Pandas
""" 
        pd.read_json
        pd.read_pickle
        pd.read_csv
        pd.read_excel
        pd.read_clipboard
        pd.read_sql
        pd.read_table
"""

# read/write a csv file
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]
        }

dfw = pd.DataFrame(data)

dfw.to_csv("my_output.csv", index=False)
# we set "index=False", because we don't want to save the indeex as a column
df_x = pd.read_csv('my_output.csv')
# Notice the use of ".csv" in both write-read

# why we use "index=False"
dfw.to_csv("my_output_2")
# notice the index is saved as "Unnamed" column
df_x = pd.read_csv('my_output_2')



# other write functions from Pandas (similar to read fumctions)
""" 
        pd.to_json
        pd.to_pickle
        pd.to_csv
        pd.to_excel
        pd.to_clipboard
        pd.to_sql
"""



# ----  open and read excel file  ----
# read/write an excel file
    # pandas only works with data 
    # not with images, formulas or macros
    # trying to do that may crash pandas

# We need to use one of the following libraries
# pip install xlrd
# or
# pip install openpyxl

# a workbook is bunch of sheets and 
# each sheet is a DataFrame

# read_excel()
import pandas as pd
# pd.read_excel(path, sheetname=)
pd.read_excel("./z_prTla_Excel_Sample.xlsx", sheet_name="Sheet1")
# pd.read_excel('z_prTla_Excel_Sample.xlsx', 'Sheet1')

# write to excel(): 
# pdObject.to_excel(path, sheetname=)
dfw.to_excel("./Excel_Sample2.xlsx", sheet_name='NewSheet')
# notice we used the pandas-DataFrame object "dfw" instead of "pd"



# ----  working with "HTML"  ----
# we may need to install libraries: 
# pip install html5lib

# it's a kind of srapping using pandas

# Failed Bank List: FDIC - Federal Deposit Insurance Corporation
# its an HTML link: https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/index.html

dataHtml = pd.read_html("https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/index.html")

# Note that it isn't directly relate to a DataFrame, it's in a List form
type(dataHtml)
# pandas trying to find every "table element" in this html link
    # then it converts each items into a DataFrame
    # we need to cycle through the dataHtml to find the actual data
dataHtml[0]

# let's explore
dataHtml[0].head()
# notice some NaN values



# ----  Working with SQL  ----
# pandas isn't actually good for SQL database
# there's many SQL engines:
    # PostgreSQL
    # MySQL
    # SQLite

# used libraries
    # pip install SQLAlchemy

# We'll built very basic SQL engine, that temporarily held in memory
# we'll use pandas to read tables as DataFrame
# we need to use specific driver to use specific SQL engine
    # if we're using PostgreSQL, we need to use library called "psycopg2"
        # "psycopg" is the most popular PostgreSQL database library for the Python
    # if we're using "MySQL" we need to use "PyMySQL" library

# create a very simple sql engine in memory
from sqlalchemy import create_engine
import pandas as pd

# read/write a csv file
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]
        }
dfw = pd.DataFrame(data)
dfw

# create a very temporary, small "sqlite" engine, database that's running in memory
# notice "///" 3-slash
engine = create_engine("sqlite:///:memory:")

# write the DataFrame to the DB (temporary engine running in the memory)
# dfw.to_sql(table_name, con=engine_name); "con" is connection
dfw.to_sql("my_table", con=engine)

# read the table: pd.read_sql(table, engine.connect())
sqlDF = pd.read_sql('my_table', con=engine.connect())
sqlDF
# notice "index" is in new column
# Note: we need to use create_engine.connect() to connect the database

# To properly close or "turn off" the SQLite engine running in memory, 
    # you need to dispose of the connection. 
    # This will release any resources associated with the engine.

# After you're done using the engine
engine.dispose()



# ----  Re-run above code  ----
# import libraries
import pandas as pd
from sqlalchemy import create_engine

# read/write a csv file
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]
        }
dfw = pd.DataFrame(data)
print(dfw)
print("\n-------------------------------")

# create a very temporary, small "sqlite" engine, database that's running in memory
# notice "///" 3-slash
engn = create_engine("sqlite:///:memory:")
dfw.to_sql("my_table", engn)

# pd.read_sql(table, engine.connect())
df = pd.read_sql("my_table", con=engn.connect())
# Note: we need to use create_engine.connect() to connect the database
print(df)

engn.dispose()  # "turn off" the SQLite engine



# --------  corr()  --------

# What is pandas.DataFrame.corr()?

"""  
    The corr() function in Pandas is used to compute the "pairwise correlation of columns" in a DataFrame. 
    CORRELATION measures the statistical relationship between two variables, with the result being a number between -1 and 1:

        1:   Perfect positive correlation. As one variable increases, the other also increases.
        0:   No correlation. The variables do not have a linear relationship.
       -1:   Perfect negative correlation. As one variable increases, the other decreases.


    By default, corr() uses the "Pearson correlation coefficient", which measures linear relationships. 
        However, Pandas also supports other methods like: 

            "Kendall's tau τ" (Kendall rank correlation coefficient) and 
            "Spearman's rho ρ" (Spearman's rank correlation coefficient) 

        by specifying the method parameter.


    Syntax:

            DataFrame.corr(method='pearson', min_periods=1)


    method: Method of correlation:
        'pearson': Standard correlation coefficient (default).
        'kendall': Kendall Tau correlation coefficient.
        'spearman': Spearman rank correlation coefficient.
        min_periods: Minimum number of observations required per pair of columns to have a valid result.

"""



# Example: following is the demo of cor()
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'C': [5, 6, 7, 8, 7],
    'D': [10, 8, 6, 4, 2]
}

df = pd.DataFrame(data)

# Calculate pairwise correlation
correlation_matrix = df.corr()
print(correlation_matrix)


""" 
    Output:

                    A         B         C         D
            A  1.000000  1.000000  0.832050 -1.000000
            B  1.000000  1.000000  0.832050 -1.000000
            C  0.832050  0.832050  1.000000 -0.832050
            D -1.000000 -1.000000 -0.832050  1.000000


    In the output:

        Columns A and B have a perfect positive correlation (1.000)
        Columns A and D have a perfect negative correlation (-1.000)
        Columns A and C have a moderate positive correlation (0.832)

"""



# How to Determine if There is Correlation in a Dataset?
""" 
    Visual Inspection: 
        Plot the data using scatter plots. 
        If the points form a 'line' or a 'clear pattern', there is likely some correlation.

        Calculate Correlation Coefficient: 
            Use df.corr() to calculate the correlation matrix:
            Look for values close to 1 or -1 for strong correlations.
            Values close to 0 indicate weak or no linear correlation.
        
        Heatmaps: 
            Use a heatmap to visualize the correlation matrix for a quick overview.



    Statistical Tests: 
        For more complex datasets, use statistical tests (like Pearson, Spearman, or Kendall) to validate correlations. 
        These tests provide 'p-values' to indicate the 'significance' of the correlation.

        Interpreting Correlation:
                Strong Correlation: |r| > 0.7
                Moderate Correlation: 0.3 < |r| < 0.7
                Weak or No Correlation: |r| < 0.3
        
            The closer the absolute value of the correlation coefficient is to 1, the stronger the correlation between the variables.

"""

# Example: Visualize using previous "demo of cor()"

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

