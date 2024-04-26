
# Courses: 
    # A-Z PY for Data-Science    5, 6, 7
    # PrTla PY for DS & ML : 4.4 (boolians)


# ------------    while loop    ------------
# Indentation is used to create "code-block" in python

while False:
    print("Hello")

# infinite loop
""" 
while True:
    print("Hello") 
"""


# Example 1: Counter
counter = 0

while counter < 12:
    print(counter) 
    counter += 1 

print("Hello")




# ------------    for loop    ------------
# iterate through a sequence
for i in range(5):
    print("Hello", i)

# range(5) is actually range(0, 5)
list(range(0, 5))   # [0, 1, 2, 3, 4]


# for each element
mylist = [10, 100, 1000]
for jj in mylist:
    print("jj is equal to:", jj)




# ------------    if-else    ------------

# Example 2: check a random number is +ve or -ve

import numpy as np
from numpy.random import randn

randn()

# if 
# ----- -2 ------ -1 ------ 0 ------ 2 ------- 1 ------
answer = None 
x = randn() 
if x > 1:
    answer = "Greater than 1"  
    print(answer)
print(x)



# if-else
answer = None 
x = randn() 

if x > 1:
    answer = "Greater than 1" 
else:
    answer = "Less than 1" 

print(x) 
print(answer)



# NESTED if-else
#Nested Statements 
answer = None 
x = randn() 

if x > 1:
    answer = "Greater than 1" 
else:
    if x >= -1:
        answer = "Between -1 and 1" 
    else:
        answer = "Less than -1"

print(x) 
print(answer)



# CHAINED or elif
#Chained Statements 
answer = None 
x = randn() 

if x > 1:
    answer = "Greater than 1" 
elif x >= -1:
    answer = "Between -1 and 1" 
else:
    answer = "Less than -1"

print(x) 
print(answer)






# ------------    Python Crash-Course (PrTla)    ------------

# --------    Booleans    --------
# two values 'True' and 'False' are the booliand in python. 
    # Notice both use capitalization. C++ and Java uses 'true' and 'false'


# --------    comparison operators    --------
# >, <, ==, >=, <=, != etc
# these returns boolian values
1>2
1<2
1>=2
1<=2
1==2    # equality
1!=2
# using with strings
'Hi!' == 'bye'
'Hi!' != 'bye'


# --------    Logical Operators    --------
# we can combine "logical" operators with "conditional" operators

# 'and'
(1 < 2) and (2 < 3)
(1 < 2) and (2 > 3)

# 'or'
(1 < 2) or (2 < 3)
(1 < 2) or (2 > 3)

True or False   # True
True and False  # False


# --------    if, elif    --------
# To make a block of code, just indent

# if
if 1<2:
    print('yep!')

if True:
    print('Perform Code')

if True:
    x = 2 + 2 

print(x)

# if-else
if 1 == 2:
    print('First')  # never gonna execute
else:
    print('last')

if 1 != 2:
    print('First')  # Always executes
else:
    print('last')   # skipped

# elif: for multiple conditions
if 1 == 2:
    print('First')  # skipped
elif 3 == 3:
    print('Middle') # execute
else:
    print('last')   # skipped

# always first true elif will executes even if there are multiple treu-elif
if 1 == 2:
    print('First')  # skipped
elif 4 == 4:
    print('second') # execute    
elif 3 == 3:
    print('Middle') # skipped
else:
    print('last')   # skipped



# --------    for, while    --------

# for
    # iterate through a sequence
seq = [1,2,3,4,5]
for item in seq: print(item)

# use any name for 'loop control variable'
for num in seq: 
    print(f"Hello: {num}")


# while
    # always use restriction to loop control variable. Following is infinite loop:
                # i = 1
                # while i < 5:
                #     print(f'i is: {i}')
    # avoid infinite loop: restart the kernel
i = 1
while i < 5:
    print(f'i is: {i}')
    i = i+1




# --------    range    --------
# range: 
    # it's a generator of numerical values
range(0, 5)
list(range(0, 5))   # [0, 1, 2, 3, 4]

for x in range(0, 5):
    print(x)

# 0 to 9. No need to specify start point if increment is 1
for x in range(10):
    print(x)

# 0 to 9 with 2 increment
for x in range(0, 10, 2):
    print(x)




# --------    list comprehension    --------
# its a shorcut for-loop to create a list from a list
# Usinng for-loop instead list-comprehension
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)  # [1, 4, 9, 16]

# using list-comprehension:
[num**2 for num in x]
out = [num**2 for num in x]
print(out)


