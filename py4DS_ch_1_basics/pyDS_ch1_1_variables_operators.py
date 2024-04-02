
################# 1.1:ok; 1.2:ok; 2.1:ok; 3.1:ok, 3.2:ok, 3.3:ok
# copy: copy img, update: new ipynb, py, content_topics
#        
#        
################# (31-mar-24 for 2-apr-24)

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

    # ------------    Anaconda virtual environment    ------------
    # Virtual Environments allow you to set up virtual installations of Python and libraries on your computer. 
    # You can have "multiple versions" of Python or libraries and easily activate or deactivate these environments 
    # Let's see some examples of why you may want to do this
        # Sometimes you'll want to program in different versions of a library. For example:
            # You develop a program with SciKit-Learn 0.17 then SciKit-Learn 0.18 is released
            # You want to explore 0.18 but don't want your old code to break
        # Sometimes you'll to make sure your library installations are in the correct location For example:
            # You want multiple versions of Python on your computer
            # You want one environment with Py 2.7 and another with Py 3.5
        # There is the "virtualenv" library for normal Python distributions
            # Anaconda has a built-in virtual environment manager that makes the whole process really easy
            # http://conda.pydata.org/docs/using/envs.html

    # Commands:
        # conda create --name env_name package_name
            # EG: conda create --name snowflakes biopython
            # EG: conda create --name fluffy numpy
            # if python version isn't specified, the base version will be used
        # activate fluffy
            # there will be different python packages in yor "venev" than the "base env"
            # to install package inside the active environment: 
                # conda install pandas
        # deactivate                

        # specific python version:
            # conda create --name env_name python=3.5 package_name
            # EG: conda create --name mypy3 python=3.5 numpy
            # EG: following creates an environment with entire anaconda ditribution
                # conda create --name mypy3 python=3.5 ANACONDA

        # CHECKS existed venvs:
            # conda info --envs
        
        # changing, cloning & removing environments are straight forward, just Google them


# ----------------    Run jupyter in VS-code    ----------------
# But we're gonna use VS-code to run "Jupyter Notebook - ipynb" files
    # install ipykernel package (vs-code): Running cells with 'Python 3.10.3 64-bit' requires ipykernel package.
    # Allow VS-code in windows sequrity (if pop-up appears)


# Use shortcut keys:
    # Shift + Enter : to run a code and open a 'New cell'
    # ctrl + enter: works for VS-code (Jupyter NB), It only runs a 'cell'
    # ALt + Enter: same as 'Shift + Enter',  to run a code and open a 'New cell'
    # use 'Help -> Keyboard Shortcuts'

    # A Jypyter NB file can be exported as 'py' file

    # Kernel Restart:
        # If you run a infinite loop or somthing that crashing the program
        # use 'Restart' or 'Kernel -> Restart'

    # Markdown Cells:
        # other than 'code-cells' Jypyter has 'markdown cells'



# ----------------    MARKDOWN Basics (ChatGPT)    ----------------
""" 
    These are some of the basic syntaxes for 'formatting text' in Jupyter Markdown. 
    You can combine these elements to create more complex documents.
    


    1. Headings: 
        Use the pound symbol (#) followed by a space to create headings. 
        The number of pound symbols indicates the level of the heading (from 1 to 6, with 1 being the highest level).
            Use #, ##, ###, ####, #####, ###### for For 6-level of 'Headings'
        
        Example:
            # Heading 1
            ## Heading 2
            ### Heading 3



    2. Bold Text:
        Surround the text with double asterisks (**) or double underscores (__)
        "No space"

        Example:
            **Bold Text**
            __Bold Text__



    3. Italic Text:
        Surround the text with single asterisks (*) or single underscores (_)
        "No space"

        Example:
            *Italic Text*
            _Italic Text_



    4. Bulleted Lists:
        Use asterisks (*), plus signs (+), or hyphens (-) "followed by a space"

        Example:
            - Item 1
            - Item 2
                * Sub-item 1
                * Sub-item 2



    5. Numbered Lists:
        Use numbers followed by a period (.) and "a space" to create numbered lists.

        Example:
            1. First item
            2. Second item



    6. Links:
        Enclose the 'text' you want to display in square brackets [] and 
        the 'URL' in parentheses ().

        Example:
            [OpenAI's website](https://openai.com)



    7. Images:
        Similar to links, but with an exclamation mark (!) before the square brackets.
        Also you can use HTML tag <img src>

        Example:
            ![Alt text](path/to/image.png)
            or
            <img src='.././path'>



    8. Horizontal Rule:
        Use three or more hyphens (---), asterisks (***), or underscores (___) on a line by themselves to create a horizontal rule.

        Example:
            ---


    9. Center aligned text
        To center-align text in a Markdown cell in Jupyter Notebook: 
            Use HTML formatting tags. Specifically, you can use the <div> tag with the style attribute set to text-align: center;
        
        Example: 
            <div style="text-align: center; font-size: 40px; font-weight: bold; font-style: italic;">
                This text will be centered.
            </div>
"""



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

