
################# 9.1: full, 9.2: 4:10
# copy:  update GitHub pyDS_ch6_4_PANDAS_oprtn.ipynb + py
#        
#        
################# (10-Nov-24 for 12-Nov-24)

# Courses: PrTla PY for DS & ML >    9.1, 9.2


# ------------    distribution plots    ------------

# Let's go over some plots that help visualize the distribution of a dataset
        #   distplot
        #   jointplot
        #   pairplot
        #   rugplot
        #   kdeplot

# what is seaborn:
    # Seaborn is a statistical plotting library based on Matplotlib
    # It has default styles that works with pandas DataFrame objects
    # It has a wide range of plot types for visualizing 
        # distributions, 
        # relationships, and 
        # categorical data.

# how to install:
    # conda install seaborn
    # or
    # pip install seaborn

# documentation:
    # GitHub: we can find it on GitHub since it's open-source:  https://github.com/mwaskom/seaborn
    # official: https://seaborn.pydata.org/
        # use "gallery" as reference, eg: heatmap, vilinplot, boxplot, joint plot
        # API: reference for various plot-types


# import libraries
import seaborn as sns
%matplotlib inline  # shows figures in ipynb

# lets load a builtin dataset of seaborn. tips: a dataset of restaurant patrons' tipping behavior
tips = sns.load_dataset('tips')
tips.head()

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')



# ------------    distplot    ------------
# it shows the distribution of uni-variate (one-variable) set of observations
# use a single column of your datsset
sns.distplot(tips['total_bill'])

# Notice we have a "kde (kernel density estimation) layer" (the blue line)
# to remove it, we just use "kde=False"
sns.distplot(tips['tip'], kde=False)
# now we just have a "histogram" is just a distribution of the data-points
# Y-axis is the "counts" and X-axis is the "data"
# so $2 nad $3 are most given tips

# change noumber of bins (depends on dataset)
# bins too high plots every single instance, make your plot wierd
sns.distplot(tips['total_bill'], kde=False, bins=40)
# most of the bills happens in between 10 and 20 dollers


# ----  rev[10-nov-2024]  ----
# ------------    jointplot    ------------
