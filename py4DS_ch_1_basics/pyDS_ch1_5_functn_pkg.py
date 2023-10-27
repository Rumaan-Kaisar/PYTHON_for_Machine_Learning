
# Courses: A-Z PY for Data-Science    3.6, 3.7

# min & max

my_list = list(range(20, 31))   # list [20, 21, . . . , 29, 30]
my_list
type(my_list)
len(my_list)
max(my_list)
min(my_list)




# -------    module & packages    -------
# includes data, functions, classes, methods

""" 
    module:
        A 'module' is simply a 'file' containing Python 
                definitions, 
                functions, and 
                statements. 

    package:
        A package is just a way of "COLLECTING RELATED MODULES TOGETHER" within a single tree-like hierarchy. 
        Very complex packages like "NumPy" or "SciPy" have hundreds of individual modules
            so putting those  into a directory-like structure keeps things organized and avoids name collisions.
"""


# steps to implement a package
    # find package (searcg pypi, or google)
    # install package (use pip)
    # import package or function


# Where to look for packages?
# GitHub

# Using anaconda cmd:
    # open conda cli
    # conda install pakageName

# Using windows cmd:
    # open windows cli
    # pip install pakageName



# how to import?
    # impoert 
    # form --- import
    # form --- import --- as ---


# find a repo in github
    # search -> select a language
    # use readme.md for installation instrution


# Example 1:
# pip install scrapy
import scrapy
from scrapy.crawler import CrawlerProcess



