
# Courses: A-Z PY for Data-Science    3.1, 3.2, 3.3, 3.4, 3.5

# Lygometry: Learn Basics -> Detect Unknown-topic -> learn
    # Lygo : darkness
    # metry : measuring

    # Lygometry : measuring unknown
        # Measuring what we dont know and try to master that



# ---------    list    ---------
    # similar to array, but not really
    # similar to 'vector' in R-language

# Behaviour:
    # ordered
    # Mixed Data-types can wwork in same array !!!

a_list_demo = ["A", "Hey", 7, True, 27.5, "B", -100]
print(type(a_list_demo))    # <class 'list'>
print(a_list_demo)


# List can be an element of another list
list_demo_nested = ["There", "is", 7, True, a_list_demo]
print(list_demo_nested)




# ---------    range()    ---------

# use range() to create list or sequence

# range() doesn't creates a list in first-place
    # range() creates a generator or iterator kind-of object
    # which can be used in loop-control, but it doesnot take as much MEMORY as 'list'

# Create a sequnce of numbers
# to get a list from range(), we need to use list()
list(range(15))

# with start-value, end, increment
list(range(15, 70, 3))  # [15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69]

# Notes on range()
""" 
    range() is a class of 'immutable iterable objects'. Their iteration behavior can be compared to lists: 
        you can't call next directly on them; you have to get an iterator by using iter. 

    So no, range is not a generator.

    You may be thinking, "why didn't they make it an iterator"? Well, ranges have some useful properties that wouldn't be possible that way:

        1.  They are immutable, so they can be used as dictionary keys.
        2.  They have the start, stop and step attributes (since Python 3.3), count and index methods and they support in, len and __getitem__ operations.
        3.  You can iterate over the same range multiple times.
"""



# --------    Accessing data from a list    --------
w = ['a', 'b', 'c', 'd', 'e'] 

#  +ve index: starts from 0
w[0]    # 'a'
lngth = len(w)  # list size
w[lngth-1]    # last elemnt: 'e'

# -ve index: starts fr0m -1, from last element
w[-1]   # last element
w[-lngth]   # last element

# update/overrite an element
w[2]    # 'c'
w[2] = "w"  # updting
w[2]    # 'w'




# ---------    slicing    ---------
# assume we are inside sqaure braces []
# 1 colon only
        :   
    # means slice everything, from satrt-finish, it remains same

        start_point : end_point
    # end_point not inclusive

# +ve index
wrd = "Hello, World!"
wrd[8:12]   # 'orld'

# -ve index
wrd[-5:-2]  # 'orl'



# advanced slicing with  " : : " 
# 2 colons
        start_point : end_point : steps

wrd = "Hello, World!"
wrd[2:11]   # 'llo, Worl'
wrd[2:11:1]   # 'llo, Worl'
wrd[2:11:2]   # 'lo ol'

# -ve step


# ---------    instructor code    ---------
letters = ['A', 'B', 'C', 'D' , 'E', 'F', 'G', 'H' , 'I', 'J']
letters
letters[ : ]
letters[2: ]
letters[ :7]
letters[:5]
letters[2:7]

# using -ve index: index 2 equivalent is -8 from back
# one +ve and another -ve
letters[-8:7]
# both -ve
letters[-8:-3]


# Advanced slicing using steps:
letters[2:9]
letters[2:9:2]
letters[:]
# only steps
letters[::3]

# -ve steps returns reversed list
letters[::-1]
letters[2:9:-1] # [] wont work
letters[2:9:-3] # [] wont work
letters[9:2]    # [] wont work

# works with reversed satrt & end
letters[9:2:-1] # index- 2 is not inclusive: ['J', 'I', 'H', 'G', 'F', 'E', 'D']
letters[9:2:-3] # ['J', 'G', 'D']




# ---------    tuple    ---------
# tuples are similar to lists, but they are immutable (i.e. cannot be changed)
# it uses () insted of []

# Its not frequently used in Data-Science
# mostly it used in general purpose python programming
letters_tuple = ('A', 'B', 'C', 'D' , 'E', 'F', 'G', 'H' , 'I', 'J')


