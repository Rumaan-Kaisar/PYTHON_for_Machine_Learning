
# Courses: A-Z PY for Data-Science    5.12, 7.5, 7.6

# ------------    WORLD TRENDS    ------------
# Homework Exercise

# Dataset:
    # Use demographic data CSV file 'DataDemographic.csv'
    # Also use following data

# Country code and life expectancy at birth in 1960 and 2013
Country_Code = list(["ABW","AFG","AGO","ALB","ARE","ARG","ARM","ATG","AUS","AUT","AZE","BDI","BEL","BEN","BFA","BGD","BGR","BHR","BHS","BIH","BLR","BLZ","BOL","BRA","BRB","BRN","BTN","BWA","CAF","CAN","CHE","CHL","CHN","CIV","CMR","COG","COL","COM","CPV","CRI","CUB","CYP","CZE","DEU","DJI","DNK","DOM","DZA","ECU","EGY","ERI","ESP","EST","ETH","FIN","FJI","FRA","FSM","GAB","GBR","GEO","GHA","GIN","GMB","GNB","GNQ","GRC","GRD","GTM","GUM","GUY","HKG","HND","HRV","HTI","HUN","IDN","IND","IRL","IRN","IRQ","ISL","ITA","JAM","JOR","JPN","KAZ","KEN","KGZ","KHM","KIR","KOR","KWT","LAO","LBN","LBR","LBY","LCA","LKA","LSO","LTU","LUX","LVA","MAC","MAR","MDA","MDG","MDV","MEX","MKD","MLI","MLT","MMR","MNE","MNG","MOZ","MRT","MUS","MWI","MYS","NAM","NCL","NER","NGA","NIC","NLD","NOR","NPL","NZL","OMN","PAK","PAN","PER","PHL","PNG","POL","PRI","PRT","PRY","PYF","QAT","ROU","RUS","RWA","SAU","SDN","SEN","SGP","SLB","SLE","SLV","SOM","SSD","STP","SUR","SVK","SVN","SWE","SWZ","SYR","TCD","TGO","THA","TJK","TKM","TLS","TON","TTO","TUN","TUR","TZA","UGA","UKR","URY","USA","UZB","VCT","VEN","VIR","VNM","VUT","WSM","YEM","ZAF","COD","ZMB","ZWE"])
Life_Expectancy_At_Birth_1960 = list([65.5693658536586,32.328512195122,32.9848292682927,62.2543658536585,52.2432195121951,65.2155365853659,65.8634634146342,61.7827317073171,70.8170731707317,68.5856097560976,60.836243902439,41.2360487804878,69.7019512195122,37.2782682926829,34.4779024390244,45.8293170731707,69.2475609756098,52.0893658536585,62.7290487804878,60.2762195121951,67.7080975609756,59.9613658536585,42.1183170731707,54.2054634146342,60.7380487804878,62.5003658536585,32.3593658536585,50.5477317073171,36.4826341463415,71.1331707317073,71.3134146341463,57.4582926829268,43.4658048780488,36.8724146341463,41.523756097561,48.5816341463415,56.716756097561,41.4424390243903,48.8564146341463,60.5761951219512,63.9046585365854,69.5939268292683,70.3487804878049,69.3129512195122,44.0212682926829,72.1765853658537,51.8452682926829,46.1351219512195,53.215,48.0137073170732,37.3629024390244,69.1092682926829,67.9059756097561,38.4057073170732,68.819756097561,55.9584878048781,69.8682926829268,57.5865853658537,39.5701219512195,71.1268292682927,63.4318536585366,45.8314634146342,34.8863902439024,32.0422195121951,37.8404390243902,36.7330487804878,68.1639024390244,59.8159268292683,45.5316341463415,61.2263414634146,60.2787317073171,66.9997073170732,46.2883170731707,64.6086585365854,42.1000975609756,68.0031707317073,48.6403170731707,41.1719512195122,69.691756097561,44.945512195122,48.0306829268293,73.4286585365854,69.1239024390244,64.1918292682927,52.6852682926829,67.6660975609756,58.3675853658537,46.3624146341463,56.1280731707317,41.2320243902439,49.2159756097561,53.0013170731707,60.3479512195122,43.2044634146342,63.2801219512195,34.7831707317073,42.6411951219512,57.303756097561,59.7471463414634,46.5107073170732,69.8473170731707,68.4463902439024,69.7868292682927,64.6609268292683,48.4466341463415,61.8127804878049,39.9746829268293,37.2686341463415,57.0656341463415,60.6228048780488,28.2116097560976,67.6017804878049,42.7363902439024,63.7056097560976,48.3688048780488,35.0037073170732,43.4830975609756,58.7452195121951,37.7736341463415,59.4753414634146,46.8803902439024,58.6390243902439,35.5150487804878,37.1829512195122,46.9988292682927,73.3926829268293,73.549756097561,35.1708292682927,71.2365853658537,42.6670731707317,45.2904634146342,60.8817073170732,47.6915853658537,57.8119268292683,38.462243902439,67.6804878048781,68.7196097560976,62.8089268292683,63.7937073170732,56.3570487804878,61.2060731707317,65.6424390243903,66.0552926829268,42.2492926829268,45.6662682926829,48.1876341463415,38.206,65.6598292682927,49.3817073170732,30.3315365853659,49.9479268292683,36.9658780487805,31.6767073170732,50.4513658536585,59.6801219512195,69.9759268292683,68.9780487804878,73.0056097560976,44.2337804878049,52.768243902439,38.0161219512195,40.2728292682927,54.6993170731707,56.1535365853659,54.4586829268293,33.7271219512195,61.3645365853659,62.6575853658537,42.009756097561,45.3844146341463,43.6538780487805,43.9835609756098,68.2995365853659,67.8963902439025,69.7707317073171,58.8855365853659,57.7238780487805,59.2851219512195,63.7302195121951,59.0670243902439,46.4874878048781,49.969512195122,34.3638048780488,49.0362926829268,41.0180487804878,45.1098048780488,51.5424634146342])
Life_Expectancy_At_Birth_2013 = list([75.3286585365854,60.0282682926829,51.8661707317073,77.537243902439,77.1956341463415,75.9860975609756,74.5613658536585,75.7786585365854,82.1975609756098,80.890243902439,70.6931463414634,56.2516097560976,80.3853658536585,59.3120243902439,58.2406341463415,71.245243902439,74.4658536585366,76.5459512195122,75.0735365853659,76.2769268292683,72.4707317073171,69.9820487804878,67.9134390243903,74.1224390243903,75.3339512195122,78.5466585365854,69.1029268292683,64.3608048780488,49.8798780487805,81.4011219512195,82.7487804878049,81.1979268292683,75.3530243902439,51.2084634146342,55.0418048780488,61.6663902439024,73.8097317073171,62.9321707317073,72.9723658536585,79.2252195121951,79.2563902439025,79.9497804878049,78.2780487804878,81.0439024390244,61.6864634146342,80.3024390243903,73.3199024390244,74.5689512195122,75.648512195122,70.9257804878049,63.1778780487805,82.4268292682927,76.4243902439025,63.4421951219512,80.8317073170732,69.9179268292683,81.9682926829268,68.9733902439024,63.8435853658537,80.9560975609756,74.079512195122,61.1420731707317,58.216487804878,59.9992682926829,54.8384146341464,57.2908292682927,80.6341463414634,73.1935609756098,71.4863902439024,78.872512195122,66.3100243902439,83.8317073170732,72.9428536585366,77.1268292682927,62.4011463414634,75.2682926829268,68.7046097560976,67.6604146341463,81.0439024390244,75.1259756097561,69.4716829268293,83.1170731707317,82.290243902439,73.4689268292683,73.9014146341463,83.3319512195122,70.45,60.9537804878049,70.2024390243902,67.7720487804878,65.7665853658537,81.459756097561,74.462756097561,65.687243902439,80.1288780487805,60.5203902439024,71.6576829268293,74.9127073170732,74.2402926829268,49.3314634146342,74.1634146341464,81.7975609756098,73.9804878048781,80.3391463414634,73.7090487804878,68.811512195122,64.6739024390244,76.6026097560976,76.5326585365854,75.1870487804878,57.5351951219512,80.7463414634146,65.6540975609756,74.7583658536585,69.0618048780488,54.641512195122,62.8027073170732,74.46,61.466,74.567512195122,64.3438780487805,77.1219512195122,60.8281463414634,52.4421463414634,74.514756097561,81.1048780487805,81.4512195121951,69.222,81.4073170731707,76.8410487804878,65.9636829268293,77.4192195121951,74.2838536585366,68.1315609756097,62.4491707317073,76.8487804878049,78.7111951219512,80.3731707317073,72.7991707317073,76.3340731707317,78.4184878048781,74.4634146341463,71.0731707317073,63.3948292682927,74.1776341463415,63.1670487804878,65.878756097561,82.3463414634146,67.7189268292683,50.3631219512195,72.4981463414634,55.0230243902439,55.2209024390244,66.259512195122,70.99,76.2609756097561,80.2780487804878,81.7048780487805,48.9379268292683,74.7157804878049,51.1914878048781,59.1323658536585,74.2469268292683,69.4001707317073,65.4565609756098,67.5223658536585,72.6403414634147,70.3052926829268,73.6463414634147,75.1759512195122,64.2918292682927,57.7676829268293,71.159512195122,76.8361951219512,78.8414634146341,68.2275853658537,72.8108780487805,74.0744146341464,79.6243902439024,75.756487804878,71.669243902439,73.2503902439024,63.583512195122,56.7365853658537,58.2719268292683,59.2373658536585,55.633])

# Country names, codes and regions dataset
Countries_2012_Dataset = list(["Aruba","Afghanistan","Angola","Albania","United Arab Emirates","Argentina","Armenia","Antigua and Barbuda","Australia","Austria","Azerbaijan","Burundi","Belgium","Benin","Burkina Faso","Bangladesh","Bulgaria","Bahrain","Bahamas, The","Bosnia and Herzegovina","Belarus","Belize","Bermuda","Bolivia","Brazil","Barbados","Brunei Darussalam","Bhutan","Botswana","Central African Republic","Canada","Switzerland","Chile","China","Cote d'Ivoire","Cameroon","Congo, Rep.","Colombia","Comoros","Cabo Verde","Costa Rica","Cuba","Cayman Islands","Cyprus","Czech Republic","Germany","Djibouti","Denmark","Dominican Republic","Algeria","Ecuador","Egypt, Arab Rep.","Eritrea","Spain","Estonia","Ethiopia","Finland","Fiji","France","Micronesia, Fed. Sts.","Gabon","United Kingdom","Georgia","Ghana","Guinea","Gambia, The","Guinea-Bissau","Equatorial Guinea","Greece","Grenada","Greenland","Guatemala","Guam","Guyana","Hong Kong SAR, China","Honduras","Croatia","Haiti","Hungary","Indonesia","India","Ireland","Iran, Islamic Rep.","Iraq","Iceland","Israel","Italy","Jamaica","Jordan","Japan","Kazakhstan","Kenya","Kyrgyz Republic","Cambodia","Kiribati","Korea, Rep.","Kuwait","Lao PDR","Lebanon","Liberia","Libya","St. Lucia","Liechtenstein","Sri Lanka","Lesotho","Lithuania","Luxembourg","Latvia","Macao SAR, China","Morocco","Moldova","Madagascar","Maldives","Mexico","Macedonia, FYR","Mali","Malta","Myanmar","Montenegro","Mongolia","Mozambique","Mauritania","Mauritius","Malawi","Malaysia","Namibia","New Caledonia","Niger","Nigeria","Nicaragua","Netherlands","Norway","Nepal","New Zealand","Oman","Pakistan","Panama","Peru","Philippines","Papua New Guinea","Poland","Puerto Rico","Portugal","Paraguay","French Polynesia","Qatar","Romania","Russian Federation","Rwanda","Saudi Arabia","Sudan","Senegal","Singapore","Solomon Islands","Sierra Leone","El Salvador","Somalia","Serbia","South Sudan","Sao Tome and Principe","Suriname","Slovak Republic","Slovenia","Sweden","Swaziland","Seychelles","Syrian Arab Republic","Chad","Togo","Thailand","Tajikistan","Turkmenistan","Timor-Leste","Tonga","Trinidad and Tobago","Tunisia","Turkey","Tanzania","Uganda","Ukraine","Uruguay","United States","Uzbekistan","St. Vincent and the Grenadines","Venezuela, RB","Virgin Islands (U.S.)","Vietnam","Vanuatu","West Bank and Gaza","Samoa","Yemen, Rep.","South Africa","Congo, Dem. Rep.","Zambia","Zimbabwe"])
Codes_2012_Dataset = list(["ABW","AFG","AGO","ALB","ARE","ARG","ARM","ATG","AUS","AUT","AZE","BDI","BEL","BEN","BFA","BGD","BGR","BHR","BHS","BIH","BLR","BLZ","BMU","BOL","BRA","BRB","BRN","BTN","BWA","CAF","CAN","CHE","CHL","CHN","CIV","CMR","COG","COL","COM","CPV","CRI","CUB","CYM","CYP","CZE","DEU","DJI","DNK","DOM","DZA","ECU","EGY","ERI","ESP","EST","ETH","FIN","FJI","FRA","FSM","GAB","GBR","GEO","GHA","GIN","GMB","GNB","GNQ","GRC","GRD","GRL","GTM","GUM","GUY","HKG","HND","HRV","HTI","HUN","IDN","IND","IRL","IRN","IRQ","ISL","ISR","ITA","JAM","JOR","JPN","KAZ","KEN","KGZ","KHM","KIR","KOR","KWT","LAO","LBN","LBR","LBY","LCA","LIE","LKA","LSO","LTU","LUX","LVA","MAC","MAR","MDA","MDG","MDV","MEX","MKD","MLI","MLT","MMR","MNE","MNG","MOZ","MRT","MUS","MWI","MYS","NAM","NCL","NER","NGA","NIC","NLD","NOR","NPL","NZL","OMN","PAK","PAN","PER","PHL","PNG","POL","PRI","PRT","PRY","PYF","QAT","ROU","RUS","RWA","SAU","SDN","SEN","SGP","SLB","SLE","SLV","SOM","SRB","SSD","STP","SUR","SVK","SVN","SWE","SWZ","SYC","SYR","TCD","TGO","THA","TJK","TKM","TLS","TON","TTO","TUN","TUR","TZA","UGA","UKR","URY","USA","UZB","VCT","VEN","VIR","VNM","VUT","PSE","WSM","YEM","ZAF","COD","ZMB","ZWE"])
Regions_2012_Dataset = list(["The Americas","Asia","Africa","Europe","Middle East","The Americas","Asia","The Americas","Oceania","Europe","Asia","Africa","Europe","Africa","Africa","Asia","Europe","Middle East","The Americas","Europe","Europe","The Americas","The Americas","The Americas","The Americas","The Americas","Asia","Asia","Africa","Africa","The Americas","Europe","The Americas","Asia","Africa","Africa","Africa","The Americas","Africa","Africa","The Americas","The Americas","The Americas","Europe","Europe","Europe","Africa","Europe","The Americas","Africa","The Americas","Africa","Africa","Europe","Europe","Africa","Europe","Oceania","Europe","Oceania","Africa","Europe","Asia","Africa","Africa","Africa","Africa","Africa","Europe","The Americas","The Americas","The Americas","Oceania","The Americas","Asia","The Americas","Europe","The Americas","Europe","Asia","Asia","Europe","Middle East","Middle East","Europe","Middle East","Europe","The Americas","Middle East","Asia","Asia","Africa","Asia","Asia","Oceania","Asia","Middle East","Asia","Middle East","Africa","Africa","The Americas","Europe","Asia","Africa","Europe","Europe","Europe","Asia","Africa","Europe","Africa","Asia","The Americas","Europe","Africa","Europe","Asia","Europe","Asia","Africa","Africa","Africa","Africa","Asia","Africa","Oceania","Africa","Africa","The Americas","Europe","Europe","Asia","Oceania","Middle East","Asia","The Americas","The Americas","Asia","Oceania","Europe","The Americas","Europe","The Americas","Oceania","Middle East","Europe","Europe","Africa","Middle East","Africa","Africa","Asia","Oceania","Africa","The Americas","Africa","Europe","Africa","Africa","The Americas","Europe","Europe","Europe","Africa","Africa","Middle East","Africa","Africa","Asia","Asia","Asia","Asia","Oceania","The Americas","Africa","Europe","Africa","Africa","Europe","The Americas","The Americas","Asia","The Americas","The Americas","The Americas","Asia","Oceania","Middle East","Oceania","Middle East","Africa","Africa","Africa","Africa"])


# Problem Description:

# You are required to produce a "SCATTERPLOT" depicting 
    #     Life Expectancy (y-axis) and 
    #     Fertility Rate (x-axis) statistics by Country.

# The scatterplot need to be 'categorised by Countries Regions'.
    # use: Regions_2012_Dataset


# You have been supplied with data for 2 years: 1960 and 2013 
    # you are requires to produce a visualisation for each of these years.

# Some data has been provided in a CSV file, some in Python lists. 
    # The CSV file contains combined data for both years. 
    # All data manipulations have to be 'performed in Python' (not in Excel) 
        
# You also have been requested to provide "insights" into how the two periods compare.

# Hint 1: 
    # Notice, we have 3 data-sets: 'DataDemographic.csv', 'Country names, codes and regions dataset', 'life expectancy dataset'
        # all 3 dataset has a 'Country Code' column
        # Marge these dataframes: we'll combine all these 3 dataset by 'Country Code'
            # How to Marge: First marge the new lists to a new data-frames then combine with 'DataDemographic.csv'.

# Hint 2 (fill in the blanks): 
    # copy & paste provided data (lists)
    # convert those lists to new dataframes
    # marge the new dataframes with the 'DataDemographic.csv'
    # plot the results

# Good Luck!!!




# ------------    WORLD TRENDS : Data Analysis    ------------
# solution:

# Import the following packages needed to perform the analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# plot shown in Jupyter Notebook
%matplotlib inline  
# expand the figure-width
plt.rcParams['figure.figsize'] = 8, 4


# --------    Loading Dataset    --------
# Import the csv dataset
data = pd.read_csv("./DataDemographic.csv")     # load datset

# -=-=-  Explore the data  -=-=-
# Visualize the dataframe
data

# rename the column names to single-string names
data.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
data.head()    # view dataset

# Check top 6 rows
data.head(6)

# Check bottom 7 rows
data.tail(7)

# Check the structure of the data frame
data.info() # it also shows data-types: 2 floats & 3 objects

# Check the summary (statistical info as summery) of the data
data.describe().transpose()     # transpose the table fro better view



# plot 1: SCATTERPLOT illustrating 'Birth Rate' and 'Internet Usage' statistics by Country.
            # The scatterplot needs to also be 'categorised' by Countries’ "Income Groups". 

# Plot the BirthRate versus Internet Users categorized by Income Group
vis1 = sns.lmplot(data = data, x = 'InternetUsers', y = 'BirthRate', hue = 'IncomeGroup', fit_reg = False, height=6, scatter_kws={'s': 10})




# plot 2: SCATTERPLOT illustrating 'Birth Rate' and 'Internet Usage' statistics by Country.
            # However, this time the scatterplot needs to be 'categorised' by Countries’ "Regions".
            # use the given 'list' from the dataset given above "Country names, codes and regions dataset"

# Copy here the data from the homework provided in lists, Country names, codes and regions dataset

# Create the dataframe: Notice how the 'dataframe' is created
    # since we dont have 'Regions' catagory in our dataset, we create a new one
    # Notice how the 'dataframe' is created:
        # column names as 'keyward'
        # 'value' is converted list to numpy-array
        # this 'dictionary' is passed to 'pd.DataFrame()'
country_data = pd.DataFrame({'CountryName': np.array(Countries_2012_Dataset), 
                             'CountryCode': np.array(Codes_2012_Dataset),
                             'CountryRegion': np.array(Regions_2012_Dataset)})


# Explore the datasets
country_data.head() # new dataframe
data.head() # old dataframe

# Merge the country data to the original dataframe. 
# Use pd.merge() 
    # we marge 'DataDemographic.csv' i.e. 'data' to our new dataframe 'country_data'
    # we use "CountryCode" to align the two data-set.
        # in this case "CountryCode" is our primary key
merged_data = pd.merge(left=data, right=country_data, how='inner', on="CountryCode")

# Explore the marged dataset
merged_data.head()


# --------    rename a single column    --------
# https://stackoverflow.com/questions/19758364/rename-specific-columns-in-pandas
# get rid of extra 'CountryName' column
mrgdData_1 = merged_data.drop('CountryName_y', axis=1)
# Rename specific column(s) in pandas. Rename 'CountryName_x' to 'CountryName'
mrgdData_1.rename(columns={'CountryName_x':'CountryName'}, inplace=True)
# 'inplace = True' makes the changes to our original dataframe object

mrgdData_1.head()

""" 
    A much faster implementation would be to use list-comprehension if you need to rename a single column.

                df.columns = ['new_name' if x=='old_name' else x for x in df.columns]


    rename multiple columns:
        If the need arises to rename multiple columns, either use conditional expressions like:

                df.columns = ['new_name1' if x=='old_name1' else 'new_name2' if x=='old_name2' else x for x in df.columns]

        Or, construct a mapping using a dictionary and perform the list-comprehension with it's get operation by setting default value as the old name:

                col_dict = old_name1': 'new_name1', old_name2': 'new_name2'}   ## key→old name, value→new name
                df.columns = [col_dict.get(x, x) for x in df.columns]
"""


# Plot the BirthRate versus Internet Users cathegorized by Country Region
vis2 = sns.lmplot(data = mrgdData_1, x = 'BirthRate', y = 'InternetUsers', hue = 'CountryRegion', fit_reg = False, height=6, scatter_kws={'s': 10})
# notice the hue = 'CountryRegion', to categorize by Region

# Observations: 
    # countries in 'Africa' has 'High-Birthrate' and 'Less-internet-user'
    # Many countries in 'America' has 'Low-Birthrate' and 'High-internet-user'
    # Most countries in 'Europe' has 'Low-Birthrate' and 'High-internet-user'







# ------------------    Challenge: scatterplot 'Life_Expectancy vs Fertility_Rate'    ------------------

# You are required to produce a scatterplot depicting 
    # 'Life Expectancy (y-axis)' and 'Fertility Rate (x-axis)' statistics by Country. (new data from given lists)
    # The scatterplot need to be categorised by 'Countries Regions' (new data from given lists).

# You have been supplied with data for 2 years: 
    # 1960 and 2013 and you are requires to produce a visualisation for each of these years.

# Some data has been provided in a CSV file, some in Python lists. 
    # All data manipulations have to be performed in Python (not in Excel)

# You also have been requested to provide insights into how the two periods compare. 


# Create a data frame with the life expectancy
life_exp_data = pd.DataFrame({'CountryCode': np.array(Country_Code),
                              'LifeExp1960': np.array(Life_Expectancy_At_Birth_1960),
                              'LifeExp2013': np.array(Life_Expectancy_At_Birth_2013)})


# Check row counts
len(life_exp_data) #187 rows
len(mrgdData_1) # 195 rows

# Check summaries
life_exp_data.describe()
# notice the life expectancy increased "17 years" between 1960 and 2013


# NOTE: Did you pick up that there is more than one year in the data? From the challenge we know that there are two: **1960** and **2013**



# Merge the 'dataframe' with the 'life expectancy'
mrgdData_2 = pd.merge(left=mrgdData_1, right=life_exp_data, how='inner', on='CountryCode')

# notice we have 195 rows in our original data, but here we have 187 rows, 
    # 'inner' brings the countries that are in 'both datasets'


# Explore the dataset
mrgdData_2.head()

# Check the new structures
mrgdData_2.info()

# We can see obsolete columns because of the merge operation
# Rename the one of the colunms containing the country names and delete the other
# Note: we dont need delete or rename, becaye we've used 'mrgdData_2' insted of 'merged_data'
del mrgdData_2['CountryName_y'] # delete extra column 
merged_data.rename(columns = {'CountryName_x':'CountryName'}, inplace = True)
# 'inplace = True' makes the changes to our original dataframe object

# Check structures again
merged_data.info()

# Plot the 'BirthRate' versus 'LifeExpectancy' cathegorized by Country Region in 1960; y = 'LifeExp1960'
vis3_1960 = sns.lmplot(data = mrgdData_2, x = 'BirthRate', y = 'LifeExp1960', hue = 'CountryRegion', fit_reg = False, height=6, scatter_kws={'s': 50})
# Observations: 
    # in 1960 Eurrope and America has 'Lower Birthrate' and 'Higher Life Expectancy'
    # African coutries has 'Higher Birthrate' and 'Lower Life Expectancy'


# Plot the BirthRate versus LifeExpectancy cathegorized by Country Region in 2013; y = 'LifeExp2013'
vis3_2013 = sns.lmplot(data = mrgdData_2, x = 'BirthRate', y = 'LifeExp2013', hue = 'CountryRegion', fit_reg = False, height=6, scatter_kws={'s': 50})
# Observations: 
    # in 2013 Eurrope and America has 'Lower Birthrate' and 'Higher Life Expectancy' mostly the same as 1960
    # African coutries has 'Higher Birthrate' and 'Lower Life Expectancy' 
        # However some African coutries 'Decreased' their birthrate in 2013
    # most of the Asian countires increased their 'Life Expectancy' near 70y as well as decreasing birthrate.


