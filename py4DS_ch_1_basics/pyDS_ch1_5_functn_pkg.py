
#################  4.5: full, 4.6: 5.05
# copy: pyDS_ch1_1_PrTla_crshCrs_2.ipynb, pyDS_ch1_5_functn_pkg.py
#        
#        
################# (20-Apr-24 for 21-Apr-24)

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

# Returning vs printing
out = sqRnum(12)    # returning, stored in out
print(out)  # printing, not stored anywhere



# --------    DOCKSTRING : adding function info    --------
# use ''' or """ immediately after function declaration
# we can get information from library functions from their DOCSTRING
def sqRnum(n):
    '''
        THIS IS A DOCSTRING.
        CAN GO MULTIPLE LINES.
        THIS FUNCTION SQUARES A NUMBER.
    '''
    return n**2


def my_func4(name='Default Name'):
    """
        This is another DOCKSTRING
    """
    print("Hello "+name)


# --------    Lambda Expression, Map & Filter    --------
# use Lambda Expression instead of writing full function

# a normal function
def times2(num):
    return num*2

times2(5)

# --------    map()    --------
seq = [1,2,3,4,5]
# we want to apply times2() on each element of the list "seq"
    # method 1 : we can use a for-loop and make another list
    # method 2 : use map(), it's a python built-in function to do the same thing
""" 
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from each of the iterables. 
    Stops when the shortest iterable is exhausted.
"""

map(times2, seq)    # mapped every elemnt of "seq" in a map-obj using the function "times2"

# converting map-obj to a list
list(map(times2, seq))


# It's more usefull with "Lambda Expression" instead of writing a whole function

# --------    Lambda Expression    --------
# now we convert above times2() to a lambda function
# our function can be re-written as
def times2(num): return num*2
# in lambda expression we don't use "def times2" and "return" we define it as below
    # we just directly use the retrning expression

# lambda expression of times2()
lambda num: num*2

# we can also store it in a variable, and call it later
    # however we don't usually use lambda like this
    # we'll use lambda for a mpa() like things
t = lambda num: num*2
t(60)

# Following we use lambda inside map()
    # this time we return multiple of 3
list(map(lambda num: num*3, seq))



