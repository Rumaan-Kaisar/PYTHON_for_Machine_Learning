
# Courses: A-Z PY for Data-Science    1.10, 7.1

# -------------    PROJECT: Law of Large numbers (LLN)    -------------
# Simple but Powerful concept:
# Consider the "coin toss example"
    # we know we have 50/50 chance of getting HEAD or TAIL.
        # But if we toss the coin for a very fiew time say 10 times, it wont be 50-50
            # toss 10 times: HEAD : TAIL    =  70% : 30%
            # toss 100 times: HEAD : TAIL    =  60% : 40%
            # toss 1000 times: HEAD : TAIL    =  55% : 45%
            # toss 10000 times: HEAD : TAIL    =  51% : 49%


# Law of Large numbers (LLN):
    # Say we have a sample, the 'average of the sample' converges to EXPECTED VALUE of that sample 
        # if the 'number of observations' tends to infinity.



# -----------    Normal distribution of random numbers    -----------
# We got a bell-shaped Normal-Distribution curve
# It says: 
    # There is 34.1% probability that the random number lies between (0, 1)
    # There is 34.1% probability that the random number lies between (-1, 0)
    # There is total 68.2% probability that the random number lies between (-1, 1)


# In our project, we'll test this law of large numbers
""" 
    Test the Law Of Large Numbers for N random normally distributed numbers with 
                    mean = 0,  stdev = 1

        It means that we need to use randn() function.


    Create a Python script that will count how many of these numbers fall between -1 and 1 and 
        divide by the total quantity of N (i.e. find the percentage).
        N = sample size

        You know that E(X) = 68.2%, i.e. 68.2% of those random numbers must fall between -1 and 1.

        Check that Mean(X_N) -> E(X) as you rerun your script while increasing N 
"""

# Hint 1: Generate certain number of random variables

randn(100)

    # returns a list ('numpy.ndarray' actually) of 100 normally distributed random variables
    # Then use a loop over that list

# Hint 2: Follow these steps
    # specify sample size
    # reset counter
    # iterate over random values
    # check where iterated variable falls
    # increase counter if condition is met
    # calculate hit-ratio
    # print answer

from numpy.random import randn

print(randn(10))    # <class 'numpy.ndarray'>
# [-0.25854459  0.78814492  0.92511946 -0.24672421  0.10898456  0.36898421 2.01347659 -0.75617161  1.04532005 -2.30121687]
list(randn(10)) # returns the list

# autometically converts 'numpy.ndarray' to countable
# for i in randn(10):
#     print(i)

N = 1000000
count = 0

for i in randn(N):
    # print(i)
    if (i<1) and (i>-1):
        count += 1

print(count/N)


# -------    Convergence Test    -------
for sample_size in range(1, 1000):    
    N = sample_size
    count = 0
    for i in randn(N):
        # print(i)
        if (i<1) and (i>-1):
            count += 1
    print(count/N)
