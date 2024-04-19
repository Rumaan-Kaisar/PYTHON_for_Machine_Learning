
#################  4.5: 13.3
# copy: pyDS_ch1_1_PrTla_crshCrs_2.ipynb, pyDS_ch1_5_functn_pkg.py
#        
#        
################# (17-Apr-24 for 19-Apr-24)

# Courses: 
    # A-Z PY for Data-Science    3.6, 3.7
    # PrTla PY for DS & ML : 4.5 (9:10)


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




# ------------    Python Crash-Course (PrTla)    ------------


# --------    function    --------
def my_func(param1):
    print(param1)

my_func("Hello")


def my_func2(name):
    print("Hello "+name)

my_func2("Mi MI")


# Using default value
def my_func3(name='Default Name'):
    print("Hello "+name)

my_func3()
my_func3('Gogo')
my_func3(name='Bogo')

# () used to call (execute) a function
    # following won't call  the function
my_func3


# Return values from a function
def sqRnum(n):
    return n**2

out = sqRnum(12)
out
