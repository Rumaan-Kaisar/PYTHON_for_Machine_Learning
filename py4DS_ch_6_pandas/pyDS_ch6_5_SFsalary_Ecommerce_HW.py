
################# 7.2: Full, 7.3: 2.33
# copy: 
# UPDATE: 
#        
################# (28-Aug-24 for 30-Aug-24), previous excercise review + current exercise 1 execution

# Courses: PrTla PY for DS & ML >   7.2, 7.3, 7.4, 7.5


# ------------    Exercises 1: SF Salaries Overview    ------------

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



# --------    groupby    --------
# What was the average (mean) BasePay of all employees per year? (2011-2014) ?
yearGroup = sal.groupby("Year")
yearGroup["BasePay"].mean()
# or
sal.groupby('Year').mean()['BasePay']
# following also works
# sal.groupby('Year')['BasePay'].mean()



# --------    operations    --------
# How many unique job titles are there?
jobs = sal["JobTitle"].unique()
len(jobs)
# or
sal['JobTitle'].nunique()

# What are the top 5 most common jobs?
sal["JobTitle"].value_counts().head(5)



# How many Job Titles were represented by only one person in 2013? 
# (e.g. Job Titles with only one occurence in 2013?)
jobs_2013 = sal[sal["Year"] == 2013]
occur_once = jobs_2013["JobTitle"].value_counts() == 1
sum(occur_once)
# or
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...



# --------  use Lambda & apply  --------
# How many people have the word "Chief" in their job title? (This is pretty tricky)
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


# --------  cor()  --------
# Is there a correlation between "length of the Job Title string" and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len','TotalPayBenefits']].corr() # No correlation.


"""  
        Output:
                                    title_len	TotalPayBenefits
                                    
                title_len	        1.000000	-0.036878
                TotalPayBenefits	-0.036878	1.000000


            Notice, the correlation of 'TotalPayBenefits' and 'title_len' is |-0.036878| = 0.036878 which is < 0.3
            i.e. 'TotalPayBenefits' and 'title_len' has no correlation

"""



# --------    Exercises 2: E-commerce Purchases    --------

# You will be given some Fake Data about some purchases done through Amazon!
#     Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.

# Most of the tasks can be solved in different ways.
# All of these questions can be answered with one line of code.


# Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.

# Import pandas as pd.
import pandas as pd

# Read "z_data_Ecommerce_Purchases" as a dataframe called ecom
    # Even though it's a csv file, no ".csv" extension used because file-name has no '.csv' extension. 
ecom = pd.read_csv("./z_data_Ecommerce_Purchases")

# Check the head of the DataFrame
ecom.head()

# How many rows and columns are there?
ecom.info()

# What is the average Purchase Price?

