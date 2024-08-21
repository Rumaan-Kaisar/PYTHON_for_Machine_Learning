
################# 7.2: Full, 7.3:
# copy: dataset-csv
#        
#        
################# (20-Aug-24 for 21-Aug-24)

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

# What is the average BasePay ?
sal["BasePay"].mean()

# What is the highest amount of OvertimePay in the dataset ?
sal['OvertimePay'].max()

# What is the job title of  JOSEPH DRISCOLL ? 
# Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).
sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]
sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"]

# How much does JOSEPH DRISCOLL make (including benefits)?
sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"]

# What is the name of highest paid person (including benefits)?
sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]
# or
print(sal.loc[sal['TotalPayBenefits'].idxmax()])

# What is the name of lowest paid person (including benefits)? 
# Do you notice something strange about how much he or she is paid?
sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min()]
## ITS NEGATIVE!! VERY STRANGE
# we noticed a negative payment!! -618.13


# --------    rev[20-Aug-2024]    --------
# What was the average (mean) BasePay of all employees per year? (2011-2014) ?


