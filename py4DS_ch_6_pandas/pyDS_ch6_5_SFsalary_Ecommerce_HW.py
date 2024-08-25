
################# 7.2: Full, 7.3:
# copy: dataset-csv
#        
#        
################# (24-Aug-24 for 25-Aug-24), next excercise

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


# Is there a correlation between "length of the Job Title string" and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len','TotalPayBenefits']].corr() # No correlation.


# ----  rev[24-Aug-2024]  ----

# What is pandas.DataFrame.corr()?

"""  
The corr() function in Pandas is used to compute the pairwise correlation of columns in a DataFrame. Correlation measures the statistical relationship between two variables, with the result being a number between -1 and 1:

1: Perfect positive correlation. As one variable increases, the other also increases.
0: No correlation. The variables do not have a linear relationship.
-1: Perfect negative correlation. As one variable increases, the other decreases.
By default, corr() uses the Pearson correlation coefficient, which measures linear relationships. However, Pandas also supports other methods like Kendall’s tau and Spearman’s rho by specifying the method parameter.

"""


Syntax
python
Copy code
DataFrame.corr(method='pearson', min_periods=1)
method: Method of correlation:
'pearson': Standard correlation coefficient (default).
'kendall': Kendall Tau correlation coefficient.
'spearman': Spearman rank correlation coefficient.
min_periods: Minimum number of observations required per pair of columns to have a valid result.
Example
python
Copy code
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'C': [5, 6, 7, 8, 7],
    'D': [10, 8, 6, 4, 2]
}

df = pd.DataFrame(data)

# Calculate pairwise correlation
correlation_matrix = df.corr()
print(correlation_matrix)
Output
css
Copy code
          A         B         C         D
A  1.000000  1.000000  0.832050 -1.000000
B  1.000000  1.000000  0.832050 -1.000000
C  0.832050  0.832050  1.000000 -0.832050
D -1.000000 -1.000000 -0.832050  1.000000
In the output:

Columns A and B have a perfect positive correlation (1.000).
Columns A and D have a perfect negative correlation (-1.000).
Columns A and C have a moderate positive correlation (0.832).
How to Determine if There is Correlation in a Dataset?
Visual Inspection: Plot the data using scatter plots. If the points form a line or a clear pattern, there is likely some correlation.

Calculate Correlation Coefficient: Use df.corr() to calculate the correlation matrix:

Look for values close to 1 or -1 for strong correlations.
Values close to 0 indicate weak or no linear correlation.
Heatmaps: Use a heatmap to visualize the correlation matrix for a quick overview.

python
Copy code
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
Statistical Tests: For more complex datasets, use statistical tests (like Pearson, Spearman, or Kendall) to validate correlations. These tests provide p-values to indicate the significance of the correlation.

Interpreting Correlation
Strong Correlation: |r| > 0.7
Moderate Correlation: 0.3 < |r| < 0.7
Weak or No Correlation: |r| < 0.3
The closer the absolute value of the correlation coefficient is to 1, the stronger the correlation between the variables.

