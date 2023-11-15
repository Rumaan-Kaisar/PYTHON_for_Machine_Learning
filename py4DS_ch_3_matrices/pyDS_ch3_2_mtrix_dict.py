
# Courses: A-Z PY for Data-Science    4.2, 4.3, 4.4, 4.5


# since we'll work with data-frames in Data-science, we need to understand MATRICES


# --------------    Matrix INDEXATION in python    --------------

# locate a single element in a 2D matrix
# matrix[row, column], and both start from 0
A[2, 3]     # an elemnt from 3rd-row and 4-th column


# locate a ROW      matrix[row, : ]
A[1, :]     # 2nd row


# locate a COLUMN   matrix[ :, col]
A[:, 3]     # 4th column




# --------------------    Our First Matrix    --------------------
# Import numpy
# Create a List-of-Lists
# convert the to 2D-array (matrix) using 'np.array'

import numpy as np

a = [.00, .01, .02]
b = [.10, .11, .12]
c = [.20, .21, .22]

mat_1 = np.array([a, b, c])




# --------------    creating a matrix    --------------

# method 1: np.reshape( data , dim , 'C')
    # matrix will be populated row-by-row 
        # in R column-by-column

    # C: it means C-programming (default)
        # C-like matrix-population (row-by-row)

    # F: it means FORTRAN-programming
        # FORTRAN-like matrix-population (column-by-column)
        # np.reshape( data , dim , 'F')
 


# method 2: np.array()
    # it puts row into matrices
        # it combines data into matrices




# METHOD 1: np.reshape(data, (row, column))
import numpy as np
mydata = np.arange(0, 20) # create a list of 20 numbers
print(mydata)
type(mydata)    # numpy.ndarray

np.reshape(mydata, (4, 5))

# applying order-flags 'F', 'C'
mat_1 = np.reshape(mydata, (4, 5), order='C')
mat_2 = np.reshape(mydata, (4, 5), order='F')

# Notice how the matrices populated!!
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])

array([[ 0,  4,  8, 12, 16],
       [ 1,  5,  9, 13, 17],
       [ 2,  6, 10, 14, 18],
       [ 3,  7, 11, 15, 19]])


# getting individual element
print(mat_1[2, 4])  # 14
print(mat_2[2, 4])  # 18


# Note :
""" 
    arange([start,] stop[, step,], dtype=None, *, like=None)
        Return evenly spaced values within a given interval.
        the interval including 'start' but excluding 'stop'
    python pyDS_ch3_2_mtrix_dict.py 
"""




# ------------------    using ordinary-list    ------------------

# creating matrices from a list (no 'numpy.ndarray' TYPE)
import numpy as np
mydata_2 = range(20) # create a list of 20 numbers
print(mydata_2)
type(mydata_2)    # numpy.ndarray

np.reshape(mydata_2, (4, 5))

# applying order-flags 'F', 'C'
mat_1 = np.reshape(mydata_2, (4, 5), order='C')
mat_2 = np.reshape(mydata_2, (4, 5), order='F')

# getting individual element
print(mat_1[2, 4])  # 14
print(mat_2[2, 4])  # 18

# To avoid using 'numpy.ndarray' object we've used ordinary-list




# ------------------    OOP concept    ------------------
import numpy as np
mydata = np.arange(0, 20) # create a list of 20 numbers
# Note:
    # since 'np.arange(0, 20)' will create a 'numpy.ndarray' TYPE object
    # and this object already has "reshape" method (and other methods as well), we can directly use:

mydata.reshape((5, 4))  # there is no need "mydata" as argument: np.reshape(mydata, (5, 4))
# mydata is an object that already contains "reshape" method




# METHOD 2:  np.array(): won't wprk for jagged array (unequal row-length)
import numpy as np

r1 = ["I", "am", "happy"] 
r2 = ["What", "a", "day"] 
r3 = [1, 2, 3]
r4 = [2.5, 3.7, 3.1415, 1.618, 0.0] # 5 elemnt, makes jagged array

# create a "list-of-list"
li_li = [r1, r2, r3, r4]

# np.array will combine this li_li into a matrix row-by-row
    # there is also type-info in "dtype"
    # also numerical data will change into "string" if strings are present
    # we can have ony one type of data in an "array"
np.array(li_li, dtype=object) # '<U5' dtype won't work due to jagged array

# VisibleDeprecationWarning: 
    # Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. 
    # If you meant to do this, you must specify 'dtype=object' when creating the ndarray.


# Solution: Works well with equal-length rows (no jagging)
import numpy as np
r1 = ["I", "am", "happy"] 
r2 = ["What", "a", "day"] 
r3 = [1, 2, 3]
r4 = [2.5, 3.7, 3.1415]

li_li = [r1, r2, r3, r4]

np.array(li_li, dtype='<U5')
# array([['I', 'am', 'happy'],
#        ['What', 'a', 'day'],
#        ['1', '2', '3'],
#        ['2.5', '3.7', '3.141']], dtype='<U5')




# Example 1: using '<U5' dtype
import numpy as np

r1 = ["I", "am", "happy"] 
r2 = ["What", "a", "day"] 
r3 = [1, 2, 3]
# r4 = [2.5, 3.7, 3.1415, 1.618]

li_li = [r1, r2, r3]

np.array(li_li, dtype='<U5')
# array([['I', 'am', 'happy'],
#        ['What', 'a', 'day'],
#        ['1', '2', '3']], dtype='<U5')     




# Example 2: Use padding for jagged array
    # trying to create a jagged array
    # providing elements of incompatible types

# ATTEMPT 1 : TF padding
import tensorflow as tf

a = [[1,2,3,4,5],[1,2,3],[1]]
x = tf.keras.utils.pad_sequences(a, padding='post')
print(f"{type(x)}\n{x}")
# -----
# <class 'numpy.ndarray'>
# [[1 2 3 4 5]
#  [1 2 3 0 0]
#  [1 0 0 0 0]]



# ATTEMPT 2 : np.pad
import numpy as np
a = np.array([[1,2,3,4,5],[1,2,3],[1]])
l = np.array([len(a[i]) for i in range(len(a))])
width = l.max()
b=[]
for i in range(len(a)):
    if len(a[i]) != width:
        x = np.pad(a[i], (0,width-len(a[i])), 'constant',constant_values = 0)
    else:
        x = a[i]
    b.append(x)
b = np.array(b)
print(b)



# ATTEMPT 3 : dtype=object
import numpy as np

r1 = ["I", "am", "happy"] 
r2 = ["What", "a", "day"] 
r3 = [1, 2, 3]
r4 = [2.5, 3.7, 3.1415, 1.618]  # 4 elemnt, makes jagged array


li_li = [r1, r2, r3, r4]

np.array(li_li, dtype=object)





# ------------------    Dictionaries    ------------------
import numpy as np
# ----    Games    ----
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]

# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

# acessing : But it's hard to indicate the PLAYER
print(Games[0])
print(Games[2])

print(Games[2][9])  # 69
# alternative
print(Games[2][-1]) # 69


# ----    using Dictionaries    ----
# dictionaries are un-ordered
#  lists are ordered
dict_1 = {
    'key_1' : 'val_1',
    'key_2' : 'val_2',
    'key_3' : 'val_3',
    'key_4' : 'val_4',
}

print(dict_1['key_3'])  # val_3

# dictionaries can have different data-types
dict2 = {
    'Germany' : 'I have been here', 
    'France' : 2,	
    'Spain':True
}

# however python stores the dict-data in its own way
print(dict2)




# --------    How to use 'Dictionaries' to access following data ?    --------
import numpy as np
# ----    Games    ----
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]

# The players will follow the same order
    # we'll treat each player as a ROW

# The "GAME SEASONS" will follow the same order for each Player (ROW)
    # we'll treat each game as a COL


# Notice the corresponding dictionaries
#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}

Pdict['DwightHoward']

# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

Games[4]
Games[Pdict['DwightHoward']][Sdict['2012']]
# row : Pdict['DwightHoward'
# col : Sdict['2012']




# ------------------    Matrix Operations    ------------------
# Calculate How many field goles a player scored
# get the "FieldGoals" and devide it by the played game in the "Season"
import numpy as np

# ----    Field Goals    ----
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]
#Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])


# ----    Games    ----
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]
# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])


#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}


# by programming approach: we need to use two loops
    # devide each element of a row of "FieldGoals" by each element of a row of "Games"


# --------    Matrix-division    --------
# however it can be easily done by "Matrix-division"
    # it devides the matrices element-by-element

# Ignore Error-warnings
# use np.matrix.round() instead of "round()"

import warnings
warnings.filterwarnings('ignore')

FieldGoals / Games

FieldGoalsPerGame = np.matrix.round(FieldGoals / Games)
FieldGoalsPerGame[Pdict['DerrickRose']][Sdict['2009']]



# --------------------     Normalization     --------------------
# what we are doing by the division 'FieldGoals / Games' is NORMALIZATION
    # it is useful to remove 'unwanted-flactuation' in the data
    # Eg: a player playes average 10 games in each season, but in one season he played 2 games due to injury
    # Then there will be 'unwanted-flactuation' in his total-score data.
    # to remove this kind of irregularity we need the division (total_score / played_games_in_a_season)


# ----    Minutes Played    ----
KobeBryant_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
JoeJohnson_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
LeBronJames_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
CarmeloAnthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
DwightHoward_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
ChrisBosh_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
ChrisPaul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
KevinDurant_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
DerrickRose_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
DwayneWade_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]
#Matrix
MinutesPlayed = np.array([KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP, KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])

MinutesPlayed_PerGame = np.matrix.round(MinutesPlayed / Games)
MinutesPlayed_PerGame
MinutesPlayed_PerGame[Pdict['DerrickRose']][Sdict['2009']]


