
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
# Also we'll use Lambda Expression a lot with Panadas library

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
# basically it's a one-line version of a small-function
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


# ----------------    filter()    ----------------
# it's similar to map(), but insteal of mapping a sequence, we'll filter the sequence
# a function/lambda (returns BOOLEAN values) is passed as an argument that will filter out.
seq = [1,2,3,4,5]
list(filter(lambda n: n%2 == 0, seq))
# notice "lambda n: n%2 == 0" returns either True or False (Boolean values)
# filter() returns only the element that are true for the condition "n%2 == 0"


# ----------------    methods    ----------------
# methods are functions that are attached to an object 
# methods canm be caled upon an object using '.' operator
# a method can modify the object and return results or do some actions

# ----  string methods  ----
# For example there are several methods defined for 'string' type object
# following uses string-method "lower"
s = "There And Back Again"
s.lower()   # all charecter to lowercase
s.upper()   # all uppercase
s.split()   # split on the white-space ' '

# split according to a charcter or string
# following splits on "#"
tweet = 'Go Sports! #Sports'
tweet.split('#')[1]
tweet.split('#')[1]     # use index to access specific element


# ----  dictionary methods  ----
d = {'k1': 1,'k2':2}
d.keys()    # get the keys
d.values()  # get the values
d.items()   # dictionary items in a tuple


# ----  list methods  ----
# pop: pop the last item of the list.
    # it changes the list parmanently
lst = [1,2,3]
lst.pop()
print(lst)

ls2 = [1,2,3,4,5]
itm = ls2.pop()     # store popped item to a vriable

# pop specific item
frst = lst.pop(0)
print(ls2)
print(itm)
print(frst)

# append(): appned new item to a list
    # new items appear at the last index
ls2.append('new')
print(ls2)



# ----  in  ----
'x' in [1,2,3]

'x' in ['x', 'y', 'z']


# ----  tuple unpacking  ----
# consider a list of tuples:
x = [(1,2), (3,4), (5,6)]

# accessing items of a tuple from above list
x[0][0]
x[0][1]

# tuple unpacking: iterating through a list of tuples
    # in python, lots of functions do this 

# using a loop:
for item in x:
    print(item[1])

# or
for (a,b) in x:
    print(a)

for (a,b) in x:
    print(b)

# above 3 lopos are actually tuple-unpacking
    # however, () is just a formality, we can do as below
for a,b in x:
    print(b)
# Note that 'x' is an iterable of (i,j) format
# for more: colt_python: 
    # py_ch4_3_4_UnPack_varArg_kwArg.py; 
    # py_ch4_4_9_zip.py


# -------------------    zip    -------------------
# Example 1: Join two tuples together:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)   # <zip object at 0x000001A40B072D80>

# x is one time usable, so we store it in a seperate variable
# list(x)     # [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
pair_nm = list(x)     # [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
pair_nm


# -------------------    UNPACKING a zip    -------------------
# we use * to unpack a zip, with zip()

itr_tup = [(5, 1), (7, 2), (8, 3)]      # an iterable of tuple
unPack = zip(*itr_tup)  # unpacking
list(unPack)    # [(5, 7, 8), (1, 2, 3)]

unPak_name = zip(*pair_nm)  # using kwargs
list(unPak_name)



# ==========     List Unpacking     ==========
# -------------    Problem passing List/Tuple to *args    -------------
    # Using * as an Argument (during function call): Argument Unpacking
    # We can use * as an argument to a function-call to "unpack" values like "List" or "Tuple"

# var-arg: *arg
# kwarg: **arg

# first we define a function "sum_all_values" using var-arg
def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

# we want to pass all elements from a list/tuple as multiple arguments of "sum_all_values"
# sum_all_values(1,30,2,5,6)
    # args: (1, 30, 2, 5, 6)

# following returns ERROR
nums = [1,2,3,4,5,6]
sum_all_values(nums)    # ERROR
    # args: ([1, 2, 3, 4, 5, 6],), list is stored as an element of the *args tuple

# -----------    unpacking list    -----------
# to unpack the list and pass its elemens as individual arguments to *args, we need to use '*' in the function call
sum_all_values(*nums)   # works
    # args: (1, 30, 2, 5, 6)


# -----------    unpacking Tuple    -----------
# following also returns ERROR
nums2 = (1,2,3,4)
sum_all_values(nums2)    # ERROR
#  args: ((1, 2, 3, 4),) tuple is stored as an element of the *args tuple
sum_all_values(*nums2)   # works

