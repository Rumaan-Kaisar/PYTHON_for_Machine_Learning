
################# 348: 6.8:3:38
# copy:
#        
#        
################# (16-JUL-24 for 17-JUL-24)

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





