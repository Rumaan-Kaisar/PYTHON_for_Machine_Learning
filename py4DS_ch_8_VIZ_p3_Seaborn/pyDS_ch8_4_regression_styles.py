
################# 9.6: 3.49
# copy:  
#        
#        
################# (17-Dec-24 for 18-Dec-24)

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


# ----  rev[17-Dec-2024]  ----
# more options

### Working with Markers
# palette: hls, husl, Set2, Paired (paired colors)
# lmplot kwargs get passed through to **regplot** which is a more general form of lmplot(). regplot has a scatter_kws parameter that gets passed to plt.scatter. So you want to set the s parameter in that dictionary, which corresponds (a bit confusingly) to the squared markersize. In other words you end up passing a dictionary with the base matplotlib arguments, in this case, s for size of a scatter plot. In general, you probably won't remember this off the top of your head, but instead reference the documentation.



