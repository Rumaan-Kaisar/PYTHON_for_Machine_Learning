
################# 9.6: 5.06
# copy:  
#        
#        
################# (18-Dec-24 for 20-Dec-24)

# Courses: PrTla PY for DS & ML >    9.6, 9.7


# ------------    Regression Plots    ------------
# Seaborn includes many tools for regression plots (Regression will be discussed later in the machine learning section)
# For now, we'll focus on the lmplot() function

# import libraries
import seaborn as sns
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# lets load a builtin dataset of seaborns: 'tips'
tips = sns.load_dataset('tips')
tips.head()


# ----  lmplot  ----
# lmplot: Displays linear models and allows:
# Splitting plots by features.
# Coloring using the hue parameter (based off of features)

sns.lmplot(x='total_bill', y='tip', data=tips)
# we got a scatterplot with a linear fit

# use 'hue' for data seperation based on categorical feature
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette="rocket")
# notice 2 scatterplot with 2 linear fit for 'male' and 'feamle'
# so male and female has almost same linear fits for "total_bill vs tips"

# Markers:
# Style the markers using matplotlib "style" parameter (matplotlib marker symbols)
    # scatter_kws is used to pass "matplotlib parameters" directly as a dictionary
    # because sns running matplotlib under the hood. Eg. 's' for marker size
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'v'], scatter_kws={'s':100}, palette="husl")


# more options: Working with Markers
# palette: hls, husl, Set2, Paired (paired colors)
""" 
    "lmplot" passes its keyword arguments to "regplot", a more general form of lmplot().
        "regplot" has a "scatter_kws" parameter, which is passed to "plt.scatter"
        To adjust marker size, set the 's' key in "scatter_kws"
        Note: s controls the squared marker size.
        Use a dictionary for Matplotlib arguments, like {'s': 50} for marker size
    
    In other words you end up passing a dictionary with the base matplotlib arguments, in this case, s for size of a scatter plot.
        You might not remember this detail, so check the documentation when needed. 
        http://matplotlib.org/api/markers_api.html
"""

# use "grid" (seperate plot) insted of seperating by "hue" (do by color)
sns.lmplot(x='total_bill', y='tip', data=tips, col="sex")   # plot for each sex
# Gives two separate column plots separated by the 'sex' category

# we can do this for rows as well
sns.lmplot(x='total_bill', y='tip', data=tips, col="sex", row='time')   # plot for each sex
# This is similar to the grid and FacetGrid call we've done earlier.
# Now it's automatic because we specify 'row' and 'col' by passing them to 'lmplot'

# combined 'hue' (as time) and 'grid' (as sex)
sns.lmplot(x='total_bill', y='tip', data=tips, col="sex", hue='time')
# another example: 'hue' (as sex) and 'grid' (as day)
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', palette='coolwarm')

# ----  5.06 :: rev[18-Dec-2024]  ----
