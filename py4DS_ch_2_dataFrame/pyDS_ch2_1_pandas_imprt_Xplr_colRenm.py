
################# 5.1: full, 5.2: 3:20
# copy:  jupyter file, dataset
#        
#        
################# (8-dec-23 for 9-dec-23)

# Courses: A-Z PY for Data-Science    5.1, 5.2, 5.3


# ------------    importing data into python    ------------
# Objective:
    # How to work with 'Data-Frames'
    # import data into python
    # work with 'PANDAS'


# Pandas
    # it is one of the best package to work with data-frames
    # Dataframes are different from 'matrices'
    # Dataframes are similar to "Tables" in Excel

    # columns usally have headers, names, list of rows
    # it is similar to tables in Excel/SQL (or other data-science tool)

    # Pandas has similarity with R-programming




# ------------    importing data    ------------
# we'll use 2 methods to import data

import pandas as pd

# ----  Method 1: Specify Full Path To File  ----
# Windows:
stats = pd.read_csv('G:\\tut_py_A_to_Z_data_science\\Python For Data Science With Real Exercises\\P4-Demographic-Data.csv')
# extra '\' in '\\' used for escape sequence

# Mac:
stats = pd.read_csv('G:/tut_py_A_to_Z_data_science/Python For Data Science With Real Exercises/P4-Demographic-Data.csv')
# both Mac & Windows version will work in Jupyter NB.
    # However Mac-version frequently used

# Notice these Data is actually a 'Table'
    # numeration (index) dosen't count
    # also 'Heading row' doesn't count



# ----  Method 2: Change Working Directory  ----
import os

# get current working directory
print(os.getcwd())  # "H:\shared_docs\codes_pyMLDL\py4DS_ch_2_dataFrame"

# change working directory
# Windows:
os.chdir("H:\\shared_docs\\codes_py\\py_ch_14_CSV_pikling")
# Mac:
# os.chdir("H:/shared_docs/codes_py/py_ch_14_CSV_pikling")

print(os.getcwd())  # "H:\shared_docs\codes_py\py_ch_14_CSV_pikling"
stats_3 = pd.read_csv('fighters.csv')






# ------------    EXPLORING dataset    ------------
# 1. Full Dataframe
import pandas as pd
stats = pd.read_csv('G:/tut_py_A_to_Z_data_science/Python For Data Science With Real Exercises/P4-Demographic-Data.csv')
stats


# 2. Number of rows
    # in Data-Scince it's important to CHECK
    # in SQL or other language: 
        # always check length of the 'imported data' to "given data size"
        # always comment the "length of imported data" so that you can later check with the 'given data size'
        # if full-dataset isn't imported or ERR occurs, try to 'fix that' or make comment
len(stats)  # 195 rows importes


# 3. see the columns
stats.columns

