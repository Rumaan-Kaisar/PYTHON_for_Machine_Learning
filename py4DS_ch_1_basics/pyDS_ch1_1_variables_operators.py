
################# 1.1: ok; 1.2: ok; 2.1:ok; 3.1: 4:20
# copy: update 'content_topics.txt'
#        
#        
################# (29-mar-24 for 30-mar-24)

# Courses: 
    # A-Z PY for Data-Science    1, 2, 3, 4
    # PrTla PY for DS & ML : 1.1, 1.2; 2.1; 3.1, 3.2, 3.3; 4.1, 4.2, 4.3 (10:50)

# -=-=-=-=-=-=-=-=-    PrTla PY for DS & M    L-=-=-=-=-=-=-=-=-
# Most Popular Python Data Science Libraries
""" 
    NumPy
    SciPy
    Pandas	
    Seaborn	
    SciKit-Learn 	
    MatplotLib
    Plotly
    PySpark
"""

# part 1: Python review
# part 2: Numpy and work with array
# part 3: Pandas: work with CSV, Excel, HTML-web scrapping and SQL-DB
# part 4: Matplotlib: Data visualization
# part 5: Seaborn: Visualization, Interactive plotting techniques, 
                    # Financial and Geographical plotting techniques
# part 6: SciKit-Learn: Implement ML algorithms, regressin, classification, clustering, NLP
# part 7: Big data: spark tech wit AWS & python, Tensor FLow basics



# -=-=-=-=-=-=-=-=-    A-Z PY for Data-Science + PrTla    -=-=-=-=-=-=-=-=-

# Anaconda:
    # it is a distribution of Python 
    # Its an “all-in-one" install that is extremely popular in data science and machine learning!
    # This means it includes not only Python, but many libraries that we use in Data-Science, 
    # It has its own virtual environment system. 

# Jupyter:
    # It is the most popular IDE in data science for exploring and analyzing data!
    # Jupyter is a "development environment" where we can 
            # write code, 
            # display images, and 
            # write down markdown notes.



# ----------------    Anaconda, jupyter Installation    ----------------
    # install anaconda for Python 3.XXX, Graphical installer
        # Note: Do Not check "Add anaconda to my PATH env" & "Register anaconda as ... Python 3.XX"
        # these will make problems if you had pre installed Python envs
    # Go to "Anaconda Navigator" -> "Jupyter Notebook"
            # or
    # open command line/terminal in your 'current folder' [win-path: type 'cmd'] 
    # or use 'cd' in cmd to change the directory
    # cmd >> jupyter notebook


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


