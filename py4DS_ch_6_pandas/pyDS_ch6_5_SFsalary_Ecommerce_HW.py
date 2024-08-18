
################# 7.2: Full, 7.3:
# copy: dataset-csv
#        
#        
################# (17-Aug-24 for 18-Aug-24)

# Courses: PrTla PY for DS & ML >   7.2, 7.3, 7.4, 7.5



# ------------    SF Salaries Overview    ------------

""" 
On the Salary Exercise, one of the questions asks 
    how many people have the word "chief" in their title. 
    
    The solution is actually slightly off, 
    We didn't take into account people that had 
        "punctuation" in their title right next to the word "chief", 
        for example : Chief, Justice. 
"""

# We will be using the SF Salaries Dataset: https://www.kaggle.com/kaggle/sf-salaries from Kaggle!
# "kaggle.com" is a good platform to practice Machine Learning


# Import pandas as pd.
import pandas as pd

# Read Salaries.csv as a dataframe called sal.
sal = pd.read_csv("./z_data_Salaries.csv")

# Check the head of the DataFrame
sal.head()

# Use the .info() method to find out how many entries there are
sal.info()


# --------   rev[17-Aug-2024]   --------
# What is the average BasePay ?





