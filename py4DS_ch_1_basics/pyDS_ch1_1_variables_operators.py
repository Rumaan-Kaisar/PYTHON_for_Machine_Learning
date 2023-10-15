
# Courses: A-Z PY for Data-Science    1, 2, 3, 4

# ----------------    Anaconda, jupyter Installation    ----------------
    # install anaconda
    # open command line/terminal
    # run jupyter notebook


# ----------------    Run jupyter in VS-code    ----------------
# But we're gonna use VS-code to run "Jupyter Notebook - ipynb" files
    # install ipykernel package (vs-code): Running cells with 'Python 3.10.3 64-bit' requires ipykernel package.
    # Allow VS-code in windows sequrity (if pop-up appears)



# -----------    basic types    -----------
# integer
x = 2
print(type(x))  # <class 'int'>


# float/double
y = 2.5
print(type(y))  # <class 'float'>


# string 
a = "2.5 Hello"
b = 'There'
c = a + b   # <class 'str'>
print(f"{c}. It's type is: {type(c)}")


# logical/Boolian
q1 = True
print(type(q1)) # <class 'bool'>




# -----------    variables    -----------
A = 10
B = 5

# Arithmetics
C = A + B
D = B / A

print(f"Division:{D}, Addition:{C}")


# math module
import math
print(math.sqrt(144))       # 12.0
print(math.sqrt(A))         # 3.1622776601683795
print(round(math.sqrt(A)))  # 3


# string arithmetics
greeting = "Hello"
name = "Bob"
message = greeting + " " + name
print(message)  # Hello Bob




# ----------    Boolean Variables and Operators    ----------
#Boolean / Logical:
#True
#False
print(4 < 5) # True
print(10 > 100) # False
print(4 == 5) # False

# operators
""" 
        ==
        != <>  here '!=' and '<>' are same operators. '<>' means not equal
        <
        >
        <=
        >=
        and
        or
        not
"""

result = 4 < 5
print(result)   # True
print(type(result))     # <class 'bool'>


result2 = not(5 > 1)
print(result2)      # False
print(result or result2)    # True
print(result and result2)   # False


# '!=' '<> '
print(4 <> 5) # Operator "<>" is not supported in Python 3; use "!=" instead
print(4 != 5) # True


