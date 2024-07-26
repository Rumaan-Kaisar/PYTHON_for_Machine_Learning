
################# 348: 6.8:6.00
# copy:     UPLOAD all first -> then change
#        
#        
################# (17-JUL-24 for 19-JUL-24)

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



# -=-=-=-=-=-=-    24-JUL-2024    -=-=-=-=-=-=-

################# 348: 6.8:full, 6.9: 5.29
# copy:
#        
#        
################# (24-JUL-24 for 26-JUL-24)

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

# notice: lEft2, riGht2 has 2 key-columns 'key1' and 'key2' but they have different elemnts
#  to use multiple key-columns, use the list for 'on='

pd.merge(lEft2, riGht2, on=['key1', 'key2'])       # how='inner' is default 

""" 
        key1	key2	A	B	C	D
    0   K0	    K0	    A0	B0	C0	D0
    1   K1	    K0	    A2	B2	C1	D1
    2   K1	    K0	    A2	B2	C2	D2
"""
# ******     Explain above using ChatGPT     ******





# -=-=-=-=-=-=-    26-JUL-2024    -=-=-=-=-=-=-

################# 348: 6.8:full, 6.9: 5.29
# copy:
#        
#        
################# (26-JUL-24 for 27-JUL-24)


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



