
#################  4.3:full, 4.4:3.47
# copy: pyDS_ch1_1_PrTla_crshCrs_1.ipynb, pyDS_ch1_4_list_tuples.py, pyDS_ch1_2_loops_control.py
#        
#        
################# (09-Apr-24 for 10-Apr-24) Start here

# Courses: A-Z PY for Data-Science    5, 6, 7


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


