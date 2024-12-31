
################# 9.8 full, 9.9
# copy:  thse 2, and style 2: total 4
#        
#        
################# (29-Dec-24 for 31-Dec-24)

# Courses: PrTla PY for DS & ML >    9.8, 9.9

# ------------    seaborn exercise    ------------

# Recreate the plots shown below (no need to match the exact colors, just focus on the plot itself)

# Dataset
    # We'll use the famous "Titanic" dataset for these exercises. 
    # Later, in the Machine Learning section, we'll revisit this dataset to predict "passenger survival rates"
    # For now, let's focus on visualizing the data with Seaborn.


# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# --------    "Titanic" dataset    --------
# Using the Titanic dataset, recreate the plots below. 
    # There are very few hints since most can be done with just one or two lines of code, 
    # a hint would essentially reveal the solution
    # so pay close attention to the "x and y labels" for hints.

# lets load a builtin dataset of seaborns: 'titanic'
ttnc = sns.load_dataset('titanic')
ttnc.head()

# plot age-fare distribution in jointpolt
sns.jointplot(x='fare', y='age', data=ttnc, kind='scatter')

# plot 'fare' on a "distplot"
# sns.distplot(ttnc['fare'], kde=False, color='red')
sns.set_style('whitegrid')
sns.distplot(ttnc['fare'], bins=30, kde=False, color='red', hist_kws={'edgecolor':'red'})

# make 'boxplot' for "age" and "class"-category
# x= categorical, y= numerical
sns.boxplot(x='class', y='age', data=ttnc, palette= 'rainbow')

# make 'swarmplot' same for "age" and "class"-category
sns.set_style('whitegrid')
sns.swarmplot(x='class', y='age', data=ttnc, palette= 'Set2')

# show countplot of 'sex'
sns.countplot(x='sex', data=ttnc, palette='magma')

# creating heatmap
ttCor = ttnc.corr()     # calculates the correlation matrix for the DataFrame
# corr() computes pairwise correlation coefficients between all numerical columns in ttnc
print(ttCor)

# To set a specific color palette for a heatmap in Seaborn, use the 'cmap' parameter
sns.heatmap(ttCor, cmap='Set2')
plt.title('titanic.corr()')


# ----  Colormap Selection  ----
# Note: For this kind of plot, use a "sequential" or "diverging" colormap for better interpretation
    # do not use "Qualitative" like 'Set2'
# To set a specific color palette for a heatmap in Seaborn, use the 'cmap' parameter
sns.heatmap(ttCor, cmap='coolwarm')
# notice we've used 'coolwarm' from "diverging" colormap
    # because data ranges from -ve to -ve including 0
plt.title('titanic.corr()')


# catagirical distribution of age-gender using "FacetGrid"
fg = sns.FacetGrid(ttnc, col='sex')
fg.map(plt.hist, 'age', color='cyan', edgecolor='c')
plt.show()


