
################# 7.2: full
# copy:  
#        
#        
################# (31-oct-23 for 1-nov-23)

# Courses: A-Z PY for Data-Science    3.10


# --------    Section recap    --------
    # What is a list?
    # Created some lists: [], range()
    # Using the [] brackets
    # Slicing Lists
    # Tuples
    # Functions in R 
    # Packages in R 
    # Numpy and Arrays 
    # Slicing Arrays




# --------------------------------------
# Exercise: FINANCIAL STATEMENT ANALYSIS
""" 
    Scenario: You are a Data Scientist working for a consulting firm. 
    One of your colleagues from the Auditing department has asked you to 
    help them assess the financial statement of organisation X.


    You havte been supplied with two lists of data: 

                monthly revenue and 
                monthly expenses 

    for the financial year in question. 

    Your task is to calculate the following financial metrics:
    -	profit for each month
    -	'profit after tax' for each month (the tax rate is 30%)
    -	profit margin for each month - equals to 'profit after tax' divided by revenue
    -	good months - where the 'profit after tax' was greater than the mean for the year
    -	bad months - where the profit aftertax was less than the mean for the year
    -	the best month - where the 'profit after tax' was max for the year
    -	the worst month - where the 'profit after tax' was min for the year


    All results need to be presented as lists.

    Results for dollar values need to be calculated with $0.01 precision, 
        but need to be presented in Units of $ 1,000 (i.e. 1k) with no decimal points.

    Results for the profit margin ratio need to be presented in units of % with no decimal points.

    Note:Your colleague has warned you that it is okay for tax for any given month to be negative 
        (in accounting terms, negative tax translates into a deferred tax asset).


    Use following functions:
                            round()
                            max()
                            min()

"""




# -----------------    SOLUTION    -----------------

# Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


# Calculate Profit As The Differences Between 'Revenue' And 'Expenses'
profit = []

for i in range (0, len(revenue)):
    profit.append(revenue[i] - expenses[i])

print(profit)
# [2522.67, 1911.3900000000003, -3707.790000000001, -2914.3099999999995, -599.9200000000001, 7265.24, 8210.550000000001, 3944.9700000000003, 3328.3899999999994, -2238.6500000000015, 659.5999999999985, 11629.54]

# 3 decimal round
# round(12.5656, 3)




# Calculate Tax As 30% Of Profit And Round To 2 Decimal Points
tax = [round(i * 0.3, 2) for i in profit]
print(tax)
# [756.8, 573.42, -1112.34, -874.29, -179.98, 2179.57, 2463.17, 1183.49, 998.52, -671.6, 197.88, 3488.86]




# Calculate Profit Remaining After Tax Is Deducted
profit_after_tax = []

for i in range (0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])

print(profit_after_tax)
# [1765.8700000000001, 1337.9700000000003, -2595.4500000000007, -2040.0199999999995, -419.94000000000005, 5085.67, 5747.380000000001, 2761.4800000000005, 2329.8699999999994, -1567.0500000000015, 461.71999999999855, 8140.68]





