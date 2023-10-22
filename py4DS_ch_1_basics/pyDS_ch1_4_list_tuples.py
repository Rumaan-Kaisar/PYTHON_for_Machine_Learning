
################# 3.2: full
# copy:  
#        
#        
################# (21-oct-23 for 22-oct-23)

# Courses: A-Z PY for Data-Science    3.1, 3.2,


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

