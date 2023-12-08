
################# 5.1: 4:40
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

